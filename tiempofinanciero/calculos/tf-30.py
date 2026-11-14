"""tf-30 US$ 1.000 en Amazon en la salida a bolsa (1997-05-15).
Precio de la oferta inicial: US$ 18 por accion (solo para clientes de los bancos colocadores).
Primer cierre de mercado: US$ 23,50 (Yahoo: 0,0979 ajustado por splits 2x, 3x, 2x y 20x = 240).
Amazon nunca pago dividendos. Hasta 2026-11-13. Sin comisiones ni impuestos."""
from datetime import date
from yahoo import *

x = serie("AMZN", date(1997, 5, 1))
f = [a[0] for a in x]; p = [a[1] for a in x]
anios = (f[-1] - f[0]).days / 365.25
print(f"Primer cierre {f[0]}: {p[0]:.6f} ajustado = US$ {p[0]*240:.2f} de la epoca. Ultimo {f[-1]}: US$ {p[-1]:.2f}. {anios:.1f} anios")
ipo = 18 / 240
print(f"  US$ 1.000 al primer cierre  -> {usd(1000 * p[-1] / p[0])} (x{p[-1]/p[0]:,.0f}, {cagr(p[0], p[-1], anios):.1%} anual)")
print(f"  US$ 1.000 al precio de oferta (US$ 18) -> {usd(1000 * p[-1] / ipo)} (x{p[-1]/ipo:,.0f})")
val = [1000 * a / p[0] for a in p]
pc = peor_caida(f, val)
i0, i1 = f.index(pc[1]), f.index(pc[2])
print(f"Peor caida: {pc[0]:.1%} ({pc[1]} {usd(val[i0])} -> {pc[2]} {usd(val[i1])})")
rec = next(d for d, v in zip(f[i1:], val[i1:]) if v >= val[i0])
print(f"  recupero el pico de {pc[1]} recien el {rec} ({(rec - pc[1]).days/365.25:.1f} anios)")
for a, b in ((date(2007, 6, 1), date(2009, 3, 1)), (date(2021, 6, 1), date(2023, 3, 1))):
    sub = [(d, v) for d, v in zip(f, val) if a <= d <= b]
    c = peor_caida([d for d, _ in sub], [v for _, v in sub]); print(f"   caida {a.year}-{b.year}: {c[0]:.1%} ({c[1]} -> {c[2]})")
print("serie anual (may-15):", [(y, round(a)) for y, a in anual(f, val, 5, 15)], "ultimo", round(val[-1]))
sp = [a for a in serie("SPY", date(1997, 5, 1)) if a[0] >= f[0]]
print(f"Comparacion: US$ 1.000 en SPY mismo periodo (con dividendos) -> {usd(1000 * sp[-1][2] / sp[0][2])}")
