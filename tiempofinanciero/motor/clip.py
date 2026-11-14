# Clips de stock de Pixabay. Uso:
#   python3 clip.py buscar "wall street"        -> lista id, duración, tamaño, tags (filtra IA/green screen)
#   python3 clip.py bajar 231177 204306 ...     -> baja a clips/<id>.mp4, guarda crédito en clips/cred.json y deja clips/<id>.jpg (cuadro vertical 9:16 para revisar)
import os,sys,json,urllib.request,urllib.parse,subprocess
K=os.environ["PIXABAY_API_KEY"]; os.makedirs("clips",exist_ok=True)
MALOS=("green screen","chroma","mockup","ai generated","greenscreen","template","covid","subscribe")
def get(u): return urllib.request.urlopen(urllib.request.Request(u,headers={"User-Agent":"Mozilla/5.0","Referer":"https://pixabay.com/"}),timeout=120).read()
def api(**p): return json.loads(get("https://pixabay.com/api/videos/?"+urllib.parse.urlencode({"key":K,"safesearch":"true",**p})))["hits"]
if sys.argv[1]=="buscar":
    for h in api(q=sys.argv[2],per_page=20):
        if any(b in h["tags"].lower() for b in MALOS): continue
        m=h["videos"]["medium"]; print(h["id"],f'{h["duration"]}s',f'{m["width"]}x{m["height"]}',h["tags"][:70])
else:
    cf="clips/cred.json"; cred=json.load(open(cf)) if os.path.exists(cf) else {}
    for i in sys.argv[2:]:
        h=api(id=i)[0]; v=h["videos"]; s=v["large"] if v.get("large",{}).get("url") and v["large"]["height"]<=1440 else v["medium"]
        p=f"clips/{i}.mp4"
        if not os.path.exists(p): open(p,"wb").write(get(s["url"]))
        cred[str(i)]=h["user"]; json.dump(cred,open(cf,"w"))
        subprocess.run(["ffmpeg","-y","-v","error","-ss",str(min(2,h["duration"]/2)),"-i",p,"-frames:v","1","-vf","scale=-2:640,crop=360:640",f"clips/{i}.jpg"])
        print(i,h["duration"],"s",h["user"],h["tags"][:60])
