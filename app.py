"""Water-injection forecast — deterministic AWPB profiles.

Replaces WI_profiles_gen_v7.2.py plus the Spotfire layer that sat downstream of it.
Run with:  streamlit run app.py
"""
from __future__ import annotations

import io
import json
import time
from dataclasses import asdict
from pathlib import Path

import numpy as np
import pandas as pd
import streamlit as st

from wi_forecast import (
    ForecastConfig, cascade as C, charts, event_spans,
    generate_facility_profile, generate_profiles, montecarlo as MC,
    prepare, read_workbook, report as RPT,
)

PROJECT = Path(__file__).parent

# Sidebar defaults come from ForecastConfig so editing config.py is
# enough to change what the app starts with.
DEFAULTS = ForecastConfig()

st.set_page_config(page_title="WI Forecast", page_icon="💧", layout="wide")


# --------------------------------------------------------------------- caching

def _cfg_key(cfg: ForecastConfig) -> str:
    d = asdict(cfg)
    d["start_date"] = cfg.start_date.isoformat()
    d["end_date"] = cfg.end_date.isoformat()
    d["decline_overrides"] = sorted(cfg.decline_overrides.items())
    d["enabled_event_classes"] = list(cfg.enabled_event_classes)
    return json.dumps(d, sort_keys=True)


def _cfg_from_key(key: str) -> ForecastConfig:
    d = json.loads(key)
    d["start_date"] = pd.Timestamp(d["start_date"])
    d["end_date"] = pd.Timestamp(d["end_date"])
    d["decline_overrides"] = dict(d["decline_overrides"])
    d["enabled_event_classes"] = tuple(d["enabled_event_classes"])
    return ForecastConfig(**d)


@st.cache_data(show_spinner=False)
def load_frames(data: bytes) -> dict[str, pd.DataFrame]:
    return read_workbook(io.BytesIO(data))


@st.cache_data(show_spinner="Generating profiles…")
def run_forecast(data: bytes, key: str) -> dict[str, pd.DataFrame]:
    cfg = _cfg_from_key(key)
    inputs = prepare(load_frames(data), cfg)

    profile = generate_profiles(inputs, cfg)
    facilities = generate_facility_profile(inputs, cfg)
    levels = C.classify_facilities(facilities)
    wide = C.build_wide_profile(profile, inputs.mapping,
                                horizon=(cfg.start_date, cfg.end_date))

    result = C.run_cascade(wide, levels, cfg)
    result["profile"] = profile
    result["facilities"] = levels
    result["wedges"] = C.wedges(wide)
    result["unmapped"] = C.unmapped_wells(wide, levels)
    result["spans"] = event_spans(inputs, cfg)
    result["mapping"] = inputs.mapping
    result["raw_facilities"] = inputs.facilities
    return result


def _dist_key(d: MC.Dist) -> list:
    return [d.kind, d.low, d.mode, d.high]


def _spec_key(spec: MC.MCSpec) -> str:
    return json.dumps({
        "n": spec.n_cases, "seed": spec.seed, "year": spec.report_year,
        "vrr": {k: _dist_key(v) for k, v in sorted(spec.vrr.items())},
        "vrr_mode": spec.vrr_mode,
        "vrr_field": _dist_key(spec.vrr_field),
        "well_cap": _dist_key(spec.well_cap),
        "decline": _dist_key(spec.decline),
        "decline_absolute": spec.decline_absolute,
        "facility_cap": _dist_key(spec.facility_cap),
        "oe": _dist_key(spec.oe),
        "shift": _dist_key(spec.schedule_shift),
    }, sort_keys=True)


@st.cache_data(show_spinner="Running Monte Carlo…", max_entries=8)
def run_monte_carlo(data: bytes, cfg_key: str, spec_key: str) -> dict:
    cfg = _cfg_from_key(cfg_key)
    inputs = prepare(load_frames(data), cfg)
    model = MC.build_model(inputs, cfg)

    raw = json.loads(spec_key)
    to_dist = lambda v: MC.Dist(v[0], float(v[1]), float(v[2]), float(v[3]))
    spec = MC.MCSpec(
        n_cases=raw["n"], seed=raw["seed"], report_year=raw["year"],
        vrr={k: to_dist(v) for k, v in raw["vrr"].items()},
        vrr_mode=raw["vrr_mode"],
        vrr_field=to_dist(raw["vrr_field"]),
        well_cap=to_dist(raw["well_cap"]),
        decline=to_dist(raw["decline"]),
        decline_absolute=raw["decline_absolute"],
        facility_cap=to_dist(raw["facility_cap"]),
        oe=to_dist(raw["oe"]),
        schedule_shift=to_dist(raw["shift"]),
    )
    started = time.perf_counter()
    out = MC.run(model, spec)
    out["elapsed"] = time.perf_counter() - started
    out["reservoirs"] = model.reservoirs
    out["n_wells"] = len(model.wells)
    out["n_events"] = len(model.ev_well)
    out["n_facilities"] = model.W2M.shape[0] + model.M2C.shape[0]
    return out


# --------------------------------------------------------------------- sidebar

