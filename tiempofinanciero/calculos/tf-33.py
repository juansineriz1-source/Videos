"""tf-33 Oro (GLD) vs SPY, 20 anios: US$ 1.000 en cada uno el 2006-11-14, hasta 2026-11-13.
GLD = ETF respaldado por oro fisico (no paga dividendos; cobra 0,40 % anual, ya incluido en el precio).
SPY con dividendos reinvertidos (adjclose). Sin comisiones de compra ni impuestos."""
from datetime import date
from yahoo import *

N = 20
res = {}
for sym in ("GLD", "SPY"):
    x = desde_fecha(serie(sym, date(2006, 10, 1)), hace(N))
    f = [a[0] for a in x]; v = [1000 * a[2] / x[0][2] for a in x]
    res[sym] = (f, v)
    pc = peor_caida(f, v)
    print(f"{sym} {f[0]} -> {f[-1]}: US$ 1.000 -> {usd(v[-1])} (x{v[-1]/1000:.2f}, {cagr(1000, v[-1], N):.1%} anual)")
    print(f"   peor caida: {pc[0]:.1%} ({pc[1]} -> {pc[2]})")
    i1 = f.index(pc[2]); pico = v[f.index(pc[1])]
    rec = next((d for d, val in zip(f[i1:], v[i1:]) if val >= pico), None)
    print(f"   recupero el pico el {rec}" + (f" ({(rec - pc[1]).days/365.25:.1f} anios despues del pico)" if rec else ""))
    print("   serie anual:", [(y, round(a)) for y, a in anual(f, v)])
fg, vg = res["GLD"]; fs, vs = res["SPY"]; s = dict(zip(fs, vs))
com = [(d, a, s[d]) for d, a in zip(fg, vg) if d in s]
print(f"Ruedas con el oro por encima del SPY: {sum(1 for _, a, b in com if a > b)} de {len(com)} ({sum(1 for _, a, b in com if a > b)/len(com):.0%})")
ult = [d for d, a, b in com if a > b]; print(f"   ultima rueda con el oro arriba: {ult[-1] if ult else None}")
for d0 in (date(2009, 3, 9), date(2011, 9, 6), date(2015, 12, 17), date(2020, 3, 23)):
    a = en_o_antes(list(zip(fg, vg, vg)), d0); b = en_o_antes(list(zip(fs, vs, vs)), d0)
    print(f"   al {a[0]}: oro {usd(a[1])} | SPY {usd(b[1])}")
# en la crisis 2008: que hizo cada uno entre el pico y el piso del SPY
g = dict(zip(fg, vg))
print(f"   2007-10-09 -> 2009-03-09: SPY {s[date(2009,3,9)]/s[date(2007,10,9)]-1:.1%} | oro {g[date(2009,3,9)]/g[date(2007,10,9)]-1:+.1%}")
# ultimos 10 anios
for sym in ("GLD", "SPY"):
    x = desde_fecha(serie(sym, date(2006, 10, 1)), hace(10)); print(f"   ultimos 10 anios {sym}: x{x[-1][2]/x[0][2]:.2f}")
