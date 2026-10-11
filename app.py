"""GitHub-friendly single-file WI Forecast app.

All original wi_forecast modules are embedded below, unchanged.
Upload this file plus requirements.txt to the ROOT of your GitHub repository.
"""
from __future__ import annotations
import base64 as _base64
import zlib as _zlib
import sys as _sys
import types as _types

# Restore the original Python package in memory, without any folders.
_PACKAGE = _types.ModuleType("wi_forecast")
_PACKAGE.__package__ = "wi_forecast"
_PACKAGE.__path__ = []
_sys.modules["wi_forecast"] = _PACKAGE

def _load_module(_name, _encoded):
    _fullname = "wi_forecast." + _name
    _mod = _types.ModuleType(_fullname)
    _mod.__package__ = "wi_forecast"
    _mod.__file__ = "<embedded wi_forecast/" + _name + ".py>"
    _sys.modules[_fullname] = _mod
    setattr(_PACKAGE, _name, _mod)
    _source = _zlib.decompress(_base64.b85decode(_encoded)).decode("utf-8")
    exec(compile(_source, _mod.__file__, "exec"), _mod.__dict__)

_load_module('config',
    'c-pO1ZExE)5dLn!|KXqvnA2IBlVR<k!o#}6Eexz~;26z^VIXMfWO1QMf}|X1MgRMbl;k8sTNKUwMV5Gc?zy+;k|bF-3JR?%v1=^%LMy1W1z#iFagR0?>TfKD?^tl>v+-y=S{%@}z7}d1Z5xLc3QkZpS388t>U})8_7?eG3J*?{xaAh4IG}?XEl$DdU^E_~+6jf=JZ~LvFpVXMMs<F51(Q2%Z?{_CPJ6DWL?TI&@hCcCtZF>nVGP9HXzPJ1rF{&?1-8+u<enFjJ4fz&v*V{JR03rgZ2Kd_Rmq8r0~0@wN537d$D{aw*L_AVBBy*j0{Wdmnx;@|EB+z!>9_wnILe9jj9g<*OtOvGBYoN%m_K@*B<Hj9=jrT4Iy*~FyQ`?mue|soJv&c-iWeUSp$&$fpc-RUi9(<%TKI+-PGH0B4n3ul3cItKYEVLBVB3cJI|T0G4y6Q%2b3^bzumBR3t}4nY+kM3z>lEubU>rhfI{yHWXp?NDD|BR5Jqz42aH!YSHBa&a(TfPt4ny+oic*SIvho1uIW98N@}`2hgtT^^FHgk`Rv(%^WU?9-TU<#_KozyNI_G<O?Z~zb%+Lhmx&CnjrNtW_`QSgJ{+t)`v_Xe7F@w4mIK&Z;c6?YmvLZ##;Aj%Oco)HfME{7QV#7w3)_cAaO|GKJ<+pl_PD|&7BWoUliTzJu1GA7JdVJc_*t5KnlQ|E8GK0kh?1PrHv9Qw28+G%Es-M)>C~XZyIfrSv0N=^;AOK{_lhz|K?YaaG?M!Jf!ZuKo8{`wHMkm)TB=4hz!5rg)HBr0jt%UDgN<#l&szVL9XaPvio*Ztyq$I_{EKKtp_r6daY`_&c;U5e=fSY=&rf;EfhbG5{hCXMkKKJ$p$cwzA$$u@EmRmYMrfaR8>}cSL89G$+43PlYD7f?p8gM=v<OfzNHxukP=#ztd`W}f?;KKhS|lzg0M)Rx+L#~)7<N?b1ly==P(i+>fnt#$>rr#?jgi=uHp{Y5*h#XwxlE>ztZ&|h$JO#8zKNYg=aQrP+|*iPT835SYEk)z6W)zubQP8h!sLeo61J1VK<HIFs82^H*szGg0$@&|MnQR;TZ>^Og}9%X+YX4e$nD@NsQ=)Nnwn&mQ4%K(Wi<t<i?~E{T0`~}(qFs!_nWRmq{XWsm}i5af~bx+VLpds6%G<WYW>b~kk|3(U&%#$y#')
_load_module('io',
    'c-oCuTW{Mo6n+no|G+6PQtGH{S71N}4RbTM^N<8VY_t!CK`;_!bCpGnq~ds8|NG7%scSBsk&8qge&@>X90x)0S*kC0Qhp(YWSJ;8gq0Z)WmOweDPA$fjF4p<1i|r9uH=qTn%AaQoKhlol~e{!l+su+eSGAlGG<s>Fs-?6#M&hk@@o}nW17HEm9=N%RF=8eH0M4@#Z#uug<VCd#UHcTazPRj1|Oyu^UL{iK3fD663nmvq_@*$_cHr5yI$J2tLe?n{Q4ucXM+e~j*oup*<}BbIeM<okB<m^!08(s1MWkjCxri9i+fh^(hwubPG&UA$!n6c)IIE~4L*pHm@OywKgVy0PL-&P3!ww%_i$dHgVXWvV8I8)cAVJH3AtmM6D9YWymE5(WkO_Wmr2DH+4G_}vzrbNw2ML*!5?9sVA#QYFL59#tKbnu-O(MZDoFbiwwzcs<m^{+akBu=u2?B@S!D2dDN~zoc)aDBt9vPwgVWp?fE(NKFS$nh6Za3X!HqN3oFy4g3jsTZ-4)#BCgV9#oMm+HD>ST_*;1+KU7hD#MQB+jQnS)VO$O@LK7S7dXoQW~L&}Q}qTpi)9|EB@R(?WOn&eUujp_46CUSU%`o^V)BGy~Z4J|>5Uc1vE-~qf={3s?Mi=S9g^O;gog?Z4pL4<BKDy$}~E(;s#=$w4@d*57*+U%lF8qE6&VFeqYAT<Z!v8~@)gM!6uxrAz81dq+`S?PdRo%9-%Pzz6+M24-xPAu|)Qyhq(^e|o4#t4e-hvi^X*I(%F+Y&BKqsK*sY#AniY@rsQ^x+EpLWIF6vaa}E|LzN@VnVr_hJbJp6UfCr&XlZ57H;J}30P48A+QIblQ+?$ov1kpEL7CH663xKT17}DURSVQoui!IvWl<Xtk*rAS-ygw-m!HI40fm>ZAL{g{D}*>=PHcI4+#lWC)a?iIyJ6{jihD0<4UCAU>7I}D@-RrD!EE|FiZ{@=v|CrRAZ<pGyV|bVzN{<kGjM;!snq&==pQEYeLc-2xG|0Hm76uyycaWS)FoAhL5@mv2_1=PC+V%>#6C6mlQcOt_}p<)8wajXYby285QMU5RRsBJHB5-x~fAMHT+tRq<kY7iUBG1#Cok{C<c_?6B{;?PSVMqkoPTrLnsN96w!w5D!Am#*f4CR690hnu&hknx&<i(Pi(d!ys_P-NZwu3K&RmE3V#FZ5xuyaF3?^9oDt$VULu8N)OH8zTX6I!JUwl$wosE1J0A8nqn1!CvPDEWs<$G?$3ve@hN%6wSEyqN;2AFr3-Mg?EMgl<=&jB=7zd!;gewTr1aYAN#ioSnbEVu=u|G443_v_yjG@{JxDvtp>0%c2&psEG-exp15ANi~3QVw4R;%Fi?DCRcPp@W37EP-R)@$tH$za#APQh~%3_#&;tYP$__t-#mcy~xfsAEfjYOa=aIlcYZcpPt(tgE|2*gF{Y#o`=;5RSr4VH_w9)J<Si-UGLY3`}U;vv+^uFGIY6rZsE}?ZxVaviH^mepundI%`H13Zn|$)rApNA%OXTDBr|C_S+ZYUQBN~CGO?)C78xUPmhkVLN|~l*2`{~O5kzQOh^fO-zo1tO`l6%2#Rlv|1Y==;0tYXia_nu^tzeq4)FNt_Lh7p<(-bn6vzijsFY{2(w=|pw3Rami1zMi39Zzx5mlEE8&BKX5*F~)MwG1ZgDl|>EH%ZUBjwf;?0nEOY<j(Motwif*S!gWHjdzTk7f}&JkDJ>G4_)VGY_2*g@a8a8ViFxaIeGYe3+qDc?`1NMQp*L8Z_q!vJT&W3@*2gwJT>ZxdrMEdDh`4?tBk<ZM!ecYA8M+0!ViMK6Y5$#dmZ9*e}rq6bVeQ;sI(j3{WM7DsAVoX0GR1!+!li1a`u4Qab*dU0lwu-Mw`X@qWu;Ch#wi5ga8ZBk5lM!}`-Hd_!`@qxeo59PGg>W3vZ$O&v%(^2CF(xL4}MJO3ot4OUK{!09EjUz*=lG>FD<;q)1#fg=0@^<5gXz&6bdmyK6Wp933_8Js&l`VZ7I<G2')
