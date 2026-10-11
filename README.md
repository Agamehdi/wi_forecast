# Water-injection forecast

Replaces `WI_profiles_gen_v7.2.py` plus the Spotfire workbook that sat downstream
of it, in one Streamlit app.

```bash
streamlit run app.py
```

## Layout

```
app.py                     Streamlit UI - four AWPB pages
wi_forecast/
  config.py                ForecastConfig: every user-facing knob
  io.py                    workbook loading + input preparation
  engine.py                daily well profiles (port of profile_gen)
  cascade.py               facility-constraint cascade (the Spotfire layer)
  charts.py                plotly builders
tests/reference_impl.py    original profile_gen/generate_cap_profile, verbatim
scripts/validate_port.py   proves engine.py == the original
docs/spotfire_logic.md     calculation spec extracted from the .dxp
docs/review_checklist.md   findings deferred until the build is done
```

## Pages

The app splits into two top-level tabs.

**Inputs** — what the workbook contains, before any forecasting:

| View | Shows |
|---|---|
| Event schedule | monthly activity histogram plus a milestone timeline - one marker per intervention, sized by the target it brings on, ribboned by event class or reservoir, with the horizon marked |
| Connectivity | expandable mind map, field → station → manifold → well; click a node to open or close it |
| Raw sheets | the prepared events, mapping and facility tables |

**Probabilistic** - Monte Carlo over the same chain:

| Input | Sampled |
|---|---|
| VRR multiplier | per well, per reservoir (default), or one draw for the whole field - selectable |
| Well capacity multiplier | one draw **per well** |
| Well decline | one draw **per well**, as a multiplier or an absolute value |
| Facility capacity multiplier | one draw **per manifold and per station** |
| Operating efficiency | one draw per case, driving North, South and plant together |
| Schedule slip | one draw **per event**, in days |

**How widely a draw is shared matters more than its width.** Independent draws
across 366 wells average out by the central limit theorem, so per-entity sampling
barely moves the field total however wide the range. With VRR as the only
uncertainty at +/-5% PERT, the AWP&B P10-P90 spread is 3.6 mbd drawn per well,
32.8 per reservoir and 32.4 field-wide. The VRR sharing mode is exposed as a
selector for exactly this reason; the other inputs are still per entity.

Distributions: Fixed, Uniform, Triangular, PERT, Normal (truncated), Lognormal -
each set by a low / mode / high triple. The profile view shades P10-P90 inside a
lighter min-max envelope, both taken down the case axis per day, and switches
between field, manifold and CPS level - at facility level you pick any subset and
the cases are summed before percentiles are taken. Those per-facility curves are
held as float32 and skipped above a 250 MB budget (about 1,600 cases at this
field size), with a warning when that happens. Results are histograms of the annual
average for the five Total-constrained headline numbers, with P10 / P50 / P90 and
the deterministic case marked.

**Outputs** — pick the page from the sidebar:

| Page | Shows |
|---|---|
| Total constrained | field constraint chain + deferment waterfall |
| Manifold profiles | trellis, one panel per manifold, constrained rate as a blue area vs red dashed capacity, each panel capped at the next ten above its own maximum |
| CPS profiles | same at station level |
| Wedges | agreed-target build-up by event class + Future Options gap |

Each output page puts the profile and its waterfall side by side, and the
manifold and CPS pages carry a constraint table underneath: how many days each
facility was capacity-constrained against the agreed target, the shortfall as an
annual average rate, and the same pair measured against RMT_OE.

**Export** - tick the charts and tables you want and download a 16:9 PowerPoint.


## Standalone Windows build

`python packaging/build_exe.py` produces `dist/WI_Forecast/`, which runs on a
Windows machine with no Python installed. Copy the folder, double-click
`WI_Forecast.exe`, and the browser opens on the app.

The build is deliberately split in two:

```
WI_Forecast.exe     Python runtime + third-party libraries, frozen
_internal/          PyInstaller's bundled libraries
app/                app.py, wi_forecast/, docs/  <- plain, editable .py files
UPDATING.txt
```

`packaging/launcher.py` never imports `wi_forecast` or `app`, so PyInstaller
freezes only the libraries. At launch the exe puts `app/` at the front of
`sys.path`, which means **the forecasting code is loaded from disk every time**.
Editing `app/wi_forecast/montecarlo.py` in Notepad and relaunching is enough to
change the maths - no rebuild, no Python.

The imports at the top of `launcher.py` look unused but are load-bearing: they
are what tells PyInstaller which libraries the external code will need. A new
third-party import in the app is the one change that does need a rebuild; add it
to `COLLECT_ALL` or `HIDDEN` in `packaging/build_exe.py` first.

`python packaging/build_exe.py --fast` reuses the previous analysis. A clean
build took 2 h 12 m on this machine; `--fast` takes about 7 minutes, so a
launcher tweak does not cost an afternoon. Use a clean build after changing
dependencies.

The launcher scans upward from port 8501 for a free port rather than dying when
one is taken. `app/launcher_settings.json` pins the port if you need a specific
one. Note for anyone editing that probe: a bind test on Windows must **not** set
`SO_REUSEADDR`, which permits binding a port another socket already holds and
makes a busy port look free.

