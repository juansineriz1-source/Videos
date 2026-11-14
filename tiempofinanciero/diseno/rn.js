// node rn.js salida.(mp4|png) duracion cfgJSON   (cfg: una escena {d,at,p} o lista [{d,p},...] para una muestra encadenada)
const {chromium}=require('playwright');const {spawn}=require('child_process');
(async()=>{const [out,dur,cfg]=process.argv.slice(2);const fps=30,C=JSON.parse(cfg);
const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1920}});
await p.goto('file://'+require('path').resolve(__dirname,'n1.html'));await p.evaluate(()=>document.fonts.ready);
if(out.endsWith('.png')){await p.evaluate(([t,C])=>window.render(t,C),[+dur,C]);await p.screenshot({path:out});await b.close();return}
const L=Array.isArray(C)?C:[Object.assign({d:+dur},C)];
const ff=spawn('ffmpeg',['-y','-v','error','-f','image2pipe','-framerate',String(fps),'-i','-','-c:v','libx264','-preset','veryfast','-pix_fmt','yuv420p','-crf','17',out],{stdio:['pipe','inherit','inherit']});
let t0=0;for(const c of L){c.at=c.at||{};c.t0=t0;const n=Math.round(c.d*fps);for(let k=0;k<n;k++){await p.evaluate(([t,C])=>window.render(t,C),[k/fps,c]);const buf=await p.screenshot({type:'jpeg',quality:94});if(!ff.stdin.write(buf))await new Promise(r=>ff.stdin.once('drain',r))}t0+=c.d}
ff.stdin.end();await new Promise(r=>ff.on('close',r));await b.close()})();
