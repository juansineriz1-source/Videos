import sys,subprocess,os
from PIL import Image,ImageDraw
v=sys.argv[1]; out=sys.argv[2]
d=float(subprocess.check_output(['ffprobe','-v','0','-show_entries','format=duration','-of','csv=p=0',v]))
n=20; W,H=216,384; im=Image.new('RGB',(10*W,2*(H+14)),'white'); dr=ImageDraw.Draw(im)
for i in range(n):
    t=0.8+i*(d-1.6)/(n-1); f=f'/tmp/claude-0/-home-user/06a9b3f8-5951-5dfa-bec5-6b0aa0c9f6e6/scratchpad/h{i}.jpg'
    subprocess.run(['ffmpeg','-v','error','-y','-ss',str(t),'-i',v,'-frames:v','1','-vf',f'scale={W}:{H}',f])
    x=(i%10)*W; y=(i//10)*(H+14); im.paste(Image.open(f),(x,y)); dr.text((x+3,y+H+1),f'{t:.1f}',fill='black')
im.save(out)
