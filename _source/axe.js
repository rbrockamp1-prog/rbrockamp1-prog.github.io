// usage: node axe.js base url1 url2 ...
const {chromium}=require('/opt/npm-tools/node_modules/playwright');const fs=require('fs');
const axe=fs.readFileSync(require.resolve('axe-core/axe.min.js'),'utf8');
(async()=>{const urls=process.argv.slice(2);const b=await chromium.launch();const {execFileSync}=require('child_process');const cache={};
const fonts=async(ctx)=>{await ctx.route(/fonts\.(googleapis|gstatic)\.com/,async r=>{const u=r.request().url();try{if(!cache[u])cache[u]=execFileSync('curl',['-sS','-A','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130 Safari/537.36',u]);await r.fulfill({body:cache[u],headers:{'access-control-allow-origin':'*','content-type':u.includes('googleapis')?'text/css':'font/woff2'}})}catch(e){await r.abort()}})};let total=0;
for(const u of urls){for(const vw of [1440,390]){const p=await b.newPage({viewport:{width:vw,height:900}});await fonts(p);await p.goto(u,{waitUntil:'networkidle'}).catch(()=>{});await p.waitForTimeout(2600);
await p.addScriptTag({content:axe});
const r=await p.evaluate(async()=>await axe.run(document,{runOnly:{type:'tag',values:['wcag2a','wcag2aa','wcag21a','wcag21aa','wcag22aa','best-practice']}}));
const v=r.violations;total+=v.length;if(v.length)console.log(u.split('/').slice(-2).join('/'),vw,v.map(x=>`\n  [${x.impact}] ${x.id}: ${x.help} (${x.nodes.length}) e.g. ${x.nodes.slice(0,3).map(n=>n.target.join(' ')+' :: '+(n.failureSummary||'').split('\n')[1]).join(' | ')}`).join(''));
await p.close()}}
console.log('TOTAL violations groups:',total);await b.close()})();