This machine runs Microsoft Store Python, which PyInstaller does not officially
support. It was tested end to end anyway and builds and runs correctly, so no
second Python installation is needed.

## PowerPoint export

`wi_forecast/report.py` draws the slide images with **matplotlib**, not plotly.
Plotly needs kaleido to rasterise a figure and kaleido cannot start its bundled
Chromium in this environment - 0.2.1 fails to launch the subprocess and 1.4
requires plotly 6. Matplotlib is the better fit anyway: the export needs type
sized for a projected slide rather than a browser, and `report.FONTS` sets that
in one place (title 20pt, axes 15pt, ticks 13pt at 170 dpi).

Two details worth knowing:

- Every manifold goes on one slide and every station on another, never split.
  `report._grid` picks the column count that leaves the fewest empty cells,
  breaking ties toward readable landscape panels - 25 manifolds come out as a
  square 5 x 5 rather than 6 x 5 with an orphan on the last row. The figure is
  drawn at the width it lands on the slide, so a point of type in the figure is
  a point of type on the slide.
- Tables go in as native PowerPoint tables rather than pictures, so the text
  stays selectable and the numbers can be edited afterwards.

If you ever want the plotly figures themselves exported, upgrading to
`plotly>=6.1.1` with `kaleido>=1.4` would do it, assuming Chromium starts.

## The calculation chain

```
RMT_TARG  --/ OE -->  RMT_OE  --min(well cap)-->  AGREED_TARG
          --sum to manifold, min(CAP-OE)-->  TOTAL_IIC_TARGET
          --sum to CPS,      min(CAP-OE)-->  TOTAL_IIC_END
          --x plant OE-->                    AWP&B injection
```

Targets are grossed up by OE at well level and netted back down at plant level,
so the two cancel when nothing is constrained.

## Validation

`python scripts/validate_port.py` regenerates the profiles and diffs them against
the original implementation. It must print `PASS` — max absolute difference 0 on
every column, 176,129 profile rows and 20,313 facility rows. Re-run it after any
change to `engine.py` or `io.py`.

The Monte Carlo path is a separate numpy implementation of the same maths, so it
is checked against the deterministic one: with every distribution set to Fixed it
reproduces the deterministic 2027 headline numbers to 0.013 mbd (6e-6 relative).
The entire residual is one well on one day - `Ru-CB44`, whose event is dated
26 Jun 2027 **12:00**, so `pd.date_range` stops at 30 Dec 12:00 and the
deterministic engine never emits a row for 31 Dec. The Monte Carlo works in whole
days and keeps it.

### Keeping the two implementations aligned

With every distribution set to Fixed the probabilistic tab should land on the
deterministic case. Three things break that alignment, all of them real rather
than numerical:

- **Operating efficiency.** The Monte Carlo OE is one value replacing North,
  South and plant together. If the sidebar holds three different OEs the two
  tabs cannot agree; the tab warns when they differ, and its default mode is the
  sidebar plant OE.
- **A partly covered reporting year.** The horizon starts 2026-07-01, so 2026 is
  184 days, not 365. Both sides now clip to the horizon and the tab says so.
- **`Ru-CB44`.** Its event is dated 26 Jun 2027 12:00, so the deterministic
  `date_range` stops at 30 Dec 12:00 and never emits 31 Dec. Worth 4.6 mbd on
  that one day, 0.013 mbd on the annual mean, and nothing at all on AWP&B
  because the well is manifold-constrained anyway.

Sidebar multipliers and the event date shift are applied before the model is
built, so both tabs inherit them identically.

`python tests/test_app_pages.py` renders every page headlessly through
Streamlit's AppTest and fails on any exception. Run it after touching `app.py`:
a broken page only shows itself when you click to it, so this catches what a
casual look at the running app will not.

Three deliberate departures from the original, none of them touching the
validated engine:

- **Day binning.** Three `INJ_EVENTS` dates carry a 12:00 time component, which
  makes the daily range emit a parallel set of half-day timestamps. Spotfire
  collapsed these with `BinByDateTime(...,"Year.Month.DayOfMonth")`;
  `build_wide_profile` normalises `DATE` to do the same. Without it, daily means
  are understated by roughly a third.
- **VRR scope.** Spotfire's `${vrr1}` scaled Mishrif RMT targets only; the app's
  VRR multiplier applies to every reservoir, by request.
- **Whitespace in facility names.** `FACILITIES` contains `CPS4 _SM`, which fails
  to join to `MAPPING_SHEET` for five wells. Both sides are normalised.

## Notes on the data

- 2027 carries four planned turnarounds recorded as zero-capacity facility rows:
  a field-wide shutdown 2-6 Feb (CPS2/CPS3 return on the 8th), CPS5 2-6 May,
  CPS4 2-6 Aug, CPS6 2-6 Oct.
- `PWRI2` and its manifolds sit at zero capacity for the entire horizon.
- `OE` is 1 throughout the `FACILITIES` sheet, so `CAP-OE == CAP`.
- Three wells have no facility record and bypass the cascade; all three carry
  zero capacity or no base row, so they are currently immaterial. The app warns
  if any unmapped well ever becomes material.