def sidebar() -> tuple[bytes | None, ForecastConfig, str]:
    st.sidebar.title("💧 WI Forecast")

    upload = st.sidebar.file_uploader("Input workbook", type=["xlsx"])
    data = upload.getvalue() if upload is not None else None
    if data is not None:
        st.sidebar.caption(f"Using **{upload.name}**")

    page = st.sidebar.radio(
        "Output page",
        ["Total constrained", "Manifold profiles", "CPS profiles", "Wedges"],
        help="Chooses what the Outputs tab shows.",
    )

    st.sidebar.divider()
    with st.sidebar.expander("Horizon", expanded=False):
        start = st.date_input("Start", DEFAULTS.start_date)
        end = st.date_input("End", DEFAULTS.end_date)
        year = st.number_input("Reporting year", 2025, 2035,
                               DEFAULTS.report_year, step=1)

    with st.sidebar.expander("Operating efficiency", expanded=True):
        north = st.slider("North OE", 0.5, 1.0, DEFAULTS.north_oe, 0.01)
        south = st.slider("South OE", 0.5, 1.0, DEFAULTS.south_oe, 0.01)
        plant = st.slider("Plant OE", 0.5, 1.0, DEFAULTS.plant_oe, 0.01)
        vrr = st.slider("VRR multiplier (all reservoirs)", 0.5, 2.0,
                        DEFAULTS.vrr_multiplier, 0.05,
                        help="Scales the RMT target for every reservoir. "
                             "Spotfire's ${vrr1} only scaled Mishrif.")

    with st.sidebar.expander("Decline & capacity", expanded=False):
        use_settings = st.checkbox(
            "Use per-reservoir decline from SETTINGS sheet", value=False,
            help="The workbook carries a decline table the original script never read.")
        decline_mult = st.slider("Decline multiplier", 0.0, 3.0,
                                 DEFAULTS.decline_multiplier, 0.05)
        wellcap_mult = st.slider("Well capacity multiplier", 0.5, 2.0,
                                 DEFAULTS.well_cap_multiplier, 0.05)
        faccap_mult = st.slider("Facility capacity multiplier", 0.5, 2.0,
                                DEFAULTS.facility_cap_multiplier, 0.05)

    with st.sidebar.expander("Events", expanded=False):
        classes = st.multiselect(
            "Included event classes", ["NWD", "RWO", "PIC", "Rigless"],
            default=["NWD", "RWO", "PIC", "Rigless"])
        shift = st.slider("Shift all event dates (days)", -180, 365,
                          DEFAULTS.event_date_shift_days, 5,
                          help="Positive slips events later — the hook the "
                               "probabilistic layer will sample over.")

    cfg = ForecastConfig(
        start_date=pd.Timestamp(start), end_date=pd.Timestamp(end),
        north_oe=north, south_oe=south, plant_oe=plant, vrr_multiplier=vrr,
        use_settings_decline=use_settings, decline_multiplier=decline_mult,
        well_cap_multiplier=wellcap_mult, facility_cap_multiplier=faccap_mult,
        enabled_event_classes=tuple(classes), event_date_shift_days=shift,
        report_year=int(year),
    )
    return data, cfg, page


# ----------------------------------------------------------------------- pages

CHAIN = ["TOTAL_RMT_OE", "TOTAL_SUBSURFACE_AGREED", "TOTAL_IIC_TARGET",
         "TOTAL_IIC_END", "AWPB_INJECTION"]


# ----------------------------------------------------------------- inputs tab

def tab_inputs(res: dict, cfg: ForecastConfig) -> None:
    """What the user supplied, before any forecasting happens."""
    spans, mapping = res["spans"], res["mapping"]

    counts = st.columns(4)
    counts[0].metric("Wells mapped", f"{mapping.WELL_NAME.nunique():,}")
    counts[1].metric("Events", f"{len(spans):,}")
    counts[2].metric("Stations", f"{mapping.CPS.nunique():,}")
    counts[3].metric("Manifolds", f"{mapping.Manifold.nunique():,}")

    schedule, connections, tables = st.tabs(
        ["Event schedule", "Connectivity", "Raw sheets"])

    with schedule:
        _input_schedule(spans, cfg)
    with connections:
        _input_connectivity(mapping)
    with tables:
        sheet = st.selectbox("Sheet", ["Events", "Mapping", "Facilities"])
        frame = {"Events": spans, "Mapping": mapping,
                 "Facilities": res["raw_facilities"]}[sheet]
        st.dataframe(frame, width="stretch", hide_index=True)


def _input_schedule(spans, cfg: ForecastConfig) -> None:
    if spans.empty:
        st.info("No events in the workbook.")
        return

    opts = st.columns([1.2, 1.2, 1.4, 1.2])
    color_by = opts[0].radio("Ribbon by", ["EVENT_CLASS", "Reservoir"],
                             format_func=lambda c: "Event" if c == "EVENT_CLASS"
                             else "Reservoir", horizontal=True)
    group_by = opts[1].selectbox("Group rows by", ["None", "CPS", "Reservoir"],
                                 help="Prefixes each row so wells cluster by "
                                      "station or reservoir.")
    classes = opts[2].multiselect("Classes", sorted(spans.EVENT_CLASS.unique()),
                                  default=sorted(spans.EVENT_CLASS.unique()))
    only_horizon = opts[3].checkbox("Horizon only", value=False,
                                    help="Hide events starting after the "
                                         "forecast end date.")

    sel = spans[spans.EVENT_CLASS.isin(classes)]
    if only_horizon:
        sel = sel[sel.in_horizon]
    if sel.empty:
        st.info("Nothing matches that filter.")
        return

    st.plotly_chart(charts.event_histogram(sel, color_by), width="stretch")

    st.plotly_chart(
        charts.event_schedule(sel, color_by, "Intervention schedule",
                              horizon=(cfg.start_date, cfg.end_date),
                              group_by=None if group_by == "None" else group_by),
        width="stretch")

    st.caption("Marker position is the event date and marker area scales with "
               "the target it brings on. Hollow markers start after the "
               "forecast horizon and contribute nothing.")

    beyond = int((~spans.in_horizon).sum())
    if beyond:
        st.caption(f"{beyond} of {len(spans)} events start after "
                   f"{cfg.end_date:%d %b %Y}.")

    by_class = (sel.groupby("EVENT_CLASS")
                   .agg(events=("WELL_NAME", "size"),
                        wells=("WELL_NAME", "nunique"),
                        first=("START", "min"), last=("START", "max"))
                   .reset_index())
    st.dataframe(by_class, width="stretch", hide_index=True)


