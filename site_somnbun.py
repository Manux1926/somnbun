from build import AFF_NOTE

JS = r"""
(function(){
function $(s){return document.querySelector(s)}
var c=$('#calc');if(!c)return;
var H=['H1 (foarte moale)','H2 (moale – medie)','H3 (medie – fermă)','H4 (fermă)','H5 (foarte fermă)'];
function lvl(w,poz){var l=w<60?1:w<=90?2:w<=110?3:3.6;if(poz==='lateral')l-=0.5;if(poz==='burta')l+=0.5;return Math.max(0,Math.min(4,Math.round(l)))}
function run(){var w=+$('#w').value||0,poz=$('#poz').value,cald=$('#cald').checked,dur=$('#dur').value,part=$('#part').checked,w2=+$('#w2').value||0,dim=$('#dim').value;
 var l=lvl(w,poz),tip,why=[];
 if(cald){tip='Arcuri independente (pocket) sau hibrid';why.push('Transpiri noaptea: arcurile lasă aerul să circule, spuma memory clasică ține mai cald.')}
 else if(poz==='lateral'){tip='Spumă cu memorie sau hibrid cu strat de confort gros';why.push('Dormi pe o parte: umerii și șoldurile au nevoie să se afunde puțin.')}
 else if(poz==='burta'){tip='Latex sau arcuri independente, ferme';why.push('Dormi pe burtă: o saltea fermă ține coloana dreaptă.')}
 else{tip='Hibrid sau spumă HR de densitate mare';why.push('Dormi pe spate: suport uniform pentru zona lombară.')}
 if(dur==='lomb')why.push('Durerile lombare: evită salteaua prea moale, în care se afundă bazinul. Dacă durerea persistă, discută cu un medic.');
 if(dur==='umeri')why.push('Dureri de umeri: un strat de confort mai moale (5–7 cm) la suprafață ajută.');
 var dual='';if(part&&Math.abs(w-w2)>=25){var l2=lvl(w2,poz);dual='Între voi e o diferență mare de greutate: alegeți o saltea cu arcuri independente, două saltele separate sau un model cu duritate diferită pe cele două jumătăți (pentru partener: '+H[l2]+').';}
 $('#rH').textContent=H[l];$('#rTip').textContent=tip;$('#rWhy').innerHTML=why.map(function(x){return '<li>'+x+'</li>'}).join('')+(dual?'<li>'+dual+'</li>':'');
 $('#rDim').textContent=dim;
}
c.addEventListener('input',run);c.addEventListener('change',run);run();
})();
"""

TOOL = """<div class="tool"><form id="calc" onsubmit="return false"><h2>Ce saltea ți se potrivește? Test în 1 minut</h2>
<div class="grid3">
<div><label class="f" for="w">Greutatea ta (kg)</label><input id="w" type="number" min="30" max="200" value="80"></div>
<div><label class="f" for="poz">Cum dormi cel mai des</label><select id="poz"><option value="spate">Pe spate</option><option value="lateral" selected>Pe o parte</option><option value="burta">Pe burtă</option><option value="mixt">Schimb des poziția</option></select></div>
<div><label class="f" for="dur">Dureri la trezire</label><select id="dur"><option value="nu">Nu</option><option value="lomb">Zona lombară</option><option value="umeri">Umeri / șolduri</option></select></div>
<div><label class="f" for="dim">Dimensiunea patului</label><select id="dim"><option>90 × 200 cm</option><option>140 × 200 cm</option><option selected>160 × 200 cm</option><option>180 × 200 cm</option><option>200 × 200 cm</option></select></div>
<div><label class="f" for="w2">Greutatea partenerului (kg)</label><input id="w2" type="number" min="0" max="200" value="60"></div>
</div>
<label class="chk"><input type="checkbox" id="part" checked> Dorm cu partenerul</label>
<label class="chk"><input type="checkbox" id="cald"> Transpir sau mi-e cald noaptea</label>
<div class="res"><div class="big"><div class="kpi main"><span>Duritate recomandată</span><b id="rH">–</b></div><div class="kpi"><span>Tip de saltea</span><b id="rTip" style="font-size:19px">–</b></div><div class="kpi"><span>Dimensiune</span><b id="rDim">–</b></div></div>
<ul id="rWhy" style="margin-top:12px"></ul>
<p class="note">Scara H diferă puțin între producători. Folosește perioada de probă oferită de mulți vânzători (adesea 30–100 de nopți) și verifică condițiile de retur înainte de cumpărare.</p></div></form></div>"""