_load_module('engine',
    'c-pO5|8LYf692tY{|8^5^hjWv!kzA&w8uWF(1OsF7SVFmX|+n-#M$+0)()}Lb`SBt-;5n6PO@FN2Nj}eJRXnd>t`lG5F9hjsx=o}X`YgMRul(iC39XdvSfl)RC6if{k{FYBa&0DS9x8KQdXMCoLo1g36NfsLvr10VM$8Mq*=Tsc_r8Tdspw=8-?`A-9O^L#^oj^uh@#-aamV{E0VE--xwanhLjakth!^_gm94-b;iY#=oQ=F`&{$tR*?e4W*ID!Os49vVt1U~C+Ui%x40CqGjf0%ti-_njut$lxQ8w&7fM@p70X%0L<)pf#5h%V<c8(4VuXqfUKR+~gu>tHii#!6Kq)~G?C;_2NRs5Wt}B)#gs;tER0ye!_7rNbc`NF5xgk^$QMT_&Dl&Kj|H=$W4Z}E<BIirT?F|T$Ql(#;w~mHOxBgC)wKfNR_;~*2-RVj4`uz0M`?Cu&BlF<u<n%N-J9>W-Oh|BibZLHne1Dl-9({a^&xYXj(Fc4!`S;1$W%By;=;8wZJe8@rMX*5b`+FJ7No!_j(2$$+r;QvFlIF|lK<J1Z{0=vakEy0_D!OLV{XGIdpu}U!!P@A2PXCI4>W$^@R}y@2B`f}4DJDb;Mk;wvN>-T-hiJ`1cE^M!X+f2WjZu(smc!+(V6h=ku>xHs-~%;?yiF~OsM!ik73>Ca@iD2;;-S*C(lfYPY@QNanh+*3^A3JDZ}N(Lo(0E2g!)2uH&ij;mf-JBXIVb62Q`OU8IjIB^$GnGTE4Q@R!DFbuu?e30~X|2!wRBiDZmB^7a4n)T~>9s^%wHCl1dpBS8OdcBXFlB)1)qq?qz9$9|Df$IZru6$7X`$0`$yFLN%C%YRAo(3JsW2LCV!e@st)|R84PL+)6t)UUv?P2DwEU->)F-Lc83ObRI`$GZLJE%~ru=K-7Bg0`d+jM<7`u**6Ily!HqqPq?GEA5Tt>9r?_>Y(@6NWU+`LXNL5FtJ#ZIrxk+~AV^X%V`!?A4Wm_ZBWnooY7+uGu(&m5)J4<CEvCINX`IBpWSXzpJ2dEyfI4}=q(T@?SH>z&6nS-YabhBermf*2mlrOyAhOWXEY<uDbDpSa0ofRAEtnTmbfc{4sEvt&iO@Q6qewUcDdr2O6?7()VM3Ob1n0tJoyX?+W)pfr7)?9V8I_>4GrMbU|L-Ly>mGP7%uQ}5&)dy0TbFv{am61974Yhsb#Lu4?IvExbpCwNTURkHO9;QvS9kcO&)K`m)ZTcoZc@zDnsd0;y6F_p^WAo`?G$vvhO%=?@|1+(3#fSJ{qf1`(|2c>)5ud;FqS(cfBWt4Q8Z-fYjxVFbV$=iWpiv7r5@$i$V)J1ucpS!z`vGUfH%=XNeGgH-hgtT1bfF4Ey)u+_X)w2FoE2{!FQozQ^!uo16e{%PH7F<6f#`3vHo0CjAk34jmdE(!A{vf&AALf0_1wE3?&o>B4LXy_m*KQ*EitY8RToQCi>-Lk&AMen?Ui=ko3r!YJg2D?!|qVhtXpmOTJCa+Z2y3C8RJJU>Nm$3L<G!Urg3F>z5GxP<+;<3;y;+7yMV4qisdJ=GPe4)TU;oWvQ%9z#AOA!9N9i&~{7g>~{n&?@3m1*m%oWsYq1|f%SkEQY;nE81j|Xt<fu-f{YYu(ndSj8cM;(tMevvNT{d)iHOCUa3R<Z054?*)ty}($L$T;OoFMVQICyFzUY$5A80b0g*eo_7ZZZX$k9iBIuQ?g#OjZJ(lAavPA?!=KrojAi*4(0zu?;$#yW^$VQ~foX=6M9yqcQmG?m07cZMH%&5lyB!&wjz&wc8}_Id$MhnQPna2x1OIG_?_N@{pn3>?N<9?<|;y(<(Jn*3lDa0c651^&`jff)M*Z6hwsAQ!l>a}3Lh%L+0uPxV~s3gG0;A5ihI)_?ixM0Miw&c7aYtX+QEr)mSf19*P)L%es^i?(ewl01S*ZNfL6WdUh>Ko5=jOu^;xRvzyN9s2p;a=t@j(zG@=rz*%G8wnRehiFj5@Yc`=g2=-<1!u!8AQ=c64%Q;V3dO9UVt}Ke-<v!i+@XOd?u54DjSujO;gG*u8nbTz@oZR;$LzbcF@LYm8Xf?i;<$UDcf`G08*^{h0G@t2``6j|)!ER}mbxy{Yr-!+egNxW=hG-)>hw7oyTEp&Vih#$fdjbH*J$VlTVbQ`dIOQMxdeJ=UjtiEFYblW!t?$f$T;7F(!K|&`Do3PavRlH8;>2=svKY%D1tqd;eom5Q=^_}+r~aH8<(hUd-}E*P<Q~XsWPB8ufXhRT}EBWu=woq8cYTM*GS;VK^RkkP#E$b1b-4r8o)U_e=<D{Bx$?+3=jZR7FVQPZ;Ff1|Kz+<+F%-sbJ|Mf6`3rb!@oz%%Y5s|U;(JF+=Nk|+dRN?ZJ*n|vK!(|$GB)W6mmjV9LV}}1w+wq`<qSUdTOd^TYtV$Q*q;_!X2>DNg3CIf38_LENx-~f&n$4t5NlUwU;10z<YfB9WJq>bo5u&RNVsO&@|nhm<Cbdr6Tfcv)I=du8YkeSAa>ArXG2^4m+)HJK!6>YJNb5u{DhV3n$oEDN=g^ZEZkX1^j9U3=R>#^f%&kAsXj5gci7WFs4H<vp%{jxZ9~+PE%fRy>USDr%dl0Q_OJis5cXIwR>7+2XIDV+AN4<+kD^vR%uo?vs7<r2W+~jUBi<DfgfY=y49M&Lt2^u!O2MIE$$rV4aa!jH^M{i^We?V>&BtLH34QOSzQ)9#dE?aUNfiz-cYMwje1jnuMq^lyq^VTCexj^0<12p&G<lXe%p*|&y5uQ!RCnEsiNUK51J8N|L>>W-v)~fWoe!OWedDYDvNq8)a(oHo*ID;;Hj(rMiH6Syj6-tx(y#3=FYYW+vucVxpr8_vYOA`t(&tJcnQ1K<-L|+w1qy-(Hp~lr`2-bq34!E7f==&C}^F2bO3&Vj(CX8fy|rHhTn!w+G)5-S1hXwM({&N+pB+4Om*!yusM+Vfi0gE5>vZ6_^<<@ket|=vk3%f!y8{8!Fu!E<Cc}$w8D8omuOhvu`(kS=<_o>c`<FjFR10HRyY;x#`$GI#jxG~fpPuMnK}OSZu4g}kv@&FQrqloDL}is%fTmvUgZ*rv-GSv=H;xnVN~hxte2K{y0v`%;=06=+RtoVk2oZ?a@%vCZ5fRGHf)^yk?fzv_kRXkUjWp<1ZpGdR;Fji*fT)iy}MVyL36)5jK0x0v^&~&TX%Gp45pr0M{R(Mlm@e)LZ_pFRj+cnbUz5h!RJD&p^4SR<a=ONPcwsWk=|{-pO^V&EO}+J_6H-?dn$M?i_Bz<!MC&ShNy(L-e`&lwaG_o@HI$}!v<jIQN3@cgFqdj20tZ5zJQ4OZ0$smOv&uYFshXHqgN}K`;6tkim?O=8U~*PUW{cyG(?Sq)Z1Fs!_v{C`R{-9f>s9')
_load_module('cascade',
    'c-p-h{cqdG_4fez9}X-~ldZ%!S+QYi9YC?=&YSI|w!5Iv1m;8@CC(Jd@<=Oc=Kbw^@7*1Fq(0&lScSx*j`!ZZ?~l849Os;eNt#rfVVGyKDtVGsEaWoekzhksEd~5a!#d?v0u$J6kymk23RZ|R&dZf#QNBh%!B_tCXV0JA79t$MU?^WmJvT`6MH2d}$Y*zmZwZUAMB;1)pS4I+HvaKuGC2$G#y3AQHhj&PtXHhc*@|aLoTt%%g=tbSUNs}^bo_4kb^-|8ySI1a%i!YTl;9_Ko<h9+u@IlWyB(-OgBV6yob<5}Pp;1nV*SX9l!NG6;JqJr{Qlh=c9H#CgeX%$>p0HyXK|UYSP;Z@RfEU^maK}rtQgO-yi&qPf$7n#UKJb0CCiFttl(J$Bk-??a4I46L9KDJFxbxXQh;`=QyRrtlYdUG?}F3I@$K#8mYp!yc{9G9I0NQfzdysToA+<=>)pjE{Yn<8kkSFFuO{Q$pKmnK&D9+VpXR{xTSD=Ea(NkmO!3*$FhW0nM#4qtPfD<kk~Tm)BW5A&zeU`mc9qU+v*7sj;_erm)l$%zcl+}jp#6M&ItdhAIM=2SravN)&!0siW<ds~?#dBJ*1r{HBBX~}Z+?w5^46U|Z&7Qi8D9wrj#QQ#hEBF&>t#|2S@2LWSNIE`9fA3M$Aa6dBhM#$K!l|LW5}5FL1mjlxB%<<@W(F&m|G~^()pMC7NraSOR*3iPwvWEcrE2&%B4)=O%N->fLIqEgNP^ThWI(-6+bV5K*Lfq&~kNK04R$MZ)Lug3<5>Yt_+7S$bDY0cS#}ABoizZ4<ePmaq=c^lyzzllk;&YKo}xp=Sdd1PT&ltpqAizd^MSQ>@_=P7=$u*WR^PWxgi0kBCgyPaPZ0lyE^)5e58R5S$$w2QIP15n8>1rU-gjJ6<}$k1+G+VT(5aIb<BFs4CW~t>5Y4a|0S0}En!-30%;R`w1Su@k$sInk-@Kg&vaSwvXbkhTDs0pW5=fG65RQc$jJ&HBvT4ktqdk&1PG?myrgB&yS04Klt3DeXCuXdohWw_ho(Y|;LqvtY-^g=v2A$STI;+{(kNIbkqC-1kCRlm`nzkY18}XPNU}w5cwdBO%e+i}%d-)y>LL|W0J=-SB`dxv2F(67WB*~-IoR(BeeFefz*#iK!QIXH`gX(+88{3kOiFbxB3=OlI2`6_y~^kfcnc<8^j63vE5RjXfyR42X!<`;vXYp;Ff*6p*BZzc5sP(PXKV1He613#$QI~{VwF@<`7EXcg^_1!$s@@ie=|js%$so<iP&5qW?D>>z{vVoRPu$yafMFv%;r42XK0xW;>D1C(Bpn6A3iW1Ry9vk2!W8QBztxI>d(XDm++641Y~)=SSoz>f^z|EnCX9k={_4j2v{HV&p4JR;JUnI8v%c+C1mmhn95+CB~N38FU$b~_*o<m5QsSnI0JA@WtdCnq9pE>P%%>??v!spGgX;Dm6KF{FFF)pA`N?1WGJSNl~c)a`a{}{wuTd#WNs%Rd*F|hkDEa96&tfytl7o&-vgR@OR6&2g|nBhM#smj0)qywA?s(L%>m|{a0y;>FGy>QBAUTi@@yfHnW%<*#G#TXK~ExOQdBIDNshw^vQ}l>MEY$+2P;l_A%!&P06zwGw1PKD_GSY<BGAEH-}eX3FQ6v>3L@SToM-bkrboy79%@FSOoB53Meta*2*E6&Y|KdIRb$$QEztJ^PZMRbe1V~~qG@13FpmQxVVM+0g&_B{@!iCzMm_sc<zoZ~JiiII5qA<db_lCLDMn$zN?_y;1I!+PO;2s#l95c^cE#5x3c_PwGi&&V6U5-nY%Nn=90KP{Ot95DS3V5-XvC!A1<=OH2$;*k1Er2PDdZcT8GOpCOEFCO91w$`(5|rVMQr3d^Snk!+IZv(SSKqrDESx3LvAFvDD%1y$gx}a^kcqpr>fYZAP;6soWXa;#3Am@r6?anqzaX3n#jsEl_c`N6={7S#NAbU`!%Q;;*Hx`V!*&7(*W$D7AMF4vB_kbWM9Qx%*4~!`4pz|(f_2w?W2Qn)C6DbIIzm;Luwi^NdXe`vILW_0tmk1V{1I5o&exzISq(QXv`f~w`|Iy0;d`AjJiSqyjY%WG0~j`28<KYasd@mJ=&Hf4o_hkdIZR<w@$-_4@noy)P-lSmBO^0fbjhxAN7%O7j<C-gA7*C)}#ZQPt_3kP#CYI>se$HN}7)gpgqvYHtVy!(zWT;J%C;AH-zu)4;t6hbxXi2FutW-S0jR^GO=p#JyV}l((J1<RzR=@nD!hG%e8K~=iCT%x;!cI$7LQ;Kk3Y7oy0{b{iw`~Ac86>2{Em>7H%`Itq4`kYX;i)&Dxzw?Wkv>l1U;XX6i%q6u>rv_y|QL{GA%GS%V(uUX8CW&fi|1(Gm?w-xAQbT^c%iL&^IqQ7(kL!Yb^fBfMq4K5?*_a4h}R8A@6}VG4nBx9+e>P#w>cd#d+{3=&ul@w#agm)O$h5cQ!mq)tnOc^RpVm<{A*iP^ivIti%4S`cGTQ<B_gSj(MY+ICxt{4@`z)=%mY*vU!PM7HYlRU)PFivKF#=*nG{E3~H9m9dMk`|`pL^X%dsFtovppPX~(&UQrp15WB=VYe$=bOJQC<0lSI4fvuIpxM<ta&|#UC<Rq60Z-@y3>cRo#6$2wO{?wns2w*FpxVgVHyEI9`}+vcSYhHV`KC3GE0C>%CJ@NUso)P-|EN*Wf0fta60$H=lO3~xQbk#gZ5>)UO&15Vq2j3^G<(z$u97TSL2T`=s(#swEqLK}nJ}}S!q-LYPSq|O6+>pR;{j`ihh|ZD%ESVK)q|jlT`~z3R&|)AL@JIT-wZl$I?Lfp9BbCHI4tWd&|9Ei<m@}z&oG8~-raN~$wWz5O`$&?bP&v1F^!7?8W=3in%DqfxW|G4g|-@LAJu0!Bm+qeWsF#;pCtNPK>?Bg*@c3wrT#NPVY?WcT5Y^l;pq)Nr9Q|iTX5if=yI;EpiVxuXhuEne>C-4SjeYROrie|B34H)#4@6<fJXN26Eq*Q;>bJ^;G<_Xc0>5I>Lxa6><d4Q#uXkAAmzL^9DgnX8)<z$5|f;%gjcnjH&fMmw;cAiC^C;G5i9GYbUfWlOD8wm2u(g{4**o%K@qq=X-Cp{g7%tEi_Tck7BN730NwfI^zP#Ab#P-k&HoEIJ%V;oqo0Nf{qR)hh~P(FD7rA7Z?pAfRO}#UFMs<<R9pIgG>Q5kVb=FV47R`92`x|Liv=EXgy8w$9ID3*u|csN2Wr+`X8hO$L)&Y%TzRLv`mnGI|Gj>5+G2#i+68sE)h^gWyXAQ>+opDMeP)?>@1<d7prEYaH?y(9z|iW*hNhN5-M2=th2qO?z#?zIaW*7rlYA;QHuimX6(@oYOjH*C9Tuj0XhH+g9hGP-LaA(5&HQ;|8?e4g4@GlYe(K;^W*hBDH2O{7JiftV$S0<QT=cr>PY(80kQ`MH?HE&sk@f`G0Zw56{=ze@0>9{6AJu*JyFIn@0nOx<G}Yi*M2npr`+?qWf}3qawL3>=8pFC^xCKo+r~|b(hs7PVmZD-u=XB`H-WGJud&I!F+S*O;AK_ldsM+qZH!t>XdOX_aSe+t3+ljIY+S<`gj%OQ(vEZF{VB?0rTV>P3h}{!q_XGBTq|q{ZbLX*hjMm|vY)GA>b*cD_rw?gk2;st68)LhhK%P$#D$UoTJUKpa5C#85xdJ5yYhH;m=4tAZrS*G(9R>b@kc8W;BRo0no-!S<B*i?w$Nd6!CgK=>K+0^MF;AK2cN9}5ah!yS$ifYdp^LWG6vf6xachwFeW6<<V(2hbc`yC-(MWJ#oMu6#jo+rzU!fNRswnR3sndh2cDXa}b8UN)ghADTu+zxaRIxRc;!T%|buou&YWl%IWNX2lwwnCp$VwFUy#wZu%fOJ51q|GSYv2^xs&pO)yTBVY+8DHyhTEtjkyd;UDq{pTCMCR~#`r`;#)A5Y@CFbed?KE{^>tW86)1F1<qr(^YwMy+AKPAm&+PjT=2jE#+2Bc&bfdWM#1L+AuX@C&Bc~WSqUsD=^x46C5&8`5AMY+8I9rP`wHO%PEkvb@*o8HII3Bzl9DCl2KOOtu4b%-0Fw$<cUywO>Hf9%7C!mcF6&e>)P4A5Tz>Yn0HzZDTURe;PQfan8x^Tc}^PBcVIstvrWD5G;RashhIJRVb;u?wvEaj_t#2JW3sx$(n4+_AubRO}IQ~)+4mCN=t{;&v2h{wnqPDB=WFR<btT~{jk(Aa>z^bD$<iLA{6-A%uiv>p3>t)1~Kt9cr5I+zwaY^(|W14@KD?5ls3NF8$Pqgp(Q6RL#hA9)Y4KBp+JkFq7>V3NPqd1Y_^$$G9LC0N&?z^<<x)$^@lK^^C)QouylEkCP*iqF$s61W!|?O~zqZ+o((ZB%CN0Z;rJh#-$EkukyPpj+=XKph~}^*J^NeM{wbYq}*+!6LGfx-iqHpv|3&yLGO%8!`C<+#FJTErr^N=b3~Of<;LTbpjr&(nSm`Uq%N0o6bqJj_?(SW~*v;9qARFDgY@p?f*Z(3j7}UnAcT%zk;=wuhc|5&%@(@0ZV-0vjPjKW=d1NeBUR<loNOyTyCl*?k6KE2*ZiGApw77EtQ1SbqIZQ1jc_aqK2HjG^g+22|3+9Nc7zTWT@$wS{b&IT?%E+`u<Czz?z9n7Ny{k(hCua0RpQzoK}FF<PjZFCzZJ@1)6{otV%a@=Yf}Kg6akW#8>5;O#3D+-M`EcZAaZKK-Z_X`=c8**95XUOF-Ewq8N_!p#X7!A^Onv2P%K6Jz&-=NV{jHrq0?%Yf3GJtLrI;acXuUKTu!`b&_y99K2>P#qh5?GfQN0Q3Gm2_OJu-3VX}NlTaJD2F%c{l9Su+fIv(+yh%x^%CJfXiHW1(eMgdMKMkJ^T+8`EK*M~q6f*RLr8Gz@1Ov0h)vk`5S|&=5hGY^V4R=|A@fX^@`=Cbj7L*#=0nia^3)LGos)p3y^?^I9wIf}S?$IJnos!yn3&B8_c{4)`vSqK=Np|x6bQ?(vxT^rzs}{6Mb;$*0{SVF^zfS')