def _selected_nodes(event) -> list[str]:
    """Node ids from a plotly selection, tolerating shape differences."""
    points = getattr(getattr(event, "selection", None), "points", None)
    if not points:
        return []
    out = []
    for pt in points:
        cd = pt.get("customdata") if isinstance(pt, dict) else None
        if isinstance(cd, (list, tuple)):
            cd = cd[0] if cd else None
        if isinstance(cd, str):
            out.append(cd)
    return out


def _input_connectivity(mapping) -> None:
    expanded: set[str] = st.session_state.setdefault("mm_expanded", set())
    tree = charts.mindmap_tree(mapping)

    bar = st.columns([1, 1, 1, 3])
    if bar[0].button("Expand stations"):
        expanded.update(tree[charts.ROOT])
        st.session_state.pop("mm_last", None)
    if bar[1].button("Expand all"):
        expanded.update(k for k, v in tree.items() if v)
        st.session_state.pop("mm_last", None)
    if bar[2].button("Collapse all"):
        expanded.clear()
        st.session_state.pop("mm_last", None)

    event = st.plotly_chart(charts.mindmap(mapping, expanded), width="stretch",
                            key="mindmap", on_select="rerun")

    # A click keeps its selection across reruns, so only act when it changes.
    picked = _selected_nodes(event)
    signature = tuple(sorted(picked))
    if picked and signature != st.session_state.get("mm_last"):
        st.session_state["mm_last"] = signature
        for node in picked:
            if not tree.get(node):
                continue                      # a well has nothing to open
            expanded.symmetric_difference_update({node})
        st.rerun()

    st.caption("Click a node to open or close it. Filled circles have children; "
               "hollow ones are leaves.")

    norm = lambda x: str(x).replace(" ", "")
    view = mapping.copy()
    view["MANIFOLD"] = view.CPS.map(norm) + "_" + view.Manifold.map(norm)
    open_cps = {n.split(":", 1)[1] for n in expanded if n.startswith("cps:")}
    open_man = {n.split(":", 1)[1] for n in expanded if n.startswith("man:")}
    if open_cps or open_man:
        view = view[view.CPS.map(norm).isin(open_cps) | view.MANIFOLD.isin(open_man)]
        st.markdown(f"**{len(view)} well(s) in the open branches**")
    else:
        st.markdown(f"**{len(view)} well(s) in total**")
    st.dataframe(
        view[["WELL_NAME", "CPS", "Manifold", "Reservoir", "Location", "Status"]],
        width="stretch", hide_index=True)



def page_total(res: dict, cfg: ForecastConfig) -> None:
    field = res["field"]
    yr = field[field.DATE.dt.year == cfg.report_year]
    if yr.empty:
        st.warning(f"No data in {cfg.report_year}.")
        return

    avg = yr[CHAIN].mean()
    cols = st.columns(5)
    for col, name in zip(cols, CHAIN):
        col.metric(charts.LABELS.get(name, name), f"{avg[name]:,.1f}")

    left, right = st.columns(2)
    with left:
        st.plotly_chart(
            charts.profile_lines(yr, CHAIN,
                                 f"Field constraint chain — {cfg.report_year}",
                                 filled=("AWPB_INJECTION",)),
            width="stretch")
    with right:
        st.plotly_chart(
            charts.waterfall(C.deferment_waterfall(field, cfg, cfg.report_year),
                             f"Deferment waterfall — {cfg.report_year}"),
            width="stretch")

    losses = pd.DataFrame({
        "Step": ["Well capacity", "Manifold capacity", "CPS capacity", "Plant efficiency"],
        "Loss, mbd": [
            avg.TOTAL_SUBSURFACE_AGREED - avg.TOTAL_RMT_OE,
            avg.TOTAL_IIC_TARGET - avg.TOTAL_SUBSURFACE_AGREED,
            avg.TOTAL_IIC_END - avg.TOTAL_IIC_TARGET,
            avg.AWPB_INJECTION - avg.TOTAL_IIC_END,
        ]})
    losses["% of RMT target"] = losses["Loss, mbd"] / avg.TOTAL_RMT_OE * 100
    st.dataframe(losses, width="stretch", hide_index=True)


