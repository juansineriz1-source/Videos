"""tf-32 (versión revisada): canasta de 5 empresas argentinas que cotizan en Nueva York (GGAL, YPF, PAM, BMA, TGS),
US$ 200 en cada una el 2011-11-14, sin rebalancear, con dividendos (precio ajustado de Yahoo), contra SPY.
Revisión financiera 2026-11-14: reemplaza ARGT, que incluye MercadoLibre y otras no argentinas."""
import json, urllib.request, pandas as pd
def serie(t):
    u=f"https://query1.finance.yahoo.com/v8/finance/chart/{t}?period1=1320000000&period2=1900000000&interval=1d"
    r=json.loads(urllib.request.urlopen(urllib.request.Request(u,headers={"User-Agent":"Mozilla/5.0"}),timeout=30).read())["chart"]["result"][0]
    return pd.Series(r["indicators"]["adjclose"][0]["adjclose"],index=pd.to_datetime(r["timestamp"],unit="s").normalize())
A=pd.DataFrame({t:serie(t) for t in ["GGAL","YPF","PAM","BMA","TGS"]}).ffill(); A=A[A.index>="2011-11-14"]
arg=(A/A.iloc[0]).mean(axis=1)*1000
s=serie("SPY"); s=s[s.index>="2011-11-14"]; spy=s/s.iloc[0]*1000
print("ARG5 hoy",round(arg.iloc[-1]),"SPY",round(spy.iloc[-1]),arg.index[-1].date())
print("noviembre de cada año:",[(y,round(arg[(arg.index.year==y)&(arg.index.month>=11)].iloc[0])) for y in range(2011,2027)])
dd=arg/arg.cummax()-1; print("peor caída",round(dd.min()*100),"%", arg[:dd.idxmin()].idxmax().date(),"->",dd.idxmin().date())
d=(spy/spy.cummax()-1); print("peor SPY",round(d.min()*100))
print("PASO 2019-08-09 -> 08-12:",round((arg["2019-08-12"]/arg["2019-08-09"]-1)*100),"%")
c=arg.resample("YE").last(); print("año calendario:",{y.year:round(v) for y,v in (c.pct_change()*100).dropna().items()})
print("2026 en el año:",round((arg.iloc[-1]/arg["2025-12-31":].iloc[0]-1)*100),"%")