_load_module('charts',
    'c-qZe>u%dfmj2&Bze9mR?@%3CEjhLmYoh>mV$Woe#DU|U#zGL(lvuL3rbsPG+0uCYT=RdPY`=4=ig!v%I=egRwnUM2uXFj%rD$2!XFp8*jhL)F-<44;W?>|fxy1J>5@)}CJ{L>pR>mF6vVQzw7KIBj9?w?EDw5-|@D|H3N`w;xVd5lS7{ovR@Z%5q?!rmtxu3ymvD^qJ7Qr&Tw{!v*ckutx&2I9DI=7LtoR7oFf5~aWMQ%eq09_znP3S5XX@7TeY;ID=&%{+A(T6XSL<(mbg>fw8y^J<IClQCj5wVOs8H+n9muLyCO+%li&gCBFGLoGie|UTK;p+N}7>LIoe-QX*-CW(AeHdSVycu6zSbbqVJ3fDPd3kEJ3(vp&dj93t>&vsZ7vr-(Ute6j<Dw_Mckj;5N=4tle>=W8yZ-aV4VSq*Ie*tXsVQ^uNi}lWeRY0*lop_k8o&Sa9~W<L-d}y<5-$%=4lm!OCElKWKG0*mJUTf!I?F$4xQz<qx1Yb%Jv~4BQakZaztv9i`nRjPd3}EWwr)1p-mNd=xNaJkOnTyK$<)Rr-ks8aRN{$t{lnS$#fNQsg)5Ob(XC8`eRUyji7ccmR?F5t+jn*wNtCu9r0;`Pf;fpBFOY6)>xO=G0&f=jZoWqI?qbbr3s!d-cmC~McmXj97Nlmkv!0!$Gxd^9!v=Goxgt-BgU&?n@IbS~)Jf!R7<p627m>4AvaDFj=wM;`_=SH`Q<F$KcW(F)#Kb;lHy3}tx_<xm>;v{?sQXVzCr2)HdHnL#={a8-YRQoSUA}tv;__8Gjc2DPC%yBxy25Gqg(}tUzB+kztnO;+qRY$E)3-19@~r#rwAZ6%Ml{tQe{khYjD2Slt`d9Z-S#1HI+xxp$gM3BFY#qxU`N_w<E*`yuQ3_x8jI2vi%Ggm=HFa;xAUZr%}G%1=(yVw2XC@A`+E46bwh27m}HML3GXF~UtiwJz-^0%xi_7cACiO<4pz8B<ECbAa5o8;kb%*y7l=8;WfF?1FP%tC!erhS_>j?q7poR{J|yaV&xQ1R@RGT3R8w>8@ZZ89!6vIgbkdQk3#?6NwRACWvs&52x!r;5O%pqj>tw*c+hRTF;=>81XnbJ#a+Y8VHiK^G^d+sQzK;o%7g7J4VLYnU*!!Ct^iEo>TtVKDvFe(ybI;bfXP?4A<{r(loY5k5<-l5t6)4z~g-ujzsk-$CJ<K5D&t!0V(iRh3=Ley-d!W8@_thGzR<N=%P>OP3&8^(ju}4X`;6>?mx`%4TYL}w27QJ*WTIws35Rn0GQ%2XzD4cmdHVpD4w%u7D3b*slNt{bCGB!wQ!M^alI2nSnM+K6v8wm9FT)KUctd_nUGGlZ)oe@agZq-&m|9(@2Cf0c8c)%tRNKNp_JL0VtQATfr3-nO_UHq=P_}x4s3GW1oQS#J_F4Mkjy=WxLzz*P6vliJLycs_N#-YbpyyEmAsS__)$?UF{mjj`2Lk9z~ajz4}rSD9oZL!dW5VBhBOb)hkJ;q}iHCoVPQZvg65Dz-8JBEfpdzj4^2<Jpbc5!Iyfjb*o?;w7y5z!WYp+Q^**!6+ZlxB2o>Z`nUiamJk%dAN^6&=!aqk)<<B$nqU^TA;Q^(w*{SoCR`m8DhXJrvT1fU@EcV#z9xh1P(C#NT8TZn&;lCazWDZc{@IjutA2{nZrwXRDF6cD2wd@>5PVXy$0;^hUn@xm=G`A6jEL{&Md0#mo;K(goel;W1M@9%@>e<91f9<Kv09w5?}`D9{Lcoe;Bl)Wgv0d*Zn`#8yHWGWB}2j5g#Gq{mTd>@zF6ojCSm^wfU5#oq*fJgBFZr6zH9eQ`EE|M2St>9l8umnWBiJGuEq;VN*)tL3=YweKB&CG~W89(<K??I&m*87Cr<V7^3PY)W<g&J}+b2O4by{YzgsYp`lUQZr*x><n=mSr8pBo_T?nNY!nNn&T_+8Y`J&MLpGCx6>`mog0}-&sPlqqfn8S_*oY<Q%oWtI<HPR-pP&L$gdHTTLt7+X;^9~08zv#j=&)1SYCIGF-<}+&p=!{px#oYD0~<f5y;_-uIiSFEHVHl-S{RM{AJ+)=`L1&;$f&5NXSMNZ5_a#$YDPSHH;2RW&|(@QaaOlic&7{L(Cw*eUjjiJIdk$N>o&!3^LW9Y1YH-1f#}wI<7MTY6$==RC@`P_X*0=pr8QE()=#`aC#RL)LEbudII=iE^)mGP#IEZv2-FY4udkfA;}nHU1FG&(gigPvHhct8->fjv0EJgh5uebZL|uM%C)M*SWq*%ecDa5zi`%e55Un2Y`)b7Qotp((=v?**hN*=kZ@K8>&^AjhLvI~7{NJhKrIcpJ(lyh=1#K$x{iWM@qkFu4wPgGXd}7TQLX~OQ$nV|I3|r8+zx0e;3#0DZs!$-M>AA2I1rd=uYlPylv%EST&T~hRjQv&nZ%w_W=w0rY9R?M=q2hGrqA=n3c21rw3<!z^!nwNfS%8Wdeg;Vz-^B@L=0mVAF-{}X|5VWhg#rZz=MGf=%8O!i&gwkf&g^@pa3)MjIDD@tw{m1uFE5ncH!49l+tRIm24i0R6A`1CmBe=y5vy`{hW>(07M13U|(Bp4YOg(ua<*pL)Ca5K4>^@d$hR#@Y@j1en_X+Ic~%{O_*m-#PjXQXD<XqjP~NV^)>CW&6LOmC?vtM{q(r$w>!Pr(`(4&$a!M{la%)cx2)H{=;t-f)=e7hI=~;Q_LyyH$>~R4*nK}6^z`^U7@^w!>-D-As1kcW=d|!%c4d#gDu(3_Gxb{xOcJtxz{1R}e$Mr4Q@ydNQYpD66>mdj+?Cot1s4W%KOP)at8KPb<E<U@E)&tF<nfH`M8+NlWG3wPAn2fADFadiKA>s5#cDx@CgFr+4y%!z#?VTpJ>_#oYpwvbDdfSJSR8e`8beSSU<Pt=P0Ly#WBXYL#JpMr@hC+QDWb~}akxY~1=!6fn*fRKXVf7L*;1c*sa#n-aQ>|v42j0V<w%z#R__<J*nYZntEwy(Yn%m%_+8W3TW{|%=k_*{(&RLGknXKyxmaTqOnoPg8*PC`Fr7HlJCgeM;L`(cLxo-rR!c#Qjy4wZYrGX^9Dl%F@m-t=>_OO~Ok<k4($5xH6_O}Zt4fh}p-6>NRz<%_LC$`SRsH~Sh-NS+>^OnJS>D3k+x1S)AbYV@SyM3CAn<&SNI4Ve?NuVh#EA&NQy_sKz?6hcgoJUWpEz;0p9|^46u*FouuN@M=y$|H7B_8aOkf(Zc)Radme4eY)}0r))@W2uBDnf3op-iw1=Vn0@N=p$4fJ>3c{<P?(wCJ-WE=B@L2=;`OXK0pdb|fT=+2(h@b7cO*LBL3mSOCv;bB8#&z1Q>f@%X8ZlDdNH%pLA`8Rrp-M0AyHMOh)<#@pqtQ?c6!8M_W?_^YH#l#^B^<25To{o+c>M1&Du9E_4qg-3x7u)RbG_Mb0G~<+$6s8#1b9CHo=kaykCD9;ZDY|s<$Nynlmr%&}o_ye-@5Ns)KHZEf0b3K7%wkUEkYpB(EXOWuqLH}(==ml6mxj!)FTPw{|Mlwqb#)9M9q_<sXHy!;M=zd7-mK8Iuzp>Vcje36@nv1)^pi7>#IK8}G^(Ryp7xN1y?zZA4w`f8#;YVH>!Wczg+;RRr45rjsEA9Z+wsKs!gj<5jD>GpTxjbCstsyjv22U{uaWpWn;clFX3K*$hv~dnp-Fgu^ssFSl_Q->5<`SDhJjuH`A9Q{v;k^!f})3t7lRy6j!=9nP>kvkPXaUw)Nmp1iLG2Q*{Fz`iYVjhB!Z}jReNF3*1<I~bI1?pOUFfnJemnKA|Xktu2+lHWR#F2jBXNM!7w0v&_}3!UJ=z&$qXHF4#fkU0*$ipVrm;*3rbq(Q{;mu@~2qPc8X{f#HP2*g{J1p^8-evptgxQE-+A?EkWb(!|)EnzGGJ#exaWUIoZnoGlH{3JslW{$!0H?n90x>hywE}9K$5X%27Z3aQ5YkR*_|1Q_Yz$HM{ZhNZj;epm+>;!DAhoenzcPrH$vQFR-S3>K6nNa(h|DRysd-M*c)zlxeu!*qQ6lP&GEo&3+WDgxm@e{DMjVcw#>>ewr$yjuR)FB^Z~m3=D1|{`n7V3NESAZx<gvj6a=y1aQk2tTzOTy=<v&rWZy;(LA6I4`{NnbqlSb_2uU5`UVxryVt6)cEPje#8c=F(zC2SS{=X~x$Yz(L2Nr)PvX0ABxzNZH34aogk!c?yeX{<<#=%R1tC=#MPU>VtZ68tDaNEM4T>Yc5^go(Y-9Q5I95Bq6({H7<Pl^hJHu(xsvcd96*JQ!?zb>|0C94bE$rbiYkx=(oaUT1NYiVxXdE%|vz@@Zgp$KitBB)Nb3m_qRw-b7(E!8%2h3l$bJ%TJskf}++VFx|II!Y7Z)r6{h=R)(i^7&q%4+?3A8yK}BtB4jRIrgyvLd7E?W1Txn^+_=c3EzvGIG5^GIUcK`zlk5+t)j4e4>Uejh&^G6YT<9VC1n!Yn2dg4tmx(pJ~^$WK;&1ljPmKHR_n*<SR0skHpWyrser1Wy+TL`Df9s^@+xt#RP`;&~iOz5yFI_ZGcu$=8nF35H4k4H9J&^0Kz-%O&?lbFxHG%G$^XRTTOq)#I&I0V0)G4SN=U+0YWUG_#NJYVL=NKij*;+MCe8IL;K4!vKV!gXe*}%6}+gn^?LH=r^n6H>t7~sUQZ%iumAp&D}I`YpZ@d7+Ui@jRQYU_!|v#bWPjmaujbz2XrHDvswvcbG3t}cm&^t2_D$WpWkWqxbOzo4&5&P$1Wn2Jw1zBkCXxk@ZR_%w4c4=OjVKtAKJMioLukO5>eojn?uiiW^?=mLc)1}YN2t(lZS~z(q+6N>nREUd?|z7}HN-|TFKO)%lvDNy-(aADwRE6MtersxWoh%GDZ%MP<m6Ivv+DWX*<9IP?53=enYWo*yfJu~>`0ZMMkq2|5_km)#%66|m}Rj?F<U%x6lf$}o<dCN1hHu_%X%~EYi^j~<A}`6f`hi04%hkLhzoqbumI`gqeDv0=t5*t6ql7NVYS}Ng1f)g>ONL!XEo7*M(_W<MN<P=_3CEV+iPkyk$^V#Rxa?1V4B5As!os;7@t$_^g078Qrs(%TDRXuo;$dSR#<ns+=3a7TMdJ9DHbrWK2jE^3JXLFCmC2QE~y)jbYt_RYC;KE(u!+Dv%SI?8{Vyf1rCF8-8Rr;!@mdoaPQ92xP{6`%$7xg-rc!;%2uC)kHTA6=6e|HjTSOSHuqtDOcU>(QZlCD3dr^V;`%{MR<JrbgtDMw#&#xi8DhNiFJ$mF*jI#!KVE&h`AcfZ7=-L5EP?^#Lf5uF0<5V!iE&AoCU`yKB7!%KW@|iZb!cbpRwn`)NXBfoaNJ~I1y(6Rqu!UV5iNI@vo1}tNd@4hC5siRK(_)o&z;ED@KP^M3NHg|v>i%T{#D(YTaaX{^-bYh>w@S#R@z^>D(Q$Q(yEu;-yozXjt;PLkits6nlBE!U+E8R@UN;VSpQOK!Pi$;H<aubg#a$OOuqo~bWBuWuS-dax&<PRbt_8~5h_O{YXTOnyKt7EIVo-OJVI9#<r6ndgH@StX$WnU$)-zB`mX9<g_r5tWQFk$a#qD{K0M?^<i*0h>D=>O{1Bd-6Hzpfer<o`ou!57!^nNgNfSM4<K6*#fU#k@5W)w$m&FX<)<TA_VT3R3Y$@{+>FiUnD7kCK##3WXYt*%n6BkR$;#$UIPBT#MqSV1ajphZ$)T4;>%tHD8BR=x5pB83F^B;A{K^(X?O1DbSaf=2#92EgO_M%N6=^)I2vZ2si%Yb~Lhl85^M|_m6khDuPqD5guX_18<)yyI~=s!N_K+^-8hRR`QMptlQ85f_XW@@Z({sVB@4j>K2o|`Gpj0rg5kDrpTW!kBzJnQoP#fNu#Vic@vi?I%^4@~V2h&JJPmu>Z}B9BtZPQ3KJ#0F_l>KiN_juN6RR*jgM#ZE&a9i5%0R3u$hSh1c9+d{7C1Rmv~g1ng{nxMi5$ku}-JWx2Cnk63Th^xR?{_m9YfD=r!JXf8gA2|<!7D(E=y^6`Rjy;Z*105T|?zKro;*U}`oKiHLiwtVzOUfVG;?QyVTzah+BqKw|njJYr?BDTr>!^k+m&u${W_cw_hN^DdkS15ub@Ha4rV&FR<Z9&KlviO^yksa6SJMho8JZU>P}Tf!)T+rE<biV)J%B=f6hEcD+oD_aW!~$95m<6B;_Mf2$iHh58VgDfi=+;Ccu~5os)bEnin8yOCFoNQEwL+j*zI%+%dAvIy3UoXam6SuL9OcSX+7;-3))iTKOB{|A>npQ3%D6l^^pNmG8%SAWiOz)PXU0Q$tkb#mveg@YEYBBYi03z>Uz}FHF;h)oXAV|;3l8ZqUC@to5E&ppB5n9QqE9Wx7GKCsk@!7!Avg`qz?_oaK`^Fof4=w6*m2P?4sy*z+oxdRpSO#=LXF~<s>6?)v9krtp#n@kQ>bLg?4Rkskh;JdclFWhCJv|T5&ss-^XunwrZoUHjUXb4KDQ~n8y0A+c`S^W|w*{j*@JAnZ>7B(lZ+D3)^~jctZbK<g%drUubuAKMh<1MCUqYmBa<o7<TWFDw29u57J2cD^u|)BUDyx<oi=Y&^@+QyQY~ufhpaBO|ywsT6I)Yv)?RAQi3N9n(9>Um*YY~hmDPxBDXd_2S$UEuF4i3#GdEDRKS=RpVoay?dBSsJMmacz#*OMuruyzrITYm<~~Q?5K|Z`)*9<YQtc2y65Wq#`lvk&rlSte$v88i2bv2EI+$h^hpI{kGPtU>yO&}r5MZ9`Yxf^HeDJX9y!nQRM}A8N^sy~oG4-OUZ}PNMv_jod!HP`Yn@!v+5|O35nOMY@;KMN3y>gZ0Y+5aonmzSB<xQm_|1$N%ST<#4H%pB4Jj&Y66lA*?N8R7Bf6GI1l+MA(l+F<<x6yZ&F(q3x81#E(JRQ}!V(I)G#aw9;FUWG&x!Q+aj%bmvJ3Q(ZJ%Y`q|8b4!pL2j}L1dirIw|#l^6uN>Mdx(X;CC$5b5=>H>RJ({WW=&~Sb$INOm6e~0$PIpD|k_v1{4>w6Y+U0eK{>GF>v~=DzS9Z*9p{m5dL8H79B~RI1`Uxx;HiUO6t{&?MTKeKdCr27cz;wX(8{nLLjaLWnz!H=^DtoBj2cS;O-Fn>jl~QyT)Vu^sbR~`0S;cOULCzA2nv33G}(w1?2mD%%7)S22yi#qK<haGkEF`faxX39|24GE6!Q!Y^78CX3cVj42tOm9xg^Yu$}odn5Kxpmqg!7jFK#E&b3%85x!<AwCpS?+6{f@OZy%Wkm^vC)9xs*E!EJB*)+2rbB9D0*wfY%1sfaVku&Qxr!cYN9Q=vc{D3&T-|H>ce|keJ`iSAGd{dqJ(%cp;{UaupFHRfrh<WOJ6x#fSx_o18Jzv*ws;+#PPJL~0rZ$|V>mBWNmaZZ5E`PQT_SmcPvAIPt&)-nh*Pfc&gOs)%5d$avB@Jb)2Oy$=_-#F)&+0*Srj~7P>8eXQmrTCck=d{#2(0tew=RBD3X9n5IMq5wfE?N1Jc+3j%XnL)eXkQ!bu7J|e=G5MigRnDLq+MiJq~;m1~{h3Jh!fovq6#at<z$uT_JiSXKIp*GNVLo1%K|lkLB}t^s$`?cAOc}c0fVfut~w3Ra8RzOu0}4yz~ci6As(?bBEtN)7`+%9DO^?AALJK*)Mid7u24hw6i3k^`gCvpDKv*EC^PPFC1_cz2M9B=sgOPm3lSO{?VfP=>L`=(%$Fd4x7)#6;86X>m$d_$K%r4)>{%6Rzm|#M4%d|35z#}p=VAop3Y$=+Y``yJxtr3DqezWXyl7JFSi||`Qd{yDbx2b0R&Ls4wP7aaN4yRk7Lapa#N%30U-eWmK=rC2$T_2Naj(vx>diGHJahGx);3|u$QLg?@loVI{_}r;9mN$&QLOn(;V<jKnq%D;6#u7w0u^~OVXGG%<?ry0=N)I2C%B>o&Gnt3#eZHyqEe-{fyd;S)fKm)|sX|-BRCch+a?~q6)`<^nwGLLF2n@(($K<uE{C6vA*WbG6dS#_f?*CF#x{PV^}{sBJqalWz=8mPR!=E|91R=fr3XX<IK75Xuz-pQciw4c+AHCw2P=pyR&;k4qt6^ljfYF(wrQynbzrmj`}hPhLWIcCNe&}6O^8nMU|~~EH9g=0_kL`!4Qeps+~!-Qh{odfLVNENqwbo3+QT8I3cPCqXONAiF(gx@qBVZ(GD#zM&C_hs57E9)XF3Kns-VmwAT#Y_INn~$4T=qBq(I57Li;-uIjfgMxpU~>GUpNWY_z)w&tSNA-)~UQ|P>AeHstkW`_V@cIyt`j#t4H9h2VL*p$ujeGcLZemSekP@6>LNt`+nlQOBzcuDUIqF^+={*X`lQ`jX=PkNo{N}M+)l7~?E68bkbd2WC<U<Fd7+`xj8P014D_bNK%l+y|t*if}dW$A`W+Tl1jpPo|v6l1OiaXieu80KotD;Ddqf?|lWlZVfVaej0XcRZ{QhrQ!M-WbRm#X4!ULmf5l*S%3Db=1_onyx1LS*fKXK&DSV1U;r?U-4!jy4r)DCKa2xDJr75DJmHf?B;6Lh)!3jduny{?N-IzP@C^oJkiX}=o8K0OWiH35bWxpu9u=6Q}Qn8$+v6W1lx?4{K*3DbZBJ@#X5z5Db1jNDBYiTvXpgN?o`1~k85_T@xqtR2xM-C=0gB{0DydJrLzRO?mz#*UbE7n0)6ItOQQ{rjC^jn<_gXzXZ|ME#bQEJQ?7^NWP!^7;N3|Cy%#6r23>ege8z4HZN5?3F)Q0Nt4<@Ge&H;9z!5sy5TFxk>q(PAt!v8<tHl}k)Rvxm)zWHDYl}nZ&~(8NsCa<BTH=l9$%E5M98#6+IKjqleZTiT6nJH*`e2@+1<8JwP9rr3<0@VpHZ!5Mbfk^d;emWmVYRaU;uBWmO)0b7vADXjx^{cqRK~ViPntz5n+89E0$jxdo9Td8Jbk{U(aOA%IYd4*dkm#~Wc2gP%8UJ2=^Ir*`T_(|#NtfF`{?m*;Xsa3In-Q@B7Y`65XPhzs^<<-aP-!2UYm(ZpL(7+QJ+3I_$nU4mG9Dd57U@jJ5zc!j#9^3BdX2fT7XfU{AFH}<GB0^%<hY0@v}a^nG^S#8`R5SzD~o{9JVPFG-)HEW};!bHa!9oVq7Y`Oh!pjYiXHQ6D2L2xT$2|w#$Uk`tI+q`nGpG<N(`VKDw7p`OT_u_Ntxj+lf_vfj!4ck6Qn7Z%9tUC~(|x7eH;(E4Y%>xkSs^gjqjRf~Vs%)=NU>@%Vw{IdM8^HGXqNTOG4iFA`Wdw`hIk%Hr_~ruzMlR}hflxZ|L>A?7|d#Ph@HF!k}X5(}1e6q(+GWy)&<UjI^CSw&o|)2Om~iPrv=8(&{jglrq5hTO=5;G;&@1Fa7=XrqfV<!r-j7%fXHGgjUffJ{QCrMJ-=kh=5LfOWB<+^cY&v#C{h7f!zGJ>G>w(fef>Fx%~cB~`<eMioZUS762sV@5@&WzeW5!LJn{E)dVRV@JpZ7-i_bf*_xF4pY0cHl)>@f>I8h7^2=ITGVh@v-Xf?)~t~?g|nGoalBIN6h;(}rdgv>Dq5tmnJuR?|DUu={?+=ka_Hre2&AAhb0;BR9HFzL6MYhrDYj*jZ}!ngueQaEUK}?I`~Ly<BL>(')