def page_level(res: dict, cfg: ForecastConfig, level: str) -> None:
    """Shared renderer for the manifold and CPS pages.

    One panel per entity - a trellis - so every manifold or CPS can be read on
    its own axes while staying on a single page.
    """
    if level == "manifold":
        df, key, cap = res["manifold"], "FAC_MANIFOLD", "CAP-OE"
        title_name, default_cols, value = "Manifold", 4, "TOTAL_IIC_TARGET"
        series = ["TOTAL_RMT_OE", "TOTAL_SUBSURFACE_AGREED", "TOTAL_IIC_TARGET", cap]
        chain = ["TOTAL_RMT_OE", "TOTAL_SUBSURFACE_AGREED", "TOTAL_IIC_TARGET"]
        gap = "Manifold-AGREED-Capacity_Gap"
    else:
        df, key, cap = res["cps"], "CPS", "CAP-OE_CPS"
        title_name, default_cols, value = "CPS", 3, "TOTAL_IIC_END"
        series = ["TOTAL_RMT_OE", "TOTAL_SUBSURFACE_AGREED", "TOTAL_IIC_TARGET",
                  "TOTAL_IIC_END", cap]
        chain = ["TOTAL_RMT_OE", "TOTAL_SUBSURFACE_AGREED", "TOTAL_IIC_TARGET",
                 "TOTAL_IIC_END"]
        gap = "CPS-AGREED_TARG-capacity_gap"

    yr = df[df.DATE.dt.year == cfg.report_year]
    if yr.empty:
        st.warning(f"No data in {cfg.report_year}.")
        return

    names = sorted(yr[key].dropna().unique())
    chosen = st.multiselect(key, names, default=names)
    sel = yr[yr[key].isin(chosen)]
    if sel.empty:
        st.info(f"Select at least one {key}.")
        return

    opts = st.columns([1, 1, 4])
    ncols = opts[0].slider("Columns", 1, 6, default_cols, key=f"cols_{level}")
    shared = opts[1].checkbox("Shared y-axis", value=False, key=f"sy_{level}",
                              help="Lock every panel to the same scale for "
                                   "direct comparison.")

    left, right = st.columns([3, 2])
    with left:
        st.plotly_chart(
            charts.trellis(sel, key, series,
                           f"{title_name} profiles — {cfg.report_year}",
                           dashed=(cap,), filled=(value,),
                           ncols=ncols, shared_y=shared),
            width="stretch")
    with right:
        st.plotly_chart(
            charts.waterfall(_level_waterfall(sel, cap),
                             f"{title_name} waterfall — {cfg.report_year}"),
            width="stretch")

    st.subheader(f"Where capacity binds — {cfg.report_year}")
    table = C.constraint_table(sel, key, cap, value)
    total = pd.DataFrame([{
        key: "ALL SELECTED",
        "days_capacity": int((sel.groupby("DATE")[cap].sum().lt(
            sel.groupby("DATE")["TOTAL_SUBSURFACE_AGREED"].sum())).sum()),
        "rate_capacity": table["rate_capacity"].sum(),
        "days_rmt": int((sel.groupby("DATE")[value].sum().lt(
            sel.groupby("DATE")["TOTAL_RMT_OE"].sum())).sum()),
        "rate_rmt": table["rate_rmt"].sum(),
    }])
    display = pd.concat([total, table], ignore_index=True).rename(columns={
        key: title_name,
        "days_capacity": "Days capacity-constrained",
        "rate_capacity": "Deferred vs agreed, mbd",
        "days_rmt": "Days below RMT target",
        "rate_rmt": "Shortfall vs RMT_OE, mbd"})
    st.dataframe(display.round(2), width="stretch", hide_index=True)
    st.caption(
        "*Days capacity-constrained* counts days the agreed target exceeded "
        "capacity, and *Deferred vs agreed* is that shortfall spread over every "
        "day of the period, so it reads as an annual average rate. The RMT "
        "columns compare the same constrained rate against the reservoir target, "
        "so they also carry whatever the wells themselves could not take — which "
        "is why those days are almost always the full period.")
    if level == "cps":
        st.caption(
            "At station level both columns measure against the **agreed** "
            "target, not against what the manifolds already removed upstream. "
            "That answers *would this station have constrained the wells on its "
            "own*, so it will not match the incremental CPS step in the "
            "waterfall, which is near zero.")


def _level_waterfall(sel: pd.DataFrame, cap: str) -> pd.DataFrame:
    daily = sel.groupby("DATE").sum(numeric_only=True)
    rmt_oe = daily["TOTAL_RMT_OE"].mean()
    agreed = daily["TOTAL_SUBSURFACE_AGREED"].mean()
    iic_t = daily["TOTAL_IIC_TARGET"].mean()
    rows = [
        {"step": "RMT_OE", "value": rmt_oe, "kind": "total"},
        {"step": "Well Cap. Const", "value": agreed - rmt_oe, "kind": "delta"},
        {"step": "Man Cap. Const", "value": iic_t - agreed, "kind": "delta"},
    ]
    if "TOTAL_IIC_END" in daily:
        iic_e = daily["TOTAL_IIC_END"].mean()
        rows.append({"step": "CPS Const", "value": iic_e - iic_t, "kind": "delta"})
        rows.append({"step": "Constrained rate", "value": iic_e, "kind": "total"})
    else:
        rows.append({"step": "Constrained rate", "value": iic_t, "kind": "total"})
    return pd.DataFrame(rows)


def page_wedges(res: dict, cfg: ForecastConfig) -> None:
    w = res["wedges"]
    yr = w[w.DATE.dt.year == cfg.report_year]
    if yr.empty:
        st.warning(f"No data in {cfg.report_year}.")
        return

    classes = list(C.EVENT_CLASSES) + ["Future Options"]
    avg = yr[classes].mean()

    cols = st.columns(len(classes))
    for col, name in zip(cols, classes):
        col.metric(name, f"{avg[name]:,.1f}")

    st.plotly_chart(
        charts.wedge_area(yr, classes, f"Agreed target build-up — {cfg.report_year}"),
        width="stretch")

    steps = _wedge_steps(res, cfg)

    st.plotly_chart(charts.waterfall(steps, f"Wedges — {cfg.report_year}"),
                    width="stretch")


