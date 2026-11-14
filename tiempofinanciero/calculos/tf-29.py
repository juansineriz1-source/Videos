"""tf-29 El primer iPhone o acciones de Apple.
El iPhone salio a la venta en EE. UU. el viernes 2007-06-29 a US$ 499 (4 GB) y US$ 599 (8 GB), con contrato.
Se compara con poner esa plata en AAPL al cierre de ese dia, dividendos reinvertidos (adjclose),
hasta 2026-11-13. Sin comisiones ni impuestos. La fecha no es redonda: es la del lanzamiento."""
from datetime import date
from yahoo import *

s = serie("AAPL", date(2007, 6, 1))
x = [a for a in s if a[0] >= date(2007, 6, 29)]
f = [a[0] for a in x]; p = [a[2] for a in x]
anios = (f[-1] - f[0]).days / 365.25
print(f"Compra {f[0]}: cierre ajustado por splits US$ {x[0][1]:.4f} (x28 = US$ {x[0][1]*28:.2f} de la epoca); adjclose {p[0]:.4f}")
print(f"Ultimo cierre {f[-1]}: US$ {p[-1]:.2f}. {anios:.1f} anios, x{p[-1]/p[0]:.1f} con dividendos, x{x[-1][1]/x[0][1]:.1f} sin; {cagr(p[0], p[-1], anios):.1%} anual")
for precio in (499, 599):
    print(f"  US$ {precio} -> {usd(precio * p[-1] / p[0])} con dividendos | {usd(precio * x[-1][1] / x[0][1])} sin reinvertir (solo precio)")
    print(f"     acciones de hoy: {precio / x[0][1]:.1f}")
val = [599 * a / p[0] for a in p]
pc = peor_caida(f, val); print(f"Peor caida: {pc[0]:.1%} ({pc[1]} -> {pc[2]}); los US$ 599 valian {usd(min(val))} el {f[val.index(min(val))]}")
# otras caidas grandes
for a, b in ((date(2012, 9, 1), date(2013, 12, 31)), (date(2018, 9, 1), date(2019, 3, 1)), (date(2021, 12, 1), date(2023, 3, 1)), (date(2024, 12, 1), date(2025, 12, 1))):
    sub = [(d, v) for d, v in zip(f, val) if a <= d <= b]
    c = peor_caida([d for d, _ in sub], [v for _, v in sub]); print(f"   caida {a.year}-{b.year}: {c[0]:.1%} ({c[1]} -> {c[2]})")
print("serie anual (jun-29 de cada anio):", [(y, round(a)) for y, a in anual(f, val, 6, 29)], "ultimo", round(val[-1]))
sp = [a for a in serie("SPY", date(2007, 6, 1)) if a[0] >= date(2007, 6, 29)]
print(f"Comparacion: US$ 599 en SPY mismo periodo -> {usd(599 * sp[-1][2] / sp[0][2])}")
