"""tf-31 US$ 100 en el colchon 20 anios contra la inflacion de EE. UU.
CPI-U, todos los rubros, promedio de ciudades de EE. UU., sin desestacionalizar, base 1982-84=100 (BLS).
Fuentes: tabla historica del BLS (oct de cada anio) y comunicado del 2026-11-10 (oct-2026 = 337,511).
Oct-2025 NO fue publicado (cierre del gobierno de EE. UU.): se interpola entre sep y nov de 2025.
Ultimo dato disponible al 2026-11-14: octubre de 2026. Periodo: oct-2006 -> oct-2026 (20 anios)."""
from datetime import date
from yahoo import *

CPI_OCT = {2006: 201.8, 2007: 208.936, 2008: 216.573, 2009: 216.177, 2010: 218.711, 2011: 226.421,
           2012: 231.317, 2013: 233.546, 2014: 237.433, 2015: 237.838, 2016: 241.729, 2017: 246.663,
           2018: 252.885, 2019: 257.346, 2020: 260.388, 2021: 276.589, 2022: 298.012, 2023: 307.671,
           2024: 315.664, 2025: (324.800 + 324.122) / 2,   # interpolado: sep-2025 324,800 y nov-2025 324,122
           2026: 337.511}
c0, c1 = CPI_OCT[2006], CPI_OCT[2026]
print(f"Inflacion acumulada oct-2006 -> oct-2026: {c1/c0-1:.1%} ({cagr(c0, c1, 20):.2%} anual)")
print(f"US$ 100 de 2006 compran hoy lo que compraban US$ {100*c0/c1:.1f} (perdida de poder de compra {1-c0/c1:.1%})")
print(f"Para comprar lo mismo que con US$ 100 de 2006 hoy hacen falta US$ {100*c1/c0:.1f}")
print("serie anual poder de compra de US$ 100:", [(y, round(100 * c0 / c, 1)) for y, c in CPI_OCT.items()])
print("peores anios (inflacion oct a oct):", sorted(((y, round(CPI_OCT[y]/CPI_OCT[y-1]-1, 4)) for y in range(2007, 2027)), key=lambda t: -t[1])[:4])
print(f"  oct-2020 -> oct-2023: {CPI_OCT[2023]/CPI_OCT[2020]-1:.1%}")
# comparacion: US$ 100 en SPY, mismo tramo (2006-11-14 -> 2026-11-13), dividendos reinvertidos
x = desde_fecha(serie("SPY", date(2006, 10, 1)), hace(20))
v = 100 * x[-1][2] / x[0][2]
print(f"US$ 100 en SPY {x[0][0]} -> {x[-1][0]}: {usd(v)} nominales, US$ {v*c0/c1:.0f} en dolares de 2006")
pc = peor_caida([a[0] for a in x], [a[2] for a in x]); print(f"  peor caida SPY: {pc[0]:.1%} ({pc[1]} -> {pc[2]})")