# --------------------------------------------------------- probabilistic tab

DIST_HELP = ("Low / Mode / High are read per distribution. Fixed uses Mode only. "
             "Uniform ignores Mode. Normal centres on Mode with the range at "
             "+/- 3 standard deviations, truncated. PERT is a smoother triangular.")


def _dist_inputs(label: str, key: str, default: MC.Dist, step: float,
                 fmt: str = "%.2f", help_text: str | None = None) -> MC.Dist:
    """Distribution type plus its three points, on one row."""
    st.markdown(f"**{label}**")
    if help_text:
        st.caption(help_text)
    cols = st.columns([1.4, 1, 1, 1])
    kind = cols[0].selectbox("Distribution", MC.DISTRIBUTIONS, key=f"{key}_kind",
                             index=MC.DISTRIBUTIONS.index(default.kind),
                             label_visibility="collapsed")
    low = cols[1].number_input("Low", value=float(default.low), step=step,
                               format=fmt, key=f"{key}_low")
    mode = cols[2].number_input("Mode", value=float(default.mode), step=step,
                                format=fmt, key=f"{key}_mode")
    high = cols[3].number_input("High", value=float(default.high), step=step,
                                format=fmt, key=f"{key}_high")
    return MC.Dist(kind, low, mode, high)


def _vrr_editor(reservoirs: list[str]) -> tuple[dict[str, MC.Dist], str, MC.Dist]:
    """VRR inputs, plus how widely one draw is shared.

    The sharing choice drives the result more than the distribution does:
    independent draws across hundreds of wells average out and barely move the
    field total, while a single field-wide draw carries straight through.
    """
    st.markdown("**VRR multiplier**")
    mode = st.radio(
        "Apply the draw", MC.VRR_MODES, index=MC.VRR_MODES.index(MC.VRR_PER_RESERVOIR),
        format_func=lambda m: MC.VRR_MODE_LABELS[m], horizontal=True, key="pw_vrr_mode",
        help="Per well: every well draws its own multiplier, which mostly "
             "averages out across the field. Per reservoir: one draw shared by "
             "every well in that reservoir. Whole field: one draw shared by "
             "every well, so the full range reaches the total.")

    if mode == MC.VRR_PER_CASE:
        st.caption("One multiplier per case, applied to every well in the field.")
        field_dist = _dist_inputs("VRR multiplier, field-wide", "pw_vrr_field",
                                  MC.Dist("PERT", 0.95, 1.0, 1.05), 0.05)
        return {}, mode, field_dist

    st.caption("Scales the RMT target of every well in that reservoir."
               + (" Each well draws separately." if mode == MC.VRR_PER_WELL
                  else " One draw per reservoir per case."))
    frame = pd.DataFrame([
        {"Reservoir": r, "Distribution": "Fixed", "Low": 1.0, "Mode": 1.0, "High": 1.0}
        for r in reservoirs])

    edited = st.data_editor(
        frame, key="vrr_editor", width="stretch", hide_index=True,
        column_config={
            "Reservoir": st.column_config.TextColumn(disabled=True),
            "Distribution": st.column_config.SelectboxColumn(
                options=list(MC.DISTRIBUTIONS), required=True),
            "Low": st.column_config.NumberColumn(format="%.2f", step=0.05),
            "Mode": st.column_config.NumberColumn(format="%.2f", step=0.05),
            "High": st.column_config.NumberColumn(format="%.2f", step=0.05),
        })
    table = {row.Reservoir: MC.Dist(row.Distribution, row.Low, row.Mode, row.High)
             for row in edited.itertuples()}
    return table, mode, MC.Dist()