TYPES = """<div class="tw"><table class="t"><tr><th>Tip</th><th>Senzație</th><th>Plus</th><th>Minus</th></tr>
<tr><td>Spumă cu memorie</td><td>Te „îmbrățișează”</td><td>Reduce presiunea pe umeri și șolduri; nu transmite mișcarea partenerului</td><td>Poate ține cald</td></tr>
<tr><td>Spumă HR (high resilience)</td><td>Elastică</td><td>Raport bun calitate-preț; revine repede</td><td>Calitatea depinde mult de densitate</td></tr>
<tr><td>Arcuri independente (pocket)</td><td>Elastică, aerisită</td><td>Ventilație bună; susținere punctuală</td><td>Mai grea</td></tr>
<tr><td>Latex</td><td>Elastică, fermă</td><td>Durabilă, ventilată</td><td>Scumpă și grea</td></tr>
<tr><td>Hibrid (arcuri + spumă)</td><td>Echilibrată</td><td>Combină suportul arcurilor cu confortul spumei</td><td>Preț mai mare</td></tr></table></div>"""

INDEX_BODY = TOOL + """
<section class="sec"><h2>Cum alegi salteaua în 3 pași</h2><ol><li><strong>Duritatea</strong>, după greutate și poziția de somn: cine doarme pe o parte are nevoie de o saltea puțin mai moale; cine doarme pe burtă, de una mai fermă.</li><li><strong>Tipul</strong>: spumă, arcuri, latex sau hibrid, după cât de cald îți e și cât te deranjează mișcările partenerului.</li><li><strong>Dimensiunea și înălțimea</strong>: salteaua trebuie să fie cu cel puțin 15–20 cm mai lungă decât cel mai înalt dintre voi.</li></ol>
<h2>Tipurile de saltele, pe scurt</h2>""" + TYPES + AFF_NOTE + """</section>
<section class="sec"><h2>Ghiduri</h2><div class="cards">
<a class="c" href="/tipuri-de-saltele.html"><span class="tag">Comparație</span><b>Memory, arcuri, latex sau hibrid?</b><span>Ce tip de saltea alegi.</span></a>
<a class="c" href="/duritate-saltea-h2-h3-h4.html"><span class="tag">Ghid</span><b>Duritatea H2, H3, H4</b><span>Ce înseamnă și ce alegi după greutate.</span></a>
<a class="c" href="/cand-schimbi-salteaua.html"><span class="tag">Sfaturi</span><b>Când schimbi salteaua</b><span>7 semne și cum o faci să țină mai mult.</span></a></div></section>"""

FAQ = [
    ('Ce duritate de saltea pentru 80 kg?', 'De obicei H3 (medie–fermă). Dacă dormi pe o parte, o saltea între H2 și H3 sau un strat de confort mai moale; dacă dormi pe burtă, H3 spre H4.'),
    ('Salteaua cu memorie e bună pentru dureri de spate?', 'Poate ajuta prin reducerea presiunii, dar contează mai mult duritatea potrivită greutății tale decât materialul. O saltea prea moale, în care se afundă bazinul, poate agrava durerile lombare. Pentru dureri persistente, consultă un medic.'),
    ('Cât costă o saltea bună?', 'Pentru un pat dublu, saltelele de calitate medie pornesc de la câteva sute de lei la spumă și ajung la câteva mii de lei la hibrid și latex. Mai important decât prețul sunt densitatea spumei, garanția și perioada de probă.'),
]

