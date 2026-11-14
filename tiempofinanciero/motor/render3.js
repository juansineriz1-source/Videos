// node render3.js salida.(mp4|png) duracion cfgJSON [clipFondo] [segundoInicio]
const {chromium}=require('playwright');const {spawn}=require('child_process');
(async()=>{const [out,dur,cfg,bg,ss]=process.argv.slice(2);const fps=30,n=Math.round(+dur*fps),C=JSON.parse(cfg);
const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1920}});
await p.goto('file://'+require('path').resolve('g3.html'));await p.evaluate(()=>document.fonts.ready);
if(out.endsWith('.png')){await p.evaluate(([t,C])=>window.render(t,C),[+dur,C]);await p.screenshot({path:out,omitBackground:!!bg});await b.close();return}
let args;const W=C.p.win;
if(bg&&W){args=['-y','-v','error','-f','image2pipe','-framerate',String(fps),'-c:v','png','-i','-','-stream_loop','-1','-ss',ss||'0.5','-i',bg,'-filter_complex',
 `[1:v]${W.crop?'crop='+W.crop+',':''}scale=${W.w}:${W.h}:flags=lanczos,setsar=1,fps=${fps},scale=w='trunc(${W.w}*(1+0.05*t/${dur})/2)*2':h=-2:eval=frame:flags=lanczos,crop=${W.w}:${W.h},unsharp=5:5:0.5,eq=saturation=0.92:contrast=1.06[f];color=c=black:s=1080x1920:r=${fps}[c];[c][f]overlay=${W.x}:${W.y}:shortest=1[b];[b][0:v]overlay=shortest=1[v]`,'-map','[v]','-t',String(dur),'-c:v','libx264','-preset','veryfast','-pix_fmt','yuv420p','-crf','16',out]}
else if(bg){const cr=C.p.bgcrop?'crop='+C.p.bgcrop+',':'';args=['-y','-v','error','-f','image2pipe','-framerate',String(fps),'-c:v','png','-i','-','-stream_loop','-1','-ss',ss||'0.5','-i',bg,'-filter_complex',
 `[1:v]${cr}scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,setsar=1,fps=${fps},eq=saturation=0.85:contrast=1.05[b];[b][0:v]overlay=shortest=1[v]`,'-map','[v]','-t',String(dur),'-c:v','libx264','-preset','veryfast','-pix_fmt','yuv420p','-crf','16',out]}
else args=['-y','-v','error','-f','image2pipe','-framerate',String(fps),'-i','-','-c:v','libx264','-preset','veryfast','-pix_fmt','yuv420p','-crf','16',out];
const ff=spawn('ffmpeg',args,{stdio:['pipe','inherit','inherit']});
for(let k=0;k<n;k++){await p.evaluate(([t,C])=>window.render(t,C),[k/fps,C]);const buf=bg?await p.screenshot({type:'png',omitBackground:true}):await p.screenshot({type:'jpeg',quality:94});if(!ff.stdin.write(buf))await new Promise(r=>ff.stdin.once('drain',r))}
ff.stdin.end();await new Promise(r=>ff.on('close',r));await b.close()})();