def tab_probabilistic(data: bytes, cfg: ForecastConfig, res: dict) -> None:
    reservoirs = sorted({str(r) for r in res["mapping"]["Reservoir"].dropna().unique()})

    st.caption("Every multiplier is drawn per entity, not once for the field: "
               "each well gets its own capacity and decline draw, each facility "
               "its own capacity draw, each event its own slip.")

    days = len(pd.date_range(max(cfg.start_date,
                                 pd.Timestamp(f"{cfg.report_year}-01-01")),
                             min(cfg.end_date,
                                 pd.Timestamp(f"{cfg.report_year}-12-31"))))
    if days < 365:
        st.info(f"The horizon covers only {days} days of {cfg.report_year}, so "
                f"every annual average on this tab is the mean over those days, "
                f"not a full year.")

    left, right = st.columns([3, 1])

    with left:
        with st.expander("Uncertainties", expanded=True):
            vrr, vrr_mode, vrr_field = _vrr_editor(reservoirs)
            st.divider()
            well_cap = _dist_inputs(
                "Well capacity multiplier", "pw_cap", MC.Dist("PERT", 0.8, 1.0, 1.2),
                0.05, help_text="Applied per well to WELL_CAP, base and events.")
            st.divider()
            absolute = st.checkbox(
                "Treat decline as an absolute value rather than a multiplier",
                value=False, key="pw_decl_abs",
                help="Off: the draw scales the workbook DECLINE. "
                     "On: the draw replaces it, as a fraction per year.")
            decline = _dist_inputs(
                "Well decline", "pw_decl",
                MC.Dist("Triangular", 0.05, 0.06, 0.10) if absolute
                else MC.Dist("PERT", 0.7, 1.0, 1.5),
                0.01, fmt="%.3f", help_text="Drawn per well.")
            st.divider()
            fac_cap = _dist_inputs(
                "Facility capacity multiplier", "pw_fac",
                MC.Dist("PERT", 0.9, 1.0, 1.05), 0.05,
                help_text="Drawn per manifold and per station.")
            st.divider()
            if not (cfg.north_oe == cfg.south_oe == cfg.plant_oe):
                st.warning(
                    f"The sidebar has North {cfg.north_oe:.2f}, South "
                    f"{cfg.south_oe:.2f} and Plant {cfg.plant_oe:.2f}. The "
                    f"probabilistic OE is a single value applied to all three, "
                    f"so results here will not line up with the Outputs tab "
                    f"until those three match.")
            oe = _dist_inputs(
                "Operating efficiency", "pw_oe",
                MC.Dist("PERT", round(cfg.plant_oe - 0.06, 2), cfg.plant_oe,
                        round(cfg.plant_oe + 0.06, 2)),
                0.01, help_text="One draw per case, replacing North, South and "
                                "plant OE together. Set it to Fixed at the "
                                "sidebar value to reproduce the deterministic case.")
            st.divider()
            shift = _dist_inputs(
                "Schedule slip, days", "pw_shift",
                MC.Dist("Triangular", 0.0, 0.0, 90.0), 5.0, fmt="%.0f",
                help_text="Drawn per event. Positive slips the activity later.")
            st.caption(DIST_HELP)

    with right:
        st.markdown("**Run**")
        n_cases = st.number_input("Cases", 10, 5000, 250, step=50, key="pw_n")
        seed = st.number_input("Seed", 0, 10**6, 0, step=1, key="pw_seed",
                               help="Same seed and settings reproduce a run exactly.")
        go_now = st.button("Run Monte Carlo", type="primary", width="stretch")

    spec = MC.MCSpec(n_cases=int(n_cases), seed=int(seed),
                     report_year=cfg.report_year, vrr=vrr, vrr_mode=vrr_mode,
                     vrr_field=vrr_field, well_cap=well_cap,
                     decline=decline, decline_absolute=absolute,
                     facility_cap=fac_cap, oe=oe, schedule_shift=shift)
    key = _spec_key(spec)
    if go_now:
        st.session_state["mc_key"] = key

    if st.session_state.get("mc_key") is None:
        st.info("Set the uncertainties, then press **Run Monte Carlo**.")
        return
    if st.session_state["mc_key"] != key:
        st.warning("Settings have changed since the last run - press "
                   "**Run Monte Carlo** to refresh.")

    out = run_monte_carlo(data, _cfg_key(cfg), st.session_state["mc_key"])
    st.session_state["mc_result"] = out
    _render_mc(out, res, cfg)


LEVEL_LABELS = {"field": "Field", "manifold": "Manifold", "cps": "CPS"}


def _profile_view(out: dict, cfg: ForecastConfig, det_field: pd.DataFrame,
                  res: dict) -> None:
    """Probabilistic profile at whichever level the user wants."""
    note = out.get("facility_note")
    stored = out.get("manifold_daily") is not None

    levels = list(MC.FAN_LEVELS) if stored else ["field"]
    controls = st.columns([1.3, 2.7])
    level = controls[0].radio("Level", levels,
                              format_func=lambda l: LEVEL_LABELS[l],
                              horizontal=True, key="mc_fan_level")
    if note:
        st.warning(note)

    if level == "field":
        metric = controls[1].selectbox(
            "Metric", MC.METRICS, index=MC.METRICS.index("AWPB_INJECTION"),
            format_func=lambda m: charts.LABELS.get(m, m), key="mc_fan_metric")
        band = MC.fan(out, metric)
        det_series = None
        if metric in det_field.columns:
            det_series = (det_field.set_index("DATE")[metric]
                          .reindex(band["DATE"]).to_numpy())
        title = (f"{charts.LABELS.get(metric, metric)} — "
                 f"min / P10 / P50 / P90 / max through {cfg.report_year}")
        colour_key = metric
    else:
        names = MC.facility_names(out, level)
        chosen = controls[1].multiselect(
            LEVEL_LABELS[level], names, default=names, key=f"mc_fan_{level}")
        if not chosen:
            st.info(f"Select at least one {LEVEL_LABELS[level].lower()}.")
            return
        band = MC.fan_facilities(out, level, chosen)
        det_series = _deterministic_facility(res, cfg, level, chosen, band["DATE"])
        metric = ("TOTAL_IIC_TARGET" if level == "manifold" else "TOTAL_IIC_END")
        scope = ("all" if len(chosen) == len(names) else f"{len(chosen)} of {len(names)}")
        title = (f"{charts.LABELS[metric]} — {scope} "
                 f"{LEVEL_LABELS[level].lower()}s, {cfg.report_year}")
        colour_key = metric

    st.plotly_chart(
        charts.fan_chart(band, colour_key, title, deterministic=det_series),
        width="stretch")

    st.caption("Bands are taken across cases on each day — the inner one is "
               "P10-P90, the outer the full min-max of every case run. They are "
               "a spread of daily rates, not individual realisations: no single "
               "case follows the max line all year, and the case that sets the "
               "minimum on one day is rarely the one that sets it on the next.")
    if level != "field":
        st.caption("Cases are summed over the selection first and percentiles "
                   "taken afterwards, so this is the spread of the group as a "
                   "whole rather than the sum of each facility's own P90.")

    summary = pd.DataFrame([{
        "Annual average, mbd": "value",
        "Min": band["min"].mean(), "P10": band["low"].mean(),
        "P50": band["p50"].mean(), "Mean": band["mean"].mean(),
        "P90": band["high"].mean(), "Max": band["max"].mean(),
    }]).drop(columns="Annual average, mbd")
    st.dataframe(summary.round(1), width="stretch", hide_index=True)