ART_TIP = """<p>Fiecare material de saltea are o „personalitate”. Alegerea potrivită depinde de cum dormi, cât de cald îți e și dacă dormi singur.</p>""" + TYPES + """
<h2>Spuma cu memorie</h2><p>Se modelează după corp sub efectul căldurii și al greutății. Este preferata celor care dorm pe o parte și a cuplurilor, pentru că nu transmite mișcarea. Caută variante cu spumă ventilată sau cu gel dacă îți e cald.</p>
<h2>Spuma HR</h2><p>Spuma de înaltă reziliență are celule deschise și revine repede. Cifra care contează este <strong>densitatea</strong> (kg/m³): o densitate mai mare înseamnă de obicei durabilitate mai bună.</p>
<h2>Arcurile independente</h2><p>Fiecare arc este într-un buzunar textil și lucrează separat, spre deosebire de arcurile bonell, legate între ele. Aerisire foarte bună, susținere pe zone (de obicei 5–7 zone).</p>
<h2>Latexul</h2><p>Natural sau sintetic, elastic și foarte durabil. Bun pentru cei care vor o saltea fermă și aerisită. Este printre cele mai scumpe.</p>
<h2>Hibridul</h2><p>Arcuri independente la bază și straturi de spumă sau latex deasupra. Pentru mulți, cel mai bun compromis.</p>
<div class="box info">Nu știi ce să alegi? Fă <a href="/">testul de un minut</a>.</div>"""

ART_H = """<p>Majoritatea magazinelor din România folosesc o scară de duritate de la H1 la H5. Nu există un standard unic între producători, dar reperele de mai jos funcționează în practică.</p>
<div class="tw"><table class="t"><tr><th>Duritate</th><th>Senzație</th><th>Orientativ pentru</th></tr>
<tr><td>H1</td><td>Foarte moale</td><td>Copii, persoane foarte ușoare</td></tr><tr><td>H2</td><td>Moale – medie</td><td>Sub ~60 kg sau cei care dorm pe o parte</td></tr>
<tr><td>H3</td><td>Medie – fermă</td><td>~60–90 kg, cea mai vândută</td></tr><tr><td>H4</td><td>Fermă</td><td>Peste ~90 kg sau cei care dorm pe burtă</td></tr><tr><td>H5</td><td>Foarte fermă</td><td>Peste ~120 kg</td></tr></table></div>
<h2>Poziția contează la fel de mult ca greutatea</h2><ul><li><strong>Pe o parte:</strong> umerii și șoldurile trebuie să se afunde, altfel coloana se curbează. Coboară cu o treaptă.</li><li><strong>Pe spate:</strong> treapta după greutate.</li><li><strong>Pe burtă:</strong> urcă o treaptă, ca bazinul să nu se afunde.</li></ul>
<h2>Saltele cu două fețe și cu duritate dublă</h2><p>Unele saltele au o față H2 și una H3, iar altele au duritate diferită pe cele două jumătăți, pentru cupluri cu greutăți foarte diferite.</p>
<h2>Testul de acasă</h2><p>Întinde-te pe o parte. Cineva să se uite dacă coloana ta este aproximativ dreaptă. Dacă șoldul se afundă mult, salteaua e prea moale; dacă umărul e strivit și talia „atârnă”, e prea tare.</p>"""

ART_CAND = """<p>O saltea bună ține de obicei 7–10 ani, în funcție de material, de greutate și de cum o întreții. Iată semnele că a venit momentul.</p>
<h2>7 semne</h2><ol><li>Te trezești cu dureri care trec după ce te miști puțin.</li><li>Dormi mai bine la hotel sau în altă parte.</li><li>Vezi adâncituri sau o „groapă” în locul unde dormi.</li><li>Auzi arcurile sau le simți prin material.</li><li>Alergiile se agravează dimineața (praf și acarieni).</li><li>Simți fiecare mișcare a partenerului.</li><li>Salteaua are peste 8–10 ani.</li></ol>
<h2>Cum o faci să țină mai mult</h2><ul><li><strong>Întoarce-o</strong> cap-coadă la fiecare 3 luni (și pe cealaltă față, dacă e reversibilă).</li><li><strong>Husă protectoare</strong> impermeabilă și respirabilă.</li><li><strong>Somieră potrivită:</strong> lamelele prea rare sau rupte deformează salteaua și pot anula garanția.</li><li><strong>Aerisire:</strong> lasă patul desfăcut dimineața, ca umezeala să se evapore.</li></ul>
<h2>Ce faci cu salteaua veche</h2><p>Multe primării și operatori de salubritate colectează deșeurile voluminoase la anumite date, iar unii vânzători preiau salteaua veche la livrare. Întreabă înainte de comandă.</p>
<div class="box info">Gata de schimb? Află ce duritate și ce tip ți se potrivesc cu <a href="/">testul de un minut</a>.</div>""" + AFF_NOTE

