import json,sys
# uso: numerar.py in.json out.json "diez por ciento=10%" ...
d=json.load(open(sys.argv[1])); w=d['original_words']
reps=[(a.split(),b) for a,b in (x.split('=') for x in sys.argv[3:])]
out=[];i=0;used=[]
while i<len(w):
    for seq,rep in reps:
        n=len(seq)
        if [x['text'].lower().strip('.,') for x in w[i:i+n]]==[s.lower() for s in seq]:
            out.append({'text':rep,'start_time':w[i]['start_time'],'end_time':w[i+n-1]['end_time']}); i+=n; used.append(rep); break
    else:
        out.append(w[i]); i+=1
d['original_words']=out; json.dump(d,open(sys.argv[2],'w'),ensure_ascii=False)
print(' '.join(x['text'] for x in out)); print('usados',used)