def _deterministic_facility(res: dict, cfg: ForecastConfig, level: str,
                            chosen: list[str], dates) -> np.ndarray | None:
    """The deterministic curve for the same selection, for the reference line."""
    key, column = (("FAC_MANIFOLD", "TOTAL_IIC_TARGET") if level == "manifold"
                   else ("CPS", "TOTAL_IIC_END"))
    df = res.get(level)
    if df is None or key not in df.columns:
        return None
    sel = df[(df.DATE.dt.year == cfg.report_year) & (df[key].isin(chosen))]
    if sel.empty:
        return None
    daily = sel.groupby("DATE")[column].sum()
    return daily.reindex(dates).to_numpy()


def _render_mc(out: dict, res: dict, cfg: ForecastConfig) -> None:
    results = out["results"]
    det_field = res["field"]
    det_field = det_field[det_field.DATE.dt.year == cfg.report_year]
    deterministic = {m: det_field[m].mean() for m in MC.METRICS
                     if m in det_field.columns}

    elapsed = max(out["elapsed"], 1e-6)
    st.success(f"{len(results):,} cases in {out['elapsed']:.1f}s "
               f"({len(results) / elapsed:,.0f} cases/s) - "
               f"{out['n_wells']} wells, {out['n_events']} events and "
               f"{out['n_facilities']} facilities sampled per case")

    summary = MC.summarise(results)
    summary.insert(1, "Deterministic",
                   [deterministic.get(m, float("nan")) for m in summary["Metric"]])
    summary["Metric"] = [charts.LABELS.get(m, m) for m in summary["Metric"]]
    st.dataframe(summary.round(1), width="stretch", hide_index=True)

    awpb = results["AWPB_INJECTION"].to_numpy()
    p10, p50, p90 = np.percentile(awpb, [10, 50, 90])
    cols = st.columns(4)
    cols[0].metric("AWP&B P10", f"{p10:,.1f}")
    cols[1].metric("AWP&B P50", f"{p50:,.1f}")
    cols[2].metric("AWP&B P90", f"{p90:,.1f}")
    cols[3].metric("P90 - P10", f"{p90 - p10:,.1f}")

    profile_tab, waterfall_tab, tornado_tab, hist_tab = st.tabs(
        ["Profile", "Waterfall", "Tornado", "Histograms"])

    with profile_tab:
        _profile_view(out, cfg, det_field, res)

    with waterfall_tab:
        wf = MC.waterfall_stats(results)
        st.plotly_chart(
            charts.waterfall_uncertainty(
                wf, f"Deferment chain with uncertainty - {cfg.report_year}"),
            width="stretch")
        st.caption("Bar labels are the mean step size. Whiskers show the "
                   "P10-P90 of each brick edge.")
        show = wf[["step", "delta_mean", "delta_low", "delta_high",
                   "bottom_mean", "top_mean"]].rename(columns={
                       "step": "Step", "delta_mean": "Mean", "delta_low": "P10",
                       "delta_high": "P90", "bottom_mean": "Bottom",
                       "top_mean": "Top"})
        st.dataframe(show.round(1), width="stretch", hide_index=True)

    with tornado_tab:
        t_metric = st.selectbox(
            "Metric", MC.METRICS, index=MC.METRICS.index("AWPB_INJECTION"),
            format_func=lambda m: charts.LABELS.get(m, m), key="mc_tor_metric")
        stats = MC.tornado_stats(out, metric=t_metric)
        if stats.empty:
            st.info("Nothing to rank - every input is currently Fixed.")
        else:
            st.plotly_chart(
                charts.tornado(
                    stats, f"What moves {charts.LABELS.get(t_metric, t_metric)} - "
                           f"{cfg.report_year}"),
                width="stretch")
            st.caption("Each bar is the effect of moving that input from its own "
                       "P10 to its P90 with the others held at their mean, taken "
                       "from a regression across the cases. Green raises the "
                       "forecast, red lowers it.")
            st.dataframe(
                stats.sort_values("abs_swing", ascending=False)[
                    ["driver", "low", "high", "swing", "corr"]]
                .rename(columns={"driver": "Driver", "low": "At input P10",
                                 "high": "At input P90", "swing": "Swing",
                                 "corr": "Rank corr"}).round(2),
                width="stretch", hide_index=True)

    with hist_tab:
        st.plotly_chart(
            charts.histograms(results, MC.METRICS, deterministic=deterministic),
            width="stretch")
        st.caption("Black lines mark P10 / P50 / P90. The red dashed line is the "
                   "deterministic case from the Outputs tab.")

    with st.expander("Case results"):
        st.dataframe(results.round(2), width="stretch", hide_index=True)
        st.download_button("mc_cases.csv", results.to_csv(index=False).encode(),
                           file_name="mc_cases.csv", mime="text/csv", key="dl_mc")


# ----------------------------------------------------------------- export tab

