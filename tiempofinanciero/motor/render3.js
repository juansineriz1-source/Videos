// node render3.js salida.(mp4|png) duracion cfgJSON [clipFondo] [segundoInicio]
const {chromium}=require('playwright');const {spawn}=require('child_process');
(async()=>{const [out,dur,cfg,bg,ss]=process.argv.slice(2);const fps=30,n=Math.round(+dur*fps),C=JSON.parse(cfg);
const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1920}});
await p.goto('file://'+require('path').resolve('g3.html'));await p.evaluate(()=>document.fonts.ready);
if(out.endsWith('.png')){await p.evaluate(([t,C])=>window.render(t,C),[+dur,C]);await p.screenshot({path:out,omitBackground:!!bg});await b.close();return}
let args;
if(bg){args=['-y','-v','error','-f','image2pipe','-framerate',String(fps),'-c:v','png','-i','-','-stream_loop','-1','-ss',ss||'0.5','-i',bg,'-filter_complex',
 `[1:v]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,setsar=1,fps=${fps},eq=saturation=0.85:contrast=1.05[b];[b][0:v]overlay=shortest=1[v]`,'-map','[v]','-t',String(dur),'-c:v','libx264','-preset','veryfast','-pix_fmt','yuv420p','-crf','16',out]}
else args=['-y','-v','error','-f','image2pipe','-framerate',String(fps),'-i','-','-c:v','libx264','-preset','veryfast','-pix_fmt','yuv420p','-crf','16',out];
const ff=spawn('ffmpeg',args,{stdio:['pipe','inherit','inherit']});
for(let k=0;k<n;k++){await p.evaluate(([t,C])=>window.render(t,C),[k/fps,C]);const buf=bg?await p.screenshot({type:'png',omitBackground:true}):await p.screenshot({type:'jpeg',quality:94});if(!ff.stdin.write(buf))await new Promise(r=>ff.stdin.once('drain',r))}
ff.stdin.end();await new Promise(r=>ff.on('close',r));await b.close()})();
