"""tf-32 Acciones argentinas en dolares vs SPY.
No hay en Yahoo una serie confiable del Merval ni del CCL historico (^MERV devuelve pocas filas),
asi que se usa el ETF ARGT (Global X MSCI Argentina, cotiza en dolares en Nueva York desde 2011-03-03).
OJO: ARGT NO es el Merval: sigue el indice MSCI All Argentina 25/50, que incluye empresas que
cotizan afuera (MercadoLibre pesa mucho). Periodo redondo: 15 anios, 2011-11-14 -> 2026-11-13.
Dividendos reinvertidos (adjclose). Sin comisiones ni impuestos."""
from datetime import date
from yahoo import *

N = 15
res = {}
for sym in ("ARGT", "SPY"):
    x = desde_fecha(serie(sym, date(2011, 3, 1)), hace(N))
    f = [a[0] for a in x]; v = [1000 * a[2] / x[0][2] for a in x]
    res[sym] = (f, v)
    pc = peor_caida(f, v)
    print(f"{sym} {f[0]} -> {f[-1]}: US$ 1.000 -> {usd(v[-1])} (x{v[-1]/1000:.2f}, {cagr(1000, v[-1], N):.1%} anual; solo precio x{x[-1][1]/x[0][1]:.2f})")
    print(f"   peor caida: {pc[0]:.1%} ({pc[1]} -> {pc[2]})")
    print("   serie anual:", [(y, round(a)) for y, a in anual(f, v)])
    # retorno por anio calendario
    yrs = {}
    for d, val in zip(f, v): yrs.setdefault(d.year, []).append(val)
    ks = sorted(yrs); print("   por anio calendario:", [(k, f"{yrs[k][-1]/(yrs[ks[i-1]][-1] if i else yrs[k][0])-1:+.0%}") for i, k in enumerate(ks)])
f, v = res["ARGT"]
for a, b in ((date(2017, 6, 1), date(2020, 12, 31)), (date(2019, 8, 1), date(2019, 8, 31))):
    sub = [(d, val) for d, val in zip(f, v) if a <= d <= b]
    c = peor_caida([d for d, _ in sub], [val for _, val in sub]); print(f"   ARGT caida {a} a {b}: {c[0]:.1%} ({c[1]} -> {c[2]})")
r = {d: val for d, val in zip(f, v)}
print(f"   ARGT 2019-08-09 -> 2019-08-12 (dia despues de las PASO): {r[date(2019,8,12)]/r[date(2019,8,9)]-1:.1%}")
# dias en que ARGT estuvo arriba / abajo del SPY (ambos desde 1.000)
fs, vs = res["SPY"]; rs = dict(zip(fs, vs))
com = [(d, r[d], rs[d]) for d in f if d in rs]
print(f"   ruedas con ARGT por encima del SPY: {sum(1 for _, a, b in com if a > b)} de {len(com)}")
# desde el lanzamiento del ETF (no redondo), como control
for sym in ("ARGT", "SPY"):
    x = [a for a in serie(sym, date(2011, 3, 1)) if a[0] >= date(2011, 3, 3)]
    print(f"   control desde 2011-03-03: {sym} x{x[-1][2]/x[0][2]:.2f}")
# control casero del 'Merval en dolares': GGAL e YPF ADR (cotizan en dolares en NY), 20 anios
for sym in ("GGAL", "YPF"):
    x = desde_fecha(serie(sym, date(2006, 11, 1)), hace(20))
    print(f"   control 20 anios {sym} (ADR, con dividendos): x{x[-1][2]/x[0][2]:.2f}")
