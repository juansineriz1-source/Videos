# Pixabay -> banco/extra/kd-NNN.mp4 (7 s, 1920x1080) + fila en indice-extra.csv. Uso: pxk.py pref "query" max
import os,json,urllib.request,urllib.parse,subprocess,csv,sys
K=os.environ["PIXABAY_API_KEY"]; pref,q,mx=sys.argv[1],sys.argv[2],int(sys.argv[3])
def get(u): return urllib.request.urlopen(urllib.request.Request(u,headers={"User-Agent":"Mozilla/5.0"}),timeout=180).read()
f='banco/extra/indice-extra.csv'; rows=list(csv.reader(open(f,encoding='utf-8-sig')))
ya={r[14] for r in rows if len(r)>14}; usados={r[2] for r in rows if len(r)>2}
n=max([int(r[2][len(pref)+1:-4]) for r in rows if len(r)>2 and r[2].startswith(pref+'-')]+[0])
d=json.loads(get(f"https://pixabay.com/api/videos/?key={K}&q={urllib.parse.quote(q)}&per_page=30"))
c=0
for h in d["hits"]:
    if c>=mx: break
    if h["pageURL"] in ya or h["duration"]<6: continue
    v=h["videos"]["large"]
    if not v.get("url") or v["width"]<v["height"] or v["width"]<1280: v=h["videos"]["medium"]
    if not v.get("url") or v["width"]<v["height"] or v["width"]<1280: continue
    open("../pxdl/src.mp4","wb").write(get(v["url"]))
    n+=1; k=f"{pref}-{n:03d}"; L=min(7,h["duration"]-0.8)
    r=subprocess.run(["ffmpeg","-v","0","-y","-ss","0.5","-i","../pxdl/src.mp4","-t",f"{L:.2f}","-an","-vf","scale=1920:1080:force_original_aspect_ratio=increase,crop=1920:1080,fps=30","-c:v","libx264","-preset","veryfast","-crf","19","-pix_fmt","yuv420p",f"banco/extra/{k}.mp4"])
    if r.returncode: n-=1; continue
    rows.append(['pixabay','extra',k+'.mp4',h["tags"],'si','no','Pixabay libre','0.5',f'{L+0.5:.1f}',f'{L:.1f}','1920x1080','horizontal','Pixabay · '+h["user"],q,h["pageURL"],''])
    c+=1; print(k,h["tags"][:80])
csv.writer(open(f,'w',encoding='utf-8-sig',newline='')).writerows(rows)
