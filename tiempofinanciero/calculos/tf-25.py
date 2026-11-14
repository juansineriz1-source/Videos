"""tf-25 El costo de esperar: US$ 100 por mes en SPY desde 1996 (30 anios) vs desde 2006 (20 anios).
Aporte el primer dia habil de cada mes, dividendos reinvertidos (adjclose), valuado al 2026-11-13.
Sin comisiones ni impuestos. Misma metodologia que tf-02."""
from datetime import date
from yahoo import *

s = serie("SPY", date(1996, 10, 1))

def plan(anio_ini, mes_ini=11, aporte=100.0):
    cuotas, puesto, visto = 0.0, 0.0, set()
    fechas, valores, puestos = [], [], []
    for f, c, a in s:
        if (f.year, f.month) < (anio_ini, mes_ini): continue
        if (f.year, f.month) not in visto and (f.year, f.month) <= (2026, 10):
            visto.add((f.year, f.month)); cuotas += aporte / a; puesto += aporte
        fechas.append(f); valores.append(cuotas * a); puestos.append(puesto)
    return fechas, valores, puestos, len(visto)

for ini in (1996, 2006, 2016):
    f, v, p, n = plan(ini)
    print(f"Desde nov-{ini}: {n} aportes, puesto {usd(p[-1])}, valor {usd(v[-1])} (x{v[-1]/p[-1]:.2f})")
    # peor momento: valor contra lo puesto
    peor = min(zip(f, v, p), key=lambda x: x[1] / x[2] - 1)
    print(f"   peor contra lo puesto: {peor[0]} puesto {usd(peor[2])} valia {usd(peor[1])} ({peor[1]/peor[2]-1:+.1%})")
    pc = peor_caida(f, v)
    print(f"   (caida de pico a piso del valor, con aportes: {pc[0]:+.1%} {pc[1]} -> {pc[2]})")
    print("   serie anual (nov):", [(y, round(x)) for y, x in anual(f, v)])
f30, v30, p30, _ = plan(1996); f20, v20, p20, _ = plan(2006)
print(f"Diferencia 30 vs 20 anios: {usd(v30[-1]-v20[-1])}; aportes de mas: {usd(p30[-1]-p20[-1])}; ratio {v30[-1]/v20[-1]:.2f}")
# cuanto valen hoy solo los primeros 10 anios de aportes (120 cuotas 1996-2006)
cu = 0; visto=set()
for f, c, a in s:
    if (1996,11) <= (f.year,f.month) <= (2006,10) and (f.year,f.month) not in visto:
        visto.add((f.year,f.month)); cu += 100/a
print(f"Los primeros 120 aportes (nov-1996 a oct-2006, US$ 12.000) valen hoy {usd(cu*s[-1][2])}")
# el que empezo en 1996: cuanto tenia en nov-2006 y en el piso de 2009
for d in (date(2006,11,14), date(2009,3,9)):
    i = max(k for k, x in enumerate(f30) if x <= d)
    print(f"   plan 1996 al {f30[i]}: puesto {usd(p30[i])}, valor {usd(v30[i])}")