_load_module('montecarlo',
    'c-rkfYjfL1lHXJ1|1gJCT>u+mBxmD0bHlC3GQFoO%T`%RvR6D74Ut0<5eQ%bP!gllf4_dr696UeCim@Bu|xvXJv}r1o}Nh%1m{(8m0YD+S~uxjEQ?Ccle!s-vm$S#I7zCk5XFtGM6;G+Asbn3(wrO5*GZZWo_+P~tIN(inXl4ZimPp!EoxCF`68*svPw3x7Pm6X#MO@e#^QFJ&etM^w+K+=bNTG6t8F8e3G`VMqRxt2q)V)~`J$45tyqdmCO~o0q(xp2#N`^mH^pL`Nm0T8icPs~pd%#tc3otEv4mk}awF2bDMY^Alsl1BRkEuEkS63!l5G<NDS!qCxwuW6HMbO-q*>Ros0)!i`>NXJNJk=;@>WwOVCJyb<Qjh0Kt>M4Rscn_m*miuSQp#MOc`Osp(CL+%neVefT{Y-6F4Y$pT!ID88FY21$`YNw1A&0=nc_J_&gH7jNiYXogANw=VG(X8u$|)i33=bc?NhQ@f;pB;#=|EtM4O*mp3wR6oL`ZURqFjSB3`)lwsiE0%xmEVS$KV0#~R$on6j8js^XU=-cJ-r@sQsO;rJWA-UP{Uq6k<Z*?=^m5>2rq9PLBPrco2U`~nmXs9o^%bIZ=`~_P8hrlf6>9WWcu>g8Yku>HB4l0?a%}$8$^5f<4``PK~36VCwjM`{U&M#u_S)+j`4hH&h(2PI4wK(oXnI$lrdJ-P{36Fm{e*=v8tDGZ?MYx_9$)<$KULiA-Fkl!bbQ+7iXow|O8Axd+7FBXP#A&Eldc;aLz(DY?xXlf%&%Q#Q*2{-WngViJ#R_r>tuh=_8_;R1!~&W>`-&MwH?HSvNs?B>G{MSABq}Efl?g~P3IT9<5CqS@T2{qI%x24Nv#sQ8Celq=R1M&Uak22?;HlLjX_9%C)F?r!nRyh0Zjjjm+p1Sef@_hN=9yA5@L#zwXa^vL%XFntzEk?`gr4d)N?EBkGaBzq=D<-anM>r&nVz#5D3WE08ihgALW7;=pmb<FXXDFHrzaP{;*)^+h1ooah5CN+)0>N*KD|3W8P8ZI>?_NmLCox>egcp65CHjTcKYEz$0wJkA3p?B?ECHM1$6%ACwzhwgu%P?PA;(dPbd`ChPtZKBwuZ_q{46K<4>3P_XE65GW_(uSmpeMxbtiAAE1M8(}m1-#Ew6I`b4~l>{_oA-~m*^sJ@DHPI?V&0jlImvgS)0krl;tJw#+_zK|tMFLD)Pfi;^~MO}lQc|~ju4}kNM6_^7s1Yjvp-^`(T1u~GO8^8un0Qn|He4vp*W)4UoYAs0hx<JI)rl^5k3L%$EkT;;7kP$zD)Hi?-8X}|9_z)c#I<R6@3T6m+luT46Y2XBRfGv6ab1)4lYI`6pU9FL>s@Sg914MKpQzAw6i8LC~n{TTd5TOPJ0WyRjFttbVtHVQOMH0kCRuL(!)8A02fMZVIpI-jg?9ESafkS3*{_Ap#tNil&!`a~>{loQw<(a{v&d?^n+W>l=;p_zV)u-{r_|wlHPe1ARm8@lTQ>2yC=;ZiftluM5>eboDx72Is_7jT^YWoNgMVc}MpS?eRGk%Xq?wQG5R6`M*wpfIeA`Kz-+nde+=wmKzV>_M}1k&O*M#W_u1)gpMc|dY;6%YQ1AH$c3^GBoDLQo>V$$WHKZ6(YPJri$%_l8U}DA8kNDJc)i0$dld1?yWi;3G7<p+LvzTl9O-Mz4YWP#Y%;8otZG1MM-efQtrNfinM$ke^Xs;_x?;928(R(4+ha@E;&ru+BNiB5>r3Zx6(GqF$&eg+{>I;0n#rcNz$zHrSm5C9pu@Wb}&^^?>aby84XRKLc}Xqn^uz7vuG7aJyg}DD)tE12Y|ZDA%AwhA4K(pRD5e1rR+H%d7xuN8)I3$WO7)p2ygK>oLDr$R%+{Sj%h))0(e_U}^?15sP9o_$yn50xT*D<`BI~@js&3mKk_4;0{1jutn%K4y_K)iWumKp;PFK`XuZFpg4-%2S}{{1nG<{rgSOjF;0RQnF$c+B&Xts5p*^5YzOcKSl}G#T5hu}M5>XPNROB2NI7Mj<Ss-)vm!!jy+)m`wN>fw5GHQ0<rZN^W9KP*Y%q>-+K;p`jY2!GPva(2*TVX>cq5zS0AB$|ZHmG=?6#Mf{d1B<L9$p6d^9LGFoCcD2QYK~yCf^u33C{@v44W!;Elt4W6KDH7h!#fD<G*2K&Ur+0My(-wDy7~2oZ$TZ%oM4+yEXQwlhV_3usMJy+DPp28R^9(lXR#G4!89q=A(I@e=3^CLk8f2am0ibw65EFpDboJdy{mqZXCvYLloYKuA`sh?$Wy0Q5Od=i%W|L|PMne>XVn#nUsEOw(i#qjXS*-H};r;1)pW@-u{&a$HqK6)uBqex0Ku?W*XZxHnVqz)qKIC$woeJGm(3+!}{5I_TggfRlk*a|<R9rV<@><#KqzeUn@b92J_AO|Mydkq^PoYbh7{p?XwFba7`pP|v3M;md#1m>|j<!f@uz1V$8-0h^+ZLt7exDor4)Ko1%;=5B=TA}x8Ir8dZBtgczRcPzbaMjZ^PKWK=5!pKTB%*Fz&I+!RYU?Ojo!+g~5j0@kuWR!bQ?fv=M4Vbitq74W|U;ijZH6<N9v*fBSvTXwhuZkiAgzu89mIQ##13VzNl|nI0W=L^*p;9)4fU%h<<{unvXP_Dpqb*wFL@pkgzys{t=y34wuVS*o>LXe-`luvNN0qaBoi3ZF(H$CWhX&c9#)V#WCt|D3)Zv8vao!!fH$Y3aPiD{Xr4`z4vP>tZmKg?4Ij}9IsW?FuQxdJA%osCAQC-7Gu3cGPpaV99z<2N#J~in^q6dA)FHvk~o20%TI*y5k{F);!D+quF^#zLZ)FzskV_b0a#;|(t+iKHv->j2*hHtxX(s~AJwpn-IkdPW(;l6kI6l2Rfp1#kfas64VG5x?Bqn-#iy(DiaV(O9sFX|?#ntlQ_84Gw=ESI2*1?36WMV0;rN|`_nA_#CmhuxvN?MLP!iVYF~W4%^Dh;)Ea(!!v`M>BfVOM34r!t=dr2=6*8sOKwLttz>qJdX0RlYEwAinqf;^RnLa=9iaek4>eThVU#FzbNrOdwKFD5GS!Xi!5EOk?-l_60CTdFL8P+iP2V(Q)r*-DaL_(0jd*3WjjZH@11%?*ZY!R{|K4^L|*Gzj7stu=3yx;pil!?-Eoq%7btTM97r!HcLJd)A5Z2r3sXv14OQYQ7V{+pIevnSdhit(VFV=#ss=yKC^ifMc0jy6!-s@xfZWaBmX-YbD0mx0+VP-N@`%W^6f(QPV<v3C;y9?$^B|K}hm(NP+#in5D4F*5_;MUfBS&`uG`5$EP~NzWrx=C&eJjIAx1O=47>Rp`7gNdtfR}g+or8RBH<a}Y31{@6$<|#U-TcbU#p5EvOIXF<WL4CmY9Dn~<rA$y;P$uBs<Wp>EEdhKlp{2Ak*`jlZteDunX?hB#RMmD{PXz3<?Q7B@x?_jCHMTz@x?e$;*0YJ?Qz-+>>vf>M!|3$Mh<gg+^gn&0__H7d8W3F9^NFK8cS_rA~nhUZU(Cq8Z;-z=TWPrn(S8Vx8sxdrys`c#xUothI$vn%uQCzF$RJ;X|dt^Vopjhm`(=^5ZF8kBl<8~z$B!U90?r|KiC+6Zs$qy+Dsg@k)7+?Sh;s8#(Hy{>P>5w)sj#2RNqc<Tp@$02(MWOkyYg6#;~~k4u{AyoUt*Kv9ffrHcyxrpT^EV*E+?HHHww>@c=Z{G#S*<sw%c6$?eU6K40y;nRMnRFLEtB)N;bVTRi?RhQ|l!G3eF771fzKjgZs^_RVS#6@%_0irU!=5R;K1VUWV|0n7Pq(6o=79SDOhM(yNk)mFr+rhSl<m^KZ~+QYMHw<#@*Zj0PLQMweudta3UBZIE)VgNt`k3@eF+}DoBqWKNXt8C_L+<`+!+VydCVt&a<!8R^$BdY$hNK7hnLGj(SlqGMDk&i_vk+jZOkSIME$tj4(XBzlax7X@IsRU3%Ag)~q#nD|TrH*=mfc3ioS}iezC&AXe6~9M<0S!b8Xv&m}Fo17mny=b=?~_TfPg`t^YV9!vxL4;nD5JK|Zf*NLFiluRY<x)im}IMcwY7iHSgg6P9CKg!=HB+DZN49Luoa~YsxhJmN7|64W;<LdYLB!YMZIKqL%SlF5eKg-FB%v^)z%(9B`xKyhBx7PnYQ@CY&xwWd{3(RdMEw~wg5*xM&CQOZhmb2demA5eT#2mq2@{v?R(|1_Nim-D#zL_Mx=UgddAUk=**w>TVr-h`$;omqMT#p&pMb0c%)F6Xn6!{oz&DVd#M9_rL}{T5{sOTS{ms{jaNG?BmE)vJd=_8CGI*TBmE&ZZqZ18h>e{e=?^U`EVGRKudyRjBm2<-SH^@UfQE03y5)4gIVpaxy|VobKwB9t5EJ}*VB{$52eRR<2ZfJ4f7XY>C2*U=_sDfLyqCIS#z%q6;kJVBZVSVAqdpECnNJP~$kRy6)X2yclG+xGkroiYKNUBQ+EQac@F9aZ5g=I-@&zflqe&im@^LsgMBSv^%vyXvV+tA#bW>V`YEr-w^N+ko#ZTNmaKGn{IsldAqemTe7oq%Q$y|nkKvNR9&{mHq1)>vM$vZ3{i#us5qggl$9obylX+BREGUu9vDxK@<Ga$?q3Bl)+^9!>{`U?elRQHu*aS>5~g*NDefDORZeVNqtf!gYaRtu@NId?F+6wp^#31jw1-D(3|WpH<N#=cch$5mdcBrcQ54HvO(7!^1-;OUfd;ckZ#H_(;`5&F-VU8|0ZC38`+L`(S)!#~HOk+Gtw?;5eqpvQ=92I%90B@AGK!J@ZJ8uUZ~7cxt`X=~qyw$_%xJ%BvS?pq+=oT;V!W*R*Nj@SZ+cDsxfw&14^XUFH~Tzg|a`yy5>!NBS%fsZuLIX%$qV&vVrCosz)Ll0EmBGTTSYcHMF+(D=H1|#PC+;LcP-(fMGYky__6oj>k4~F4ip1J7(3Sunc*vWQ8HUrmzu!tGLVu+$AcnAoXY|@FDa4XNsy*YCC8lm&aJe`;|fz}?d2cUG$<GzcddfMK`7yB4i<-ASOY-daAFk^324M_()03QFdlV=2JS*zkdtX{3aybX+SgZGBv>b^oWm&9l=FUnmQ8Nf;K?)XGyz_h5%z~HCAWv$mbFNUQ};Q7PbL7CnZ&8$hTs25m{k!=tC71?%^*CUP`RayeRLI`w#wQik=!23y7t0m~OQLqHpqiLl?D1N9UYbxCjCki9CLZc*4+?{{gjoLPjqs}q8!<Y(Bj4faZA}{ykvb77?NvxURAMjvdfG1=fl9Z;@Epd`rUk<yo#AyO*g8B_%rh}%KQORTIx<*}C>;pzsFTtW<JX738gCyUD(Xf9tV5&Il1yIC_A%W*fPOy58utM!N>PG>S)|abOf(IRt^Xh6#*VV^FGOm)<7G9d&jRdHj>(o2lJRM53oD(esyk~YnU&viC-&#%!L;^VTA-Ef0Mw`m`FIDj0^$T)g(63&Bkf;>VAGE)yYtw0yMU4Qrd1>=Lq)h%$hcvOMu{=PP3G6RhqLHGfH0;Z46V8E~a|W0D#(Sya0V9ks<ufWB9}xuuy`es!8mbCIKtGGEx3#GPPXXy1$vzlRNz}=V?Ki==8`=&aQwdssP_L6xP7bGS9PE2MjRTBE8%H5c{gy5eAv}dk`cVV`R9o^YCJ$O$LE7JDiK`%vVo-ng+nWJ-6GbG~xCZ2N8wGV3IRzLrRg4#UYwsFhgREGsa9hw8YS192<mzcmSc`)c=_(8icfHC<E8;4ltn1V?6gj)?nQ)YcrgbvJo(YNnlIffTSY#X$wkT*dZFzROzE!ViAMxn#eu3)dRd*6WEzP;$x&+<L0OA5t_fbdLQ%e;-^{C%@kvD0+m2F42zD6h0h@hK%8i}-PQi_Iv_Nw{*egINWS`Q2tWshhG&PpP?QeQQMkWtiQ5X{<QGh8#m)Zb1m^ODy29_R3Zmf1)aR-}f6ppzTzI`&<LY!TmP!@VT8IPyzKRv<d*hNZ<2$YlxF%8-LbpXOBZaJ#13ZV3Tll_!e=mZ+*^M*FJCDoJyo8~0)Hn2{+7I^Yu_3YjU`g+NW${m?-o!kx^UZIXc#x+zou$q}du8}VRGQtfQ*H94*yOB4X~LgjLq&Ql1Qcfk;po#V&_7#sJU770`lZKw?aFJ2UNfR&Or0InhE1A1o)<{#<RUoBM11?>amDA5zwZp5Aim_~hFUib%Ga390;#QIqQp%l?hJ3dqi5v)gITo2xC54I&bo}p!<c3KkEvYEe;{t$bna^!yL@vz;Yj`ojx<bLTvQ^*mlJDaKz{f>>CjP!?C4{fCWx+$D$n}3Oe!snT|B2c*`Y?*8+#MJjuV!wL8^;NXV<_0SJ!WJ>%?Kytq=NEfi7^G?v=m&bI8;`Q-cX|%=J8}v5RUw0E+n9EW`1*IMnO1Tr7?-=+0eBNs>~=VK{o1WpwJFOd;3uB%)`za8SNG7yXuOxt#qTB9(DpdW_81-yGX4IQwBdP2H+j)wENyG5O*1RLsAaOMq+C4J(%X@tJ?P&P6{w1Y^hO$QLGKJ0*2A|Qw*aOyLDe5(W%+?$D1iXeXfkAnb;?IZC-^xQ;H=R(P*Y@SH!65SUADj)4MGO1sKuy@ooQ)dYmy36t?VDmQi9G6UDQ~op;3brDy($I)Z%`MEldqkERwsl9vww)!FHo&LcAE+5jqWsF<MQSY}<%=!Zt#824eCJI8ILc*y8^`s>YyGnSOnOAHli2acg)<y`4yBUzav?+!pj;g5y)7N|pj-)P>@L2HUCG^+7=Gzv`EEcgMrwczxPCWE*e*UY)aac+!E&#~P~oS36Kx7aS?)HO)iXVCshla<0S=BEiiL9_?S8mhDWk@~ih&OcMq?`d&9~WrKS-Kp8S?plAdy#F1~Jpm(Qklz7lx2b4Bn)Nb(`V5MW+R;OYsCB*7Dw=;Mncm^+unvt{HsXE8ql9XEzp&`*sd|q|rq}5=LptM>!;-V#`YD<XTEcu-hf{7xd>rLK3{HW-+jf|Ri8}UOgw`E%B@7j{N{uoG!R#p}`P3OWJyY1F&4qAVutPx;lmkhJ=KWao?8qGA(-#aA1iw;S;2Nq$6EYr2gw;8G^&Tya{927N@x;^xhcWxBo9hV+Di{nDa9f0n6>Y=k{kHb0#u7`T|o`%39*h7D~Zo}5m>{d&de=n~3T3pMr(MKg!Vqe^(5)T+dWKb0))<-3H`@$-dc0Yj?l`X)gzGwQi9gj;It@Y4d85^)@{~g@-M?Lp;0x<}JPg{M?hAsdQpJ;LMdX0RG*J*(0RI&zM1C^L<IVxT7RtX-3uI+{ggzL)wbJ|iLAcE&ATP7)bA~UWIdznm{I@A<lz^^6CNvW9P4&x>5O`!Cg+{z19*(sl{;t~)HnW-@3o(OR2LLO|5r3qSEITYnV(i~wxzM*`r+?35O%(=h`?<^7ON`VJmgN^gnY98j+-P{X^=Y!P7IWFInN-M2mJ?|V*hXt(ozK^SPrLRoEor2hGd1C|OU+9hu)^{(>2?0D$d`)}SBFUNpG&!EFOgU?Tcc|PJTi|0{gk{?3iM`q`pyfbMouVj}e$;3848U&K$L%eG9Jqzub2N%BvgdkPo{K-JQ^iu2es|1p{RfI@cnbXwBhh;}zjf{k28wn@v$_rtAMF6<rbU;-rEScuT*xx;mee3ds>Qvc{abM)Uk&5I;qpP8y}@(d_xUh>;EM=i5wua7>wxb2?;~j8<JBa7DRSW34nDqAAp`A^X{NiCim6bM91x>mLB>+vsx(@S3Q-khYz9`)kSVlygr02lF^-WK?Qr3)A+vDbb{8yHn?uMcrTo4%nosrbZk7L${acqGXUKZ}xfcNPj!SzFiS;{e8Aa`_)K)e}H$@DQkJyyas(^qKLtZ&YTQjxK8Pnz)bc$P(n<-~yTPb*)UVMinp$21^)`@FUsohp8cjr0%`=!g{D1!+}bF3`+O+9oPR%ihlUrWK5I#)7|Bd^ve<Z(n^n?ahxV4Cm{WRtGth@BAP2unU**uaL%1KMb5v3#tYx-!RaCjA-VsqeZ43K$#;^$BQV1i{c$Xa+P5@PPidqVs?@<k43l;h=B4>;Q<I2Cs<WT3~wqXBxR#D4Z5O_sY}h?bu)-VKfvt^&No`Rr9v5l#j4^nixGk_q*d;u~2|-5vm#UtK0N0w0U4%tn;Ho(5>g+)9=@Zd}~RvL%(o)Rc|ZkkuEP=;0025FlC4vfl_my2Rmoh)#8&r6X!6`9@)hGU(F~Rryjx0oZ!(PCI9!W$vKl)eTS3So;IK_ATP$=_7UEI_vSg?-17V0mfv?<o`H-*(;Fr19Yn8t5xwp~lqx)F51O;&j$eZR*?D=<Ea+w3fHGVZ%h8e9F1U%rU&K*+yMR1!KQQtn7H9X5swxn`A?XcRehe|FG~$=z%Q3`H?;(`B9G}zGRZL14*t@H!fHB}0F>b|bdICb;=6MS$13^Gynj~m9e&il3i{}g?pFL>4?D{N=3NLcogUY>bs~z821m|?Q+t{kXenkEEa#=L+;$Pp0Q+@MW&z$yvPOa)#0yl#V;T;pOA0$+CPeR<f_r@HHx6fW<BJ2_60)8SMHnuWhuH{mGpb6Wst_m-TIRMTVG6%P<D5a^N9di&!Ra>Ze)NPClvB1h%y2%T@6O69a-Af5x^|sRig~15GwuF|iAS#wB_Ni#M^njdWH)h5w8S`EH7DshCnMsaQmjJTZ&Ver4Oy$%D-kU*JL%>8}F&>0A+0N4J!=-p8-%^;%yQW>3o6w#SnSHiK;Ly;bP4^4Bn+~DUx}ipZX41`V2OCmP&<QE1o_qx`MMu*?bK(}2`}P6K9vw>n-yin2M;7Y`;QOe0KsKZ{iD*!qeGOQ9Qw!AJev=2K1m7Khn7tqW%$JCTfx5TL8ufs!w_8|lEi&3~SCT09AVDGtF@@zryO~1K37(#`*_H0GYrL%j&{9=M+r5Y|TQkwFu!oW|GEZQ$o`{b~HJ<ot!f|K&$H}!XUJ-rorpX_mRuo%^D~x9KZEK(vuJBa7a8B6s-kd6Fn6Hak=E9D{D3}wz9}faVbw#LBQ*?={%s{uoGbco%3R7KrYjhjl(yF94SvIn|O{zuh+(t{-O1e)?QN+0MQdqoYlJAQH&5~TxwQi~o$>4WyNukb@#X?p6Z&cO;<7iCZsr*Wk(;Z28SRqvz@}!0#VwC6K+qq8Ft)J)xs;hqJdMeOcZ52eR1y(}DNXy`!xZpwg$2tX-Wu`E_D<_I`EblT_=WqxrVuRzcELu?ZCM0fE9W?SYGXrx9YT<2e<9l<A4?A+p+&h(Ah8kTPU#9bGN(4=~wmhE_Fcrx2&@ml|-{}3+OA#{gqXWwem+LeqTGH7V(9B`<#~5*E)n=QIB3)<dR`~wEmH4Nv1ggVZm=cJMfE`fS>i)2+&w<)g@cfUcKa50R$z@4bgsEdizG|UMbFaWBxc&x{S|urqtD<R&jgX6#b*zrLmA;_ywqT*Gt;WRbxW$_Sx<J61>c9B@8FpU^`iqX1s`tRIy(@&vmb!LtuSQ9~N-DnnR3gvg*S5at2`RJW3bRIdjT7EQx1>8yN$H}nwL%X^#9%UJZrn*A{jn#^7c~vN>U{;sm0H}f)>%DkO97egi(9*$Mea?Gn1=Ls^^t&>Np@Op%hI$24t=C0g%fy<7Y+J=NAzXEHS!mTf|}+4=NZ1zbhlG2*vU+ZjxNB1M?Gb5PJ7l5rY_TwVR}!Zvkz8@{v*J2w`B*K1;8hjrhOl&3Sd921ign=1^fuH3c8<ITr-bSTK0XEV(a~666hW>5%Lil6=;XXFH9?-u2dzdN>ld7nz(<_ic@=4<?nVKld4IR%-r0pR3%ryDz679EYUq7kL>*D@SrIU&?%~K@hqg)oEIe+<wl>m<n03$=`l7`br`266*U6KsOI~sL2Yl!3~!*{HYOg$E5(Z~-?3HnBuOFC1+|dq{{sQ5dK2EFipL&Qtf~qKd0&i)$)M$$WSw?7*0|G)Gk5TDtS^Vo7tRhO#@1=2eABtU+!My5?$1u<*W}%D7_1V)=s)vyfzEZ@8AsuXF0z#Z>qe4F^Un&@V~xG6Qe9bGs#U5fWY>#?Q#;Rq|Fhknc@l2b0XK}Hm1jy2cvl@`BEr65JA_M#>qudL$HeGNv&n6f>!VZA)0n@jG_*2AJ2!#JF?h$4U^SMiOJw=lX&E*LEs|=N(*E>h&O0saFVb}f>ZF=Fg;h4CI-57~x}xl#JUDvkJD3_X+DkB9yGZ=N*+PDfdz>%3F`_5S`lK9qftcQ-yWLUI#L5H1d^#>e@CEg8tZ<U6dZs`iN-Zivsb`6{br{p%?6!fT_t7J33t6YDTvdM((Wr3d*WpB;Ug0T-V(~W}=gtecjK%XALqY#Zwi;x0Q~y0=bg=;Dt?+-kG4l4qdK{8p`{D&X(at1epz$~K)qi#C;D~KChag##U#W1(G3IwOa-Hu;TQkLup1zC4gx=#@AB>9nHSRmheP7}Rs6`*r*xIIp4US>(7it*KMM$)Q!@-?*Y>u)w{g5=gy`aoF!(ITo^t#pFavS*dS9Q1#t^-J%ITW+H1YNa(DT5i_b&b5{TRWPTk@U=D*tL`1U38vsBsDB9#`o<DqSR5=zFVZ+dU;E^dkr9r!u{I4u;GsP_4vdh-Kvn}*J0FAY;@YgHr(xP2+F9sqfHCcKcuEmBUL;9SyvGqwoY8z^Kq~?C?sJ8i&E{P3EsGjO#i<!XUmH')
