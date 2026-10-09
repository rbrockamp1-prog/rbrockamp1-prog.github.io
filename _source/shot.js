// usage: node shot.js url out.png [width] [height] [fullPage]
const {chromium}=require('/opt/npm-tools/node_modules/playwright');
(async()=>{const [,,url,out,w='1440',h='900',full='0',wait='2500']=process.argv;
const b=await chromium.launch();const {execFileSync}=require('child_process');const cache={};
const fonts=async(ctx)=>{await ctx.route(/fonts\.(googleapis|gstatic)\.com/,async r=>{const u=r.request().url();try{if(!cache[u])cache[u]=execFileSync('curl',['-sS','-A','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130 Safari/537.36',u]);await r.fulfill({body:cache[u],headers:{'access-control-allow-origin':'*','content-type':u.includes('googleapis')?'text/css':'font/woff2'}})}catch(e){await r.abort()}})};const p=await b.newPage({viewport:{width:+w,height:+h}});await fonts(p);
const errs=[];p.on('pageerror',e=>errs.push(e.message));p.on('console',m=>{if(m.type()==='error')errs.push(m.text())});
await p.goto(url,{waitUntil:'networkidle'}).catch(e=>errs.push('nav '+e.message));await p.waitForTimeout(+wait);
await p.screenshot({path:out,fullPage:full==='1'});console.log('errors:',JSON.stringify(errs));await b.close()})();