def tab_export(cfg: ForecastConfig, res: dict) -> None:
    mc = st.session_state.get("mc_result")

    st.caption("Pick what to include and download a 16:9 deck. Charts are drawn "
               "at slide type sizes rather than scaled-down browser charts, so "
               "they stay readable when projected.")

    groups: dict[str, list] = {}
    for item in RPT.MENU:
        groups.setdefault(item.group, []).append(item)

    selected: list[str] = []
    columns = st.columns(len(groups))
    for col, (group, items) in zip(columns, groups.items()):
        with col:
            st.markdown(f"**{group}**")
            for item in items:
                disabled = item.needs_mc and mc is None
                checked = st.checkbox(
                    item.label, value=not disabled and not item.needs_mc,
                    key=f"exp_{item.key}", disabled=disabled,
                    help="Run the Monte Carlo first" if disabled else None)
                if checked and not disabled:
                    selected.append(item.key)

    if mc is None:
        st.info("Probabilistic slides unlock once a Monte Carlo run has "
                "finished on the previous tab.")

    st.divider()
    if not selected:
        st.warning("Nothing selected.")
        return

    st.write(f"**{len(selected)}** item(s) selected.")
    if st.button("Build PowerPoint", type="primary"):
        context = {
            "cfg": cfg,
            "res": res,
            "mc": mc,
            "level_waterfall": _level_waterfall,
            "wedge_steps": lambda: _wedge_steps(res, cfg),
        }
        with st.spinner("Rendering slides…"):
            data = RPT.build_deck(selected, context)
        st.session_state["deck"] = data
        st.success(f"Deck ready — {len(data) / 1024:,.0f} KB")

    if st.session_state.get("deck"):
        st.download_button(
            "Download wi_forecast.pptx", st.session_state["deck"],
            file_name=f"wi_forecast_{cfg.report_year}.pptx",
            mime="application/vnd.openxmlformats-officedocument.presentationml.presentation",
            type="primary")


def _wedge_steps(res: dict, cfg: ForecastConfig) -> pd.DataFrame:
    """The wedges waterfall, shared by the page and the export."""
    w = res["wedges"]
    yr = w[w.DATE.dt.year == cfg.report_year]
    avg = yr[list(C.EVENT_CLASSES) + ["Future Options"]].mean()
    rows = [{"step": c, "value": avg[c], "kind": "delta"} for c in C.EVENT_CLASSES]
    rows += [{"step": "Total agreed", "value": avg[list(C.EVENT_CLASSES)].sum(),
              "kind": "total"},
             {"step": "Future Options", "value": avg["Future Options"],
              "kind": "delta"},
             {"step": "RMT_OE", "value": yr["TOTAL_RMT_OE"].mean(), "kind": "total"}]
    return pd.DataFrame(rows)


# ------------------------------------------------------------------------ main

def landing() -> None:
    """Shown until a workbook is loaded — nothing is computed before then."""
    st.title("💧 Water-injection forecast")
    st.markdown(
        "Load the input workbook from the sidebar to generate the profiles.")

    st.subheader("Expected sheets")
    st.dataframe(pd.DataFrame([
        ("INJ_RATES", "Base well state: RMT_TARG, WELL_CAP, DECLINE, CPS, Manifold"),
        ("INJ_EVENTS", "Dated interventions: NWD, RWO, PIC, Rigless"),
        ("FACILITIES", "Dated facility capacity (CAP) and OE, per FAC_NAME"),
        ("MAPPING_SHEET", "Well to CPS / Manifold / Reservoir / Location"),
        ("SETTINGS", "Optional: per-reservoir decline table"),
    ], columns=["Sheet", "Contents"]), width="stretch", hide_index=True)

    st.caption("Rates are in mbd. The app reproduces the deterministic AWPB "
               "profiles and the facility-constraint cascade: agreed target → "
               "manifold capacity → CPS capacity → plant efficiency.")


def main() -> None:
    data, cfg, page = sidebar()
    if data is None:
        landing()
        return

    res = run_forecast(data, _cfg_key(cfg))

    st.caption(f"{cfg.start_date:%d %b %Y} – {cfg.end_date:%d %b %Y} · "
               f"reporting {cfg.report_year} · rates in mbd")

    tab_in, tab_out, tab_prob, tab_exp = st.tabs(
        ["📥  INPUTS", "📤  OUTPUTS", "🎲  PROBABILISTIC",
         "📑  EXPORT"])

    with tab_in:
        st.header("Inputs")
        st.caption("What the workbook contains, before any forecasting.")
        tab_inputs(res, cfg)

    with tab_out:
        st.header(page)

        unmapped = res["unmapped"]
        material = unmapped[unmapped.mean_agreed_mbd > 0]
        if len(material):
            st.warning(f"{len(material)} well(s) have no facility mapping and "
                       f"bypass the capacity cascade — "
                       f"{material.mean_agreed_mbd.sum():,.1f} mbd.")

        if page == "Total constrained":
            page_total(res, cfg)
        elif page == "Manifold profiles":
            page_level(res, cfg, "manifold")
        elif page == "CPS profiles":
            page_level(res, cfg, "cps")
        else:
            page_wedges(res, cfg)

        with st.expander("Download data"):
            for name in ["profile", "field", "manifold", "cps", "wedges", "spans"]:
                st.download_button(
                    f"{name}.csv", res[name].to_csv(index=False).encode(),
                    file_name=f"{name}.csv", mime="text/csv", key=f"dl_{name}")

    with tab_prob:
        st.header(f"Probabilistic forecast - {cfg.report_year}")
        tab_probabilistic(data, cfg, res)

    with tab_exp:
        st.header("Export to PowerPoint")
        tab_export(cfg, res)


main()