_load_module('report',
    'c-qZe>u%i0a{h0?@6h046LL*)XCzB|B%E19mZd#Pd=YGI7J)J#I5RyO9&yMyBuCO5!$2M)?~?y{lsrkks_rJ698!|Kmqgx`$i7rpS65ZnrJIi9Tx54LzsTaW6!LzR<z?{v+4E-?NmeEsF^$qRD@7g^rOe|(ig|p!&SfFuRFsRj5Hh`u^DJFTbl(v-Q6l46_K$^_tkYQ{XX0d$XUllKeEuw#^L2rqWhRO;%BgvQ$0VLf5ig@_R7JTIvpl*>#a&!3#4;*Zgho8Ua6llM1>$lMl>*}etLM)mahK&cQJ!Hi0=8UF7b3zC3n?bD1j-mKOT<Fv@`y{-3`HvC49zwxDT?^-Ky#kuB6|L8m1lpI(-H*=uRKC009iz-h{Pn%?h2XvBEoPMa@X-Kke|glx{7I*mN~}E<|0<4yo@FZ>aQ~*8n8>F5*>s^_foaM3<$?k-j_t84N7DJm{iMSqW1Z-biJI&yr8AQB!!&Cgl{zG*`oVAn$ozA<2-*h2k}K1&etUtEet_to<1)su*lMa5Y(k{raR1{GMXk)L93<fsv@g>O@Zgn>gNE9>^jHS*N)fOHUKDE>Ow5}sjJCqLr>IZm6TNjOnkLr0<NmE7041XwAD;wZ^0?!=?$o&+n%k{=~<SezNAHb8{NNqlTD*C%XQDys=POiFTmvBX(p0Y9n6+VFwK&zg8Jd7S10stH(Hl*V(L$qYhRqF(}gU2aZwUYxM5%#Orv5Nf!8pHldZZ11f^(~F2Q1Q8s$kwo!*`h%x}c-;OOxAvyX4iU!R7*gy-*kp`QPOXE74Py<l%|&lf)g`_G@9o&TiU(35E~3=Vv;AMEcFxJb;`NwTBlpv+~GK<e<Hl1~UB@frya*jyx7hC*biDx@x8`wypY-kg8b<Cr%y)^6}}j|Mx$V6QLEspyA+n#g5KEJaHyeG>j!9Kq{n@84a11c*=1p9%apWn3oGITE`AUzbGpae;#2zF#$&-cZ4wDM;kCOlOTEFqcdkCAU$sCcwj8lzb+1&)@wE26n#LJ)nOOxt~6qzvhzHhxE^(M$ezk<XnVBxk;q!iJc$CyDXJQ3Mg1S$fp-k9xaPty&|D-^+b3~rE!DVD#pMdm2cG*(XB*%cjX*x5)d6x#T2?yvmV=xqI+2cOs{53HTUhNNi>m3vnkWI(ej?g>1w(?{^sdT)d~ePt!7ibblb?v*|lV0MO#{z?%9|YSW3GAso|ifPED|<a`R9n4||=*#A%oLTH19~9Q5JKl}Vh+yLeVE&|m;*-DVSL|7yz4-2!`qvo(Bwo6nwN*YNEtV&aCzbdzW~nMLB(7vYhZJD+Zk{9rKu?C3t<h@D^eV>V~l5^DnZPt~U5LjV0;rXwO4M&mMZUdp8wp&Pk5!j74%H(pfh{TlYc%6jL`KU_|a#Dt6kOfyOfsV4FE^xe-#0;;aOBKTv}Ua4O6>VnELnT1eD^B5Y&7tR?K(54UY5$)wr*>OrWm)K&Hx<<|%&))`h2XW8mQIb%X*K#g%Hl-THk3m{SX*|zryb9{{Ru_t{!ae|vVJirorF|gST4{8*h_hAMf-+qdjY*tbd=#zsjvfvCs7t$`qfdniweP}kyW1V9lOlwX8c~De>l}=P4*9h#VeiJtY-hcqnqRnKckc#js-fs8Yg2a`&Lifk<6kcR;gz@;4t6f~@&DmKSj>2lXOn0W6Z^(f6tKLs0rhYk^R2SGA@wpZi5#0JLxmNUMzc(@YxVe~u5csD?3%Veo?x1;!R^@Ca`*(IS@|S*#d^7na)tVEAifu%6#WLRbXC2|eE`S5kxnDEmSb~*1Cke&Apl+NvKogTO)}V0BT-vq3mIQ8%4Q8&O`cYE#*9#JxrAw-vJp|NCuI0STgKP4L5|cI2BPO#rpP=_<6_}P_rBQF`jYIH4`2^pK+`*ILnXQo3R#A#y{rCsRn>;f0B*31{+i|CyxKQtGpXAZD`>Fd3LAXJ!jcni&UnmSZ{s4y%DAkNZG72P0J<GG-M0o#luhp{_ab-;b77(Fd>1S&a~N@>UC-+UP-Ct^yvFZ(8+5*%h;RSRF#yO!Wm2$rcOO6*glrxto5nTER_#nYQm*|kcVNv@OLC~Ta(6aAf>%SMM`sWKtO~5%SQdJJ!g`H;_~QxOY&f^;RU)a(7eNrvzU6w>#&7+=Ut09_FvtP}c)9l|V_vnU3cG<Osxheti052ImN}|{dUI^@isN)G>ryg6*2Hnj#|ci}zj^=RBazQVRglY70yD*RLQ=%w6KF&j)%&mhbar;=crBXNVBQ?RI(<`t@o5-u3rk?A>DI&&%SYwmM3#3_rdWY1=k@XBDNIXD=?Y!P3^B_`3VjeMSuLW`AlTivh5;Os#HaMHEV|Kdu<NVYjQDrQ>QQ5s{*kk@<5;s%YbwBRQaC$?JhhaYf=Y}k=2y0}3!xb~>(vV0@>G(LfaH@&b`QNCMsQw%u{#L%eK8D%2Uv*|1CQXq&51FybYuipGY>opNOhP*n`~XSR28agmZ#0MpWiWv&Fv3!=Sq3(WU);Zs}f}h1QSZJ<+#>Euq|)4R_VJdTBmW{Uqc=1r71?bpi8!RWsA{O2S*d{zB;3SP^;U(JAl=UG5CX)^WfJnXJuQMH7!cHD%#7+UUY~dt4&Aw)eo<4zE0CPy+-LE7}N?W_C=oE5jEj9EMYX1dei`ZP0mWLs1+Oi+yVp^1=>7!(bdAIsVPtw+{EcjjDTTDHn`K$7n7_kv!&T!{aU91L!TU_N?|qo)l<2xD@b@d;iK6yPF>x}uX?`_w_dZo!UOH2N#V9DE99JS4u-E^A0M*<xfMSGU9CC3IeU3<@bb6^+ZPRV!EBQVJ8C_9h3&`?rK#sMD+dR=O+86oHUZI7ePQPCLhvG9RckX2Xi{FVjP6}ed`BeS+wTw@%P|FN(a5O;;1(}x7`&J$!bryu6bFuZH@1u&-pLC$kJ4-DCfE`fE6=hXiq?Lw(01q#DHOBOkA{Cz=qP)qPo&9!fTQn{NiuTo32S8%{RSdwnf0}JMrBJpA2$KIB@TdkCC;z}Og_LPxl$$JQbs953sA*x9R`A1Nl}kfc9}WM&~Ag(spm{4WyAw@@xAAD@i$?;Q_bPaxtwUGCYog6ftV=gy7r`N5+tOL%*z5x++)PmKW-;EbwLGAzcWOyrDZ@GAhiSR#E)VqcMgxXhXgfbo@coxi5h5wqS4hAQ<J)b-LDuDm5j+aU6vy!bRL<4A|b`e#57v5P#)NZ(J*+45u^MDE)-P`2i+>fCL8Myuq3+~T;hyv)$y`hb2M4xaW&Eb<g4`xuzgss@N}N0S1MO6Ub@(c`bok2{~xA{LWY+fK>|wl<nUKBo8veqS+ZWHg$nwoBHiH_w4gqeT7c81;{So6<pt4@Qw~$^ia%=#;ZTY&kr5^3I3XtQU^NT5T$LM`LrGFVieY!&(56<#l!78?Wp)?kGr@xvl)j5FhiJyhH_mT>If21~e(#9gePKdg6u?O-AyNEo4SQBW+ZXrv-_9Q%a0v%k&=g|>ZkDg8N+(W|2xt-uRwPjm5YSZoc_el%!PMlXb%Z1iEB=~bsy_b?i)ofi=ua}!DVE?maXNP_MV>0-I2DQw;ePyJ>jp}%pgY#cO;^EG#)+GX?^Q2bQxai8MKo0azf(PTgr&@*VnxYOD04e4R6)ao+sF`o&oHb(%w)`9FT`#zz))lqXy7~G=EJ55r+WR_qDR}p+9nrc<g2a?R;E@pFYA<8zw=^((p_$Qr$T(tm4A}k4vsm!mHDP(O)wY>f6VgJAwri6lhWVH?XmKu<lY_d64`XRUTqpFKA#fSkyvpGJDY1MqU0S|ic;<bvaVNEHUMIg3=);cDa&F;aV$9f6pz$0aKS2I4)VvPMiNtx;n~c@1P+|Z_Op_JQI9#u6!fNSe=en9H7kr+L7EI$FH913p`ALF(FZPYn6%cRrb6Y#+TxgEd5PN#fRQtDAF<TqV3udAG=hb?PUF9=rE5flq&F*7FN^!wz6x9B)wbf~0a>g@T7A-P!NAM_X@{WJjckeS3Lp}N(D{(@<bhxq?Q8pKIH-$ZZ@pB-!=Z7xnN%ZTH>-OOcg={}mSn0mB9)A~Z$z$&TlS}pA2o-dgQfg?Ym1@{<zB_-DE*a0<x#_e=ng%yM-|aA7A?CJS{OI%U?OqT5LQHQfG2+p<6gz$d%YH8Jb$YndlAveu4-cI2>^lFG{4b$&|u?$_%LKUqi|IqqeB0&sNHtt4#RYqf7{`^riHE}9>*U}kHc4Qem>m_wDqkTGs;&*0KLvx^hNf%qI;NX9r&S_hvIvCt?|e_^?7AgsP9R@Y@2rP5l&W-zz3q5kM;kuSfNG7m{@DjK|n1GK?L<nK_-mQ;55y^tTkb;<}3`J<!iIP@S!$lqrH|54=og~_zZ+w9R?UtscJq9TJhCQPt@N!)#L7Y5BKRzQG7*KVY1=PWaJLXg7O{)^mulm?S_6)#>DhfuC`{MkWa{k>s2@$xXpD{mLV~$9W_;oqKccMdaQj0^}CIs<!fMI&(ixQBB^<2r2mpHyd9$CFeGhVx>W~{HzJhVVVvqHNME>f;Pv?}bb4<@Gr)gX$U$)U61=+z75ky&jvoh=joIbl%%jv;gcHo6Z4)jfjF%~!g%8JB9>|U;7^Dh+*ge=id+pSAhO>-QhZc;+W}C*ra#bbGO|PK~sk+u*>WzTaFM!k5XZ;GuXw6}j(s16!=?($uNRvD;c)$J}Je(gndh$RW6Z@)xo<h<jyQ^Q6EB+*!R#~P$RrKT|0EYu>^xi41_6N>`iKmw})cq$x)br>k+OFT)fSv%flO9ik`a5MtUjBxOE`2`Ys{^l-sE{;w6l;~OVmhYW83!@ub~PC54oOD7>?(jD#mn{5wAU-A-xSHc0F&p_wPv(MtUF`#`r^(T)i>G-Zdoy~Nt7?#jc)>vSXVhOM;ssJ`2VPRx~&cq0`MLAmQ_6L4xXbk=4h^8r#AfUpe{y@?r(`!t|6Ll#~vFp-Q>IdUlsi}Axhdg7x7ih46hLI#0!Bk9gZVP(0ZY}ic${2hjD+TlIMQ(!ViWVrM$JHluwL9Zd4p{<87BV<BqdDz6IcMD?q8vg0v3p=;I?#IAGB{8e&BoH$BnDuQ7+dL`>`BMn+O|S*(+?=-$b@veQlX+W78!5BusGoY#)8eW~ZXeX#qF_L#MdESnNy=Jz`|#+1(0i*&UdZ)qb9fEL!hh2+I)G1?ncyUezE)#GHYhUkQy6u%A!O2c6jA$f~|6Chtv1FAo)bg-evJ?Ts^h06ReB(fWP;W9w-!sz)>mwVgCQjF%h?@?L&yOlKYdOR~|k8QUS(_VU?|2?I%a-V>e%6+gP_c2gg#pomBPjT$32-25mh_5?9_9YtNH#zP%lhYe@9JES%tkP>bl&4Z2S@3ED<K+CkUggPpP70wab}hA~&-c4%Ln@t!GI9XT7%eg1D;YUFInw&(WcNs)>-Oq92Gb-fB%@J{3zEqjchIB;%B_seB#F`+ca=la*;ir=i<;wyIaZHCx<wGpW+6YiRiUPOadj}Z&-CdyfeIzl4r#*W>j_s?r$e?*B4X+kf8|IvCuG#H1OrvBx@`k9?&ZE`?%ue3MC&nKsD5;h`YH`}W^(&1ScjE@rtJX8U|iniLoTrDg1aoAg?D*G{y3>FyN<7Vjd=3aAs4dnxRRs>ThVG!z^V&SLw~DgL3O<Y9WF|D_rPn_O(+3ik6G0)iv;;KMHJ2bC3kSYdjPk$`dzz~)q+^s5V%!{674HwZM{o{W{w6(t5#2|J)7a4_fW&03H(6bd-dDqwN*SV+3r@{W`xn^DHg*@RJGj1(=J9c&{!-xxo!A#Zd3ZYkLNTZFc8B9P&r+$=@6^iX#N+~d>9;fR?-1T2Kq3~kE*|&+aoEagGCJYd#kZU_8NdPSgeBY6a=r?TBVHY#_GMhEgAf}sk=3KvV|)EWEAZ-6bI#GtED6s+_KIvEi#Ze(@Y79m+j@IyCoF^FJv@xO&=phY+q^Xjan-P01LuqANqFDP)nuC4R<LfM!1<-Rj_;6XRpCNPtZtv2RiX;SU_DH9Vx5=ezR?~X;=1wC#90<4O@+}=A@?xNI)+XC!2cB29>0n$nTcAs9J>`8t#dTVfR7B(9n7HWU;HbAv<nf$ArmoBg#>lm9Hj`hW6w&wb+Ad_9l4kgU(x&%A1sGQ;W<o1`UgA7k(T^;0wC%9HmnjmQ)4o!N)p{@001tPw@WQX^>{rh?AOS2ROR;<f#+@trnMheMp86Y)4zmGqePiji8Y1Ay-{wru?;acAc_HyzS4RPgy`GWCGR6?Bk-4OX6Za<FSDKk_s%=k`67DlzXN-uWWDyRd#kdr*oAW^p%5G$84JHMO8I;H8sm=UBT9{vz!{!X(J<!!_KcMBSon;DlyCj8;2%tSw{77WMlmpt+=h_+AS+>yQSVMQ+Arc$EJ;{GR#cKOPNz#4^DA@p>uzr6WyGp^gp;*PU(Qj|NO^)icd6$&n?TI`~u99C4d8HN8io_Uv~IRm-e|*rn7d{fBzThclAjC?e`l4R<baHI9KYno1wS5`bKdge!Ak{0Yw9YSs5sbkC^gf1C01dnUy?GUwOvHs2DkpEr>-Ifh;0H?P@3nfZe9D6_lM|W58k^Hu2C`Gky<D^hT!#X}H)oa-$M8TCN($UZ|3eM>cOOwltNR#k}VRV?Uc1-P^pZqL<VcZ%=}^r<WhjPd=K<DI=F|t-S&l|MTg|<@x(}j_-Mm#Gy>Kkgjj3^`PBxSMpJuw~nWu1TzDs9#PH3Cz1D=3Hz`mZ@&BTW#b-Wdy7cqEoDJd<v4`=>H=O%|IX%GcDTW~qmmB;^odO~bh>6U2p!aLinGEfzlK*%1s-(yI7rRWm2Q%MB9uQ@7cw6u_tp_9Uwo&>R|!TvcDJECcaE{7pBVSgg2xUL`eugfeJ-4*tVrXgWAmcu|ARGQhtN4WzSwzx%DX<pWDzhkaCDYlHR5v+53bCwkc4VmRO?eyYRu~fY@a3t)y>NKlI{OJt#5b&#)LCtZVN#xHLhLzlb}|PS|t-n8bCc52Q(p98_%Op+f=_f;yHshvuIO<=p0SsazmH!U(?54P_ScP^6pqThj!X#PtsqxoQc~)M0_LJ?+e<gVe@5KjX04IDDmO#CCAYSw66WgN8|t!b>aI{1@d!?KK5o<u^=%XCuoGhl0vRC>|ur-^^VzZxAGNK^)VnmDoD66Qx_{bkSo{%l6=k)GvbqlXtshz$!3Amzp>c&w_7Z!s*J6o-kfny8})Fd{yc^K42imLj6W)?_8mDjsLxh3cCXWaJ$-i>p1e8!`0?~3C6lh4Gyc|(c)#M$`#59oQGz_W)#_{NHl7bC5QZA^H5e$59<8CQ%z{os^PO$SQy*2D>Tf&Qu6kt-(cNxF2>`&7Q?)z$<}|9skJXsjy6g<DvdtacN*4{9;ZGEh3&2wC+EIru7`+v1(AfzJw@lgZpf|%_)_Uk${<isOIEQcj*Ty_8MeA<6-^)YRnG_gjcykH)woT@B6>WiXK2f$xPr*C#KMOhuCB+GUjR^jQER5sSV710~2RbJB*mnpX6p{z8IAO|lJts3O^tb2d{IZA(x@S^pAAQV%w2X|V3o*&*yezSJ-#pEi5bRmfuvmWJV$K05OqSE;d3EA^l}zT_3VrfO7aW!u-EZh(j7mnk&Kz{xTFxoY4H`^=rGw&ex`OcVm#1Q2PwWOSkRR(~C+*2wpKIu1<L0*=W-*=Ro~&6@J-EWXX<6If@Op4E--ECb(%*sLB~dSNQ33U~8eTbXIf3c$2Vr`$XX>JtIxpAiWo-z}U9<81i3+X8D(b?X4YNZcD=Dm0S7l<UlV_x!tZM`mjA^EGYJ0BvtrpRxyz5$h=MI)%^#PSO5)H$@aSpEA0N%dw;yP!?C*j-UcjssC-@NYHF|VA<_m{_SLS?(~7fJa2<Ik@?{`>*GPs8J%KAfJuuB*<^Pr}RN4?mq=c5cDOO7FV3;dX$aY_93!dtQsSe4M!n=(k1LYH|9GyI2lHdk${9wS~ModF^elV%u{5s+DXlWJTq!DK<#x=mX(4lI=-9fA+uVo(F9')

# Initialise public package names after loading dependent modules.
exec(compile(_zlib.decompress(_base64.b85decode('c-nPP%W4BL47?ls4<hHKf6!AQkZ&l(sE)ib@mfZ968iVqm%ST8eVfrpo*5@Rzz6stu@tbFEuN_ZdqF9=gMniqixRj4p-H2an^!DH=li;NWEo|-e9dgtQ0#rAs-Zi@VsgSb9_}fUU?Jns`ryl-Ny5$t+KpBw*K?lhsZ&h1$zB>gq0r<F&*s5${bjytrIj%lf-&$3-&(==4zCsu-AXT~8eALL@LWWLTOW;DYH4tnvT^^0eOJ`XZL&t(eYZ<Gu|HZp0l<NfEd')).decode("utf-8"), "<embedded wi_forecast/__init__.py>", "exec"), _PACKAGE.__dict__)


# ---- Original Streamlit UI (unchanged) ----
"""Water-injection forecast — deterministic AWPB profiles.

Replaces WI_profiles_gen_v7.2.py plus the Spotfire layer that sat downstream of it.
Run with:  streamlit run app.py
"""

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
