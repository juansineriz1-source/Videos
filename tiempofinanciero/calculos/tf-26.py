"""tf-26 Regla del 72: anios para duplicar = 72 / tasa anual (%).
Se contrasta con el SPY real (dividendos reinvertidos, adjclose) de los ultimos 30 anios
y con la inflacion de EE. UU. (CPI-U, BLS). Sin comisiones ni impuestos."""
import math
from datetime import date
from yahoo import *

print("Regla vs exacto (ln2/ln(1+r)):")
for r in (1, 2, 3, 4, 6, 8, 10, 12, 24, 36):
    print(f"  {r:>2} %: regla {72/r:5.1f} anios | exacto {math.log(2)/math.log(1+r/100):5.1f}")

s = serie("SPY", date(1996, 10, 1))
for n in (10, 20, 30):
    x = desde_fecha(s, hace(n))
    r = cagr(x[0][2], x[-1][2], n)
    print(f"SPY {n} anios ({x[0][0]} -> {x[-1][0]}): x{x[-1][2]/x[0][2]:.2f}, {r:.2%} anual -> regla del 72: {72/(r*100):.1f} anios")
x = desde_fecha(s, hace(30))
f = [a[0] for a in x]; v = [a[2] / x[0][2] for a in x]
# cuando se duplico de verdad cada vez (primer cierre >= 2, 4, 8, 16 veces)
for m in (2, 4, 8, 16):
    hit = next((d for d, y in zip(f, v) if y >= m), None)
    print(f"  primera vez x{m}: {hit}" + (f" ({(hit - f[0]).days/365.25:.1f} anios desde el inicio)" if hit else ""))
# ultima vez que estuvo por debajo de x2 (duplicacion 'definitiva')
last_below = max(d for d, y in zip(f, v) if y < 2)
print(f"  ultima vez por debajo de x2: {last_below} ({(last_below - f[0]).days/365.25:.1f} anios)")
pc = peor_caida(f, v); print(f"  peor caida 30 anios: {pc[0]:.1%} ({pc[1]} -> {pc[2]})")
print("  serie anual (US$ 1.000 iniciales):", [(y, round(1000 * val)) for y, val in anual(f, v)])
# inflacion EE. UU.: CPI-U NSA oct-2006 201.8 -> oct-2026 337.511 (BLS)
c0, c1 = 201.8, 337.511
inf = cagr(c0, c1, 20)
print(f"CPI-U oct-2006 {c0} -> oct-2026 {c1}: {inf:.2%} anual -> los precios se duplican cada {72/(inf*100):.0f} anios (regla)")
print(f"Comision de 2 % anual: se come la mitad en {72/2:.0f} anios (regla)")
