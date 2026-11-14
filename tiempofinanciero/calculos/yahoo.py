"""Helper comun de los calculos tf-25 a tf-34. Baja precios diarios de Yahoo Finance
(period1/period2, nunca range=max) y da utilidades. Fecha del calculo: 2026-11-14,
ultimo cierre usado: 2026-11-13. Cache en la carpeta temporal del sistema para que el revisor
pueda repetir la cuenta con los mismos datos (borrar la carpeta para bajar de nuevo)."""
import json, os, time, calendar, tempfile, urllib.request
from datetime import date, datetime, timezone

HOY = date(2026, 11, 14)
FIN = date(2026, 11, 13)          # ultimo cierre
CACHE = os.path.join(tempfile.gettempdir(), "tf_cache_yahoo")   # fuera del repo

def _unix(d):
    return calendar.timegm(d.timetuple())

def serie(simbolo, desde, hasta=HOY):
    """Lista de (fecha, close, adjclose) diarios. close ya viene ajustado por splits;
    adjclose ademas por dividendos (equivale a reinvertirlos)."""
    os.makedirs(CACHE, exist_ok=True)
    f = os.path.join(CACHE, f"{simbolo}_{desde}_{hasta}.json")
    if os.path.exists(f):
        d = json.load(open(f))
    else:
        u = (f"https://query1.finance.yahoo.com/v8/finance/chart/{simbolo}"
             f"?period1={_unix(desde)}&period2={_unix(hasta)+86400}&interval=1d&events=div")
        for i in range(4):
            try:
                r = urllib.request.urlopen(urllib.request.Request(u, headers={"User-Agent": "Mozilla/5.0"}), timeout=60)
                d = json.load(r)
                break
            except Exception as e:
                if i == 3: raise
                time.sleep(3)
        json.dump(d, open(f, "w"))
    res = d["chart"]["result"][0]
    ts = res["timestamp"]
    cl = res["indicators"]["quote"][0]["close"]
    ad = res["indicators"]["adjclose"][0]["adjclose"]
    out = []
    for t, c, a in zip(ts, cl, ad):
        if c is None or a is None: continue
        dia = datetime.fromtimestamp(t, timezone.utc).date()
        if dia > FIN: continue
        out.append((dia, c, a))
    return out

def hace(anios, ref=HOY):
    return date(ref.year - anios, ref.month, ref.day)

def en_o_antes(s, d):
    """Ultima fila con fecha <= d."""
    r = [x for x in s if x[0] <= d]
    return r[-1]

def desde_fecha(s, d):
    """Recorta la serie desde el ultimo cierre <= d (inclusive)."""
    ini = en_o_antes(s, d)[0]
    return [x for x in s if x[0] >= ini]

def peor_caida(fechas, valores):
    """Maxima caida de pico a piso: (caida, fecha_pico, fecha_piso)."""
    pico, fp, peor = valores[0], fechas[0], (0.0, fechas[0], fechas[0])
    for f, v in zip(fechas, valores):
        if v > pico: pico, fp = v, f
        c = v / pico - 1
        if c < peor[0]: peor = (c, fp, f)
    return peor

def anual(fechas, valores, mes=11, dia=14):
    """Valor en cada aniversario (ultimo cierre <= dia/mes de cada anio) + ultimo cierre."""
    out = []
    for y in range(fechas[0].year, fechas[-1].year + 1):
        lim = date(y, mes, dia)
        prev = [(f, v) for f, v in zip(fechas, valores) if f <= lim]
        if prev and prev[-1][0] >= fechas[0]:
            out.append((y, prev[-1][1]))
    return out

def cagr(v0, v1, anios):
    return (v1 / v0) ** (1 / anios) - 1

def usd(x):
    return f"US$ {x:,.0f}".replace(",", ".")
