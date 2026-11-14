# python3 publicar_tf.py reel|story <clave NAS dentro de contenido/> <archivo caption|-> [now|AAAA-MM-DDTHH:MM hora BA] [thumb_ms]
import sys,json,os,urllib.request,datetime
src=open('/mnt/project-files/nas/presign.py').read().rsplit('\n',2)[0]; exec(src.replace('print(presign(sys.argv[1],sys.argv[2]))',''))
tipo,key,capf=sys.argv[1:4]; when=sys.argv[4] if len(sys.argv)>4 else "now"; th=int(sys.argv[5]) if len(sys.argv)>5 else None
url=presign("GET",key,604800); vid=key.endswith(".mp4")
a={"video":{"url":url}} if vid else {"image":{"url":url}}
if vid and th is not None: a["video"]["metadata"]={"thumbnailOffset":th}
i={"schedulingType":"automatic","channelId":"6af89cff62b70b94b0300c8e","text":"" if capf=="-" else open(capf).read().strip(),"assets":[a],
   "metadata":{"instagram":{"type":tipo,"shouldShareToFeed":tipo=="reel"}}}
if when=="now": i["mode"]="shareNow"
else: i.update(mode="customScheduled",dueAt=(datetime.datetime.fromisoformat(when)+datetime.timedelta(hours=3)).strftime("%Y-%m-%dT%H:%M:00.000Z"))
q='mutation($i:CreatePostInput!){ createPost(input:$i){ __typename ... on PostActionSuccess { post { id status dueAt } } ... on MutationError { message } } }'
req=urllib.request.Request("https://api.buffer.com",data=json.dumps({"query":q,"variables":{"i":i}}).encode(),headers={"Authorization":"Bearer "+os.environ["BUFFER_API_KEY"],"Content-Type":"application/json"})
try: print(urllib.request.urlopen(req).read().decode())
except Exception as e: print(e, getattr(e,'read',lambda:b'')().decode()[:500])