SITE = {
    'name': 'SomnBun', 'domain': 'somnbun.online',
    'c1': '#3b3a8f', 'c2': '#6c63c7', 'accent': '#ffd27a',
    'mark': '<path d="M40 12a20 20 0 1 0 12 32A16 16 0 0 1 40 12z" fill="#fff"/><circle cx="44" cy="20" r="2.5" fill="#ffd27a"/><circle cx="50" cy="30" r="2" fill="#ffd27a"/>',
    'tagline': 'Ghiduri independente pentru a alege salteaua potrivită: duritate, materiale, dimensiuni și test gratuit.',
    'badges': ['Test saltea în 1 minut', 'Ghiduri fără jargon', 'Actualizat 2026'],
    'nav': [('/', 'Test saltea'), ('/tipuri-de-saltele.html', 'Tipuri'), ('/duritate-saltea-h2-h3-h4.html', 'Duritate'), ('/ghiduri.html', 'Ghiduri')],
    'main_tool': 'Test: ce saltea ți se potrivește',
    'side_title': 'Ce saltea ți se potrivește?', 'side_text': 'Duritate și tip, după greutate și poziția de somn.',
    'about': '<p>SomnBun este un site independent care te ajută să alegi salteaua potrivită, explicând diferențele dintre materiale și scările de duritate folosite în România.</p><p>Nu oferim sfaturi medicale. Pentru dureri persistente, consultă un medic. Unele linkuri către magazine pot fi de afiliere și sunt marcate.</p>',
    'js': JS,
    'pages': [
        {'slug': 'index', 'title': 'Ce saltea să aleg? Test de duritate și tip | SomnBun', 'kind': 'tool', 'short': 'Test saltea', 'appcat': 'LifestyleApplication',
         'desc': 'Află ce saltea ți se potrivește: duritate H2, H3 sau H4, tipul (memory, arcuri, latex, hibrid) și dimensiunea, după greutate și poziția de somn.',
         'h1': 'Ce saltea ți se potrivește? Test în 1 minut', 'toolname': 'Test alegere saltea',
         'lead': 'Greutatea, poziția în care dormi și cât de cald îți e: îți spunem duritatea și tipul de saltea potrivite.', 'body': INDEX_BODY, 'faq': FAQ},
        {'slug': 'tipuri-de-saltele', 'title': 'Saltea cu memorie, arcuri, latex sau hibrid? Comparație', 'kind': 'article', 'short': 'Tipuri de saltele',
         'desc': 'Comparația tipurilor de saltele: spumă cu memorie, spumă HR, arcuri independente, latex și hibrid. Avantaje, dezavantaje și pentru cine e fiecare.',
         'h1': 'Tipuri de saltele: ce material alegi', 'lead': 'Cinci tipuri de saltele, explicate simplu, cu plusuri și minusuri.', 'body': ART_TIP},
        {'slug': 'duritate-saltea-h2-h3-h4', 'title': 'Duritate saltea H2, H3, H4: ce alegi după greutate', 'kind': 'article', 'short': 'Duritatea H2, H3, H4',
         'desc': 'Ce înseamnă duritatea H1–H5 la saltele, ce alegi după greutate și poziția de somn și un test simplu de făcut acasă.',
         'h1': 'Duritatea saltelei: H2, H3 sau H4?', 'lead': 'Scara de duritate, explicată, cu tabel după greutate și poziție.', 'body': ART_H},
        {'slug': 'cand-schimbi-salteaua', 'title': 'Când schimbi salteaua: 7 semne și cum o întreții', 'kind': 'article', 'short': 'Când schimbi salteaua',
         'desc': 'Cât ține o saltea, cele 7 semne că trebuie schimbată, cum o întreții ca să dureze mai mult și ce faci cu salteaua veche.',
         'h1': 'Când e timpul să schimbi salteaua', 'lead': 'Semnele de uzură și obiceiurile care prelungesc viața saltelei.', 'body': ART_CAND},
    ]
}
