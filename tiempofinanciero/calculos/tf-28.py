"""tf-28 Lo que se come una comision de 2 % anual en 30 anios.
US$ 10.000 en SPY el 1996-11-14 hasta 2026-11-13, dividendos reinvertidos (adjclose).
La comision se descuenta todos los dias sobre el saldo: factor (1-0,02)^(1/252) por rueda.
Sin otras comisiones ni impuestos. (El SPY ya tiene adentro su propio gasto de ~0,09 % anual.)"""
from datetime import date
from yahoo import *

x = desde_fecha(serie("SPY", date(1996, 10, 1)), hace(30))
f = [a[0] for a in x]; p = [a[2] for a in x]
print(f"Periodo {f[0]} -> {f[-1]}")
def con_comision(c):
    k = (1 - c) ** (1 / 252); v = [10000.0]
    for i in range(1, len(p)): v.append(v[-1] * p[i] / p[i-1] * k)
    return v
base = con_comision(0)
for c in (0, 0.005, 0.01, 0.02, 0.03):
    v = con_comision(c)
    print(f"  comision {c:.1%}: final {usd(v[-1])} ({cagr(10000, v[-1], 30):.2%} anual) | se fue en comision {usd(base[-1]-v[-1])} = {1-v[-1]/base[-1]:.0%} del resultado")
pc = peor_caida(f, base); print(f"Peor caida sin comision: {pc[0]:.1%} ({pc[1]} -> {pc[2]})")
print("serie anual sin comision:", [(y, round(a)) for y, a in anual(f, base)])
print("serie anual con 2 %:", [(y, round(a)) for y, a in anual(f, con_comision(0.02))])
# variante de control: cobrando 2 % una vez por anio sobre el saldo (30 cobros)
print(f"  control (2 % una vez por anio, 30 cobros): {usd(base[-1]*0.98**30)}")
