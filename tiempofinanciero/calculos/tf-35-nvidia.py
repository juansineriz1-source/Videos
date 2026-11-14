"""tf-35 Nvidia sin Jensen Huang. Cierres diarios de NVDA (Yahoo). Fecha del calculo: 2026-11-14."""
import json,urllib.request,datetime
u="https://query1.finance.yahoo.com/v8/finance/chart/NVDA?period1=1790000000&period2=1794700000&interval=1d"
d=json.loads(urllib.request.urlopen(urllib.request.Request(u,headers={"User-Agent":"Mozilla/5.0"})).read())["chart"]["result"][0]
s=[(datetime.datetime.fromtimestamp(a,datetime.timezone.utc).date().isoformat(),round(c,2)) for a,c in zip(d["timestamp"],d["indicators"]["quote"][0]["close"]) if c]
m=dict(s); print(s[-12:])
mx=max(s,key=lambda x:x[1]); print("maximo del periodo",mx)
for a,b in [("2026-11-03","2026-11-13"),("2026-11-06","2026-11-13"),("2026-11-11","2026-11-12"),(mx[0],"2026-11-13"),("2026-10-28","2026-11-13")]:
    if a in m: print(a,"->",b,m[a],m[b],f"{(m[b]/m[a]-1)*100:.1f} %")
