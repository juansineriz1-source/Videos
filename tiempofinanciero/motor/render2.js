const {chromium}=require('playwright');const {spawn}=require('child_process');
(async()=>{const [out,dur,cfg]=process.argv.slice(2);const fps=30,n=Math.round(+dur*fps),C=JSON.parse(cfg);
const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1920}});
await p.goto('file://'+require('path').resolve('g2.html'));await p.evaluate(()=>document.fonts.ready);
if(out.endsWith('.png')){await p.evaluate(([t,C])=>window.render(t,C),[+dur,C]);await p.screenshot({path:out});await b.close();return}
const ff=spawn('ffmpeg',['-y','-v','error','-f','image2pipe','-framerate',String(fps),'-i','-','-c:v','libx264','-preset','veryfast','-pix_fmt','yuv420p','-crf','16',out]);
for(let k=0;k<n;k++){await p.evaluate(([t,C])=>window.render(t,C),[k/fps,C]);ff.stdin.write(await p.screenshot({type:'jpeg',quality:93}))}
ff.stdin.end();await new Promise(r=>ff.on('close',r));await b.close()})();
