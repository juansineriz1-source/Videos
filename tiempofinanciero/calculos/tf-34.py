"""tf-34 US$ 100 en bitcoin hace 10 anios: 2016-11-14 -> 2026-11-13 (BTC-USD de Yahoo, cierre diario UTC).
Bitcoin no paga dividendos. Sin comisiones, sin impuestos, sin costo de custodia."""
from datetime import date
from yahoo import *

N = 10
x = desde_fecha(serie("BTC-USD", date(2016, 10, 1)), hace(N))
f = [a[0] for a in x]; p = [a[1] for a in x]; v = [100 * a / p[0] for a in p]
print(f"BTC {f[0]} US$ {p[0]:,.0f} -> {f[-1]} US$ {p[-1]:,.0f}: US$ 100 -> {usd(v[-1])} (x{v[-1]/100:.1f}, {cagr(100, v[-1], N):.1%} anual)")
imax = v.index(max(v)); print(f"Maximo: {f[imax]} US$ {p[imax]:,.0f} -> los US$ 100 valian {usd(v[imax])}; hoy esta {v[-1]/v[imax]-1:.1%} abajo del maximo")
print("Caidas de pico a piso de mas de 50 % (en orden):")
pico, fp, piso, fpi, en = v[0], f[0], v[0], f[0], False
caidas = []
for d, val in zip(f, v):
    if val > pico:
        if en and piso / pico - 1 <= -0.5: caidas.append((fp, pico, fpi, piso))
        pico, fp, piso, fpi, en = val, d, val, d, False
    elif val < piso or not en:
        if val < piso or not en: piso, fpi, en = min(val, piso) if en else val, d if (not en or val < piso) else fpi, True
if en and piso / pico - 1 <= -0.5: caidas.append((fp, pico, fpi, piso))
for a, b, c, e in caidas:
    print(f"   {a} {usd(b)} (BTC US$ {b*p[0]/100:,.0f}) -> {c} {usd(e)} (BTC US$ {e*p[0]/100:,.0f}): {e/b-1:.1%}")
pc = peor_caida(f, v); print(f"Peor caida: {pc[0]:.1%} ({pc[1]} -> {pc[2]})")
print("serie anual (nov-14):", [(y, round(a)) for y, a in anual(f, v)], "ultimo", round(v[-1]))
sp = desde_fecha(serie("SPY", date(2016, 10, 1)), hace(N))
print(f"Comparacion: US$ 100 en SPY mismo periodo (con dividendos) -> {usd(100 * sp[-1][2] / sp[0][2])}")
# peores dias
r = sorted(((f[i], p[i]/p[i-1]-1) for i in range(1, len(p))), key=lambda t: t[1])[:3]; print("Peores dias:", [(str(d), f"{q:.1%}") for d, q in r])
