# python3 voz.py <resultado_heygen.txt> <tfNN>  -> voz-tfNN.wav + voz-tfNN.json (sin caracteres); aplica reemplazos de subtítulo
import sys,json,urllib.request
REEMP={"espái":"SPY"}
d=json.loads(open(sys.argv[1]).read())
if isinstance(d,list): d=json.loads(d[0]["text"])
for w in d["original_words"]:
    for a,b in REEMP.items(): w["text"]=w["text"].replace(a,b)
n=sys.argv[2]; json.dump({"duration":d["duration"],"original_words":d["original_words"]},open(f"voz-{n}.json","w"),ensure_ascii=False)
open(f"voz-{n}.wav","wb").write(urllib.request.urlopen(d["audio_url"]).read()); print(n,d["duration"],len(d["original_words"]),"palabras")
