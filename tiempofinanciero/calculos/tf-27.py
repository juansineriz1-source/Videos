"""tf-27 Perderse los 10 mejores dias del SPY en 20 anios.
US$ 10.000 el 2006-11-14, retornos diarios con dividendos (adjclose), hasta 2026-11-13.
'Perderse un dia' = ese dia el retorno es 0 (estabas afuera). Sin comisiones ni impuestos."""
from datetime import date
from yahoo import *

x = desde_fecha(serie("SPY", date(2006, 10, 1)), hace(20))
f = [a[0] for a in x]; p = [a[2] for a in x]
ret = [(f[i], p[i] / p[i-1] - 1) for i in range(1, len(p))]
print(f"Periodo {f[0]} -> {f[-1]}, {len(ret)} ruedas")
orden = sorted(ret, key=lambda r: -r[1])
def final(saltear):
    fuera = set(d for d, _ in orden[:saltear]); v = 10000.0
    for d, r in ret:
        if d not in fuera: v *= 1 + r
    return v
base = final(0)
for n in (0, 5, 10, 20, 30, 40):
    v = final(n)
    print(f"  sin los {n:>2} mejores dias: {usd(v)} (x{v/10000:.2f}, {cagr(10000, v, 20):.2%} anual, {v/base-1:+.0%} vs todo)")
print("10 mejores dias:"); [print(f"   {d} {r:+.2%}") for d, r in orden[:10]]
peores = sorted(ret, key=lambda r: r[1])[:10]
print("10 peores dias:"); [print(f"   {d} {r:+.2%}") for d, r in peores]
idx = {d: i for i, (d, _) in enumerate(ret)}
for vent in (5, 10):
    cerca = sum(1 for d, _ in orden[:10] if any(abs(idx[d] - idx[q]) <= vent for q, _ in peores))
    print(f"De los 10 mejores, {cerca} cayeron a {vent} ruedas o menos de uno de los 10 peores")
print("Mejores 10 por anio:", sorted(d.year for d, _ in orden[:10]))
# tambien: sin los 10 peores (para no engañar)
fuera = set(d for d, _ in peores); v = 10000.0
for d, r in ret:
    if d not in fuera: v *= 1 + r
print(f"  (sin los 10 PEORES dias: {usd(v)})")
val = [10000 * a / p[0] for a in p]
pc = peor_caida(f, val); print(f"Peor caida: {pc[0]:.1%} ({pc[1]} -> {pc[2]})")
# series anuales: todo vs sin los 10 mejores
fuera = set(d for d, _ in orden[:10]); v = 10000.0; sin = [10000.0]
for d, r in ret:
    if d not in fuera: v *= 1 + r
    sin.append(v)
print("serie anual todo:", [(y, round(a)) for y, a in anual(f, val)])
print("serie anual sin 10:", [(y, round(a)) for y, a in anual(f, sin)])
