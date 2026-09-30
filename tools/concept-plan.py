import math, random
random.seed(7)
# Lot in feet. North line A-B horizontal (bearing N35°39'E). West (101' + 23.5') side on the left by Sir Francis Drake.
A=(0,0); B=(221.8,0); C=(188.6,118.7); D=(-18.6,123.3)
LOT=[A,B,C,D]
def xw(y): return A[0]+(D[0]-A[0])*y/D[1]          # west line x at depth y
def xe(y): return B[0]+(C[0]-B[0])*y/C[1]          # east line x at depth y
def ys(x): return D[1]+(C[1]-D[1])*(x-D[0])/(C[0]-D[0])  # south line y at x
def pts(p): return " ".join(f"{x:.1f},{y:.1f}" for x,y in p)
def inside(x,y,poly):
    c=False
    for i in range(len(poly)):
        x1,y1=poly[i]; x2,y2=poly[(i+1)%len(poly)]
        if (y1>y)!=(y2>y) and x < x1+(y-y1)*(x2-x1)/(y2-y1): c=not c
    return c
def rect(x,y,w,h): return [(x,y),(x+w,y),(x+w,y+h),(x,y+h)]

out=[]
o=out.append
DR=(9,21)   # driveway band depth
house=[(88,36),(122,36),(122,33),(136,33),(136,36),(150,36),(150,68),(88,68)]
garage=rect(150,36,24,24)
terrace=rect(84,68,70,11)
motor=[(142,21),(176,21),(176,36),(174,36),(174,36),(150,36),(150,30),(142,30)]
PC=(22,68); PA=-81.4   # pool centre and angle: long side runs parallel to Sir Francis Drake
patio=rect(44,42,40,38)
firepit=(58,97,9)
guest=rect(-2,100,38,16)
blocked=[rect(-6,96,46,24),house,garage,terrace,motor,rect(6,36,40,66),patio,rect(34,50,12,30),rect(22,21,10,18),rect(-30,DR[0]-2,280,DR[1]-DR[0]+4),rect(112,21,12,15)]

o('<svg xmlns="http://www.w3.org/2000/svg" viewBox="-75 -60 345 245" font-family="Georgia, serif">')
o('<defs><pattern id="pave" width="3" height="3" patternUnits="userSpaceOnUse"><rect width="3" height="3" fill="#e9e7e2"/><circle cx=".8" cy=".9" r=".28" fill="#a9a59c"/><circle cx="2.2" cy="2.1" r=".22" fill="#bdb9b0"/></pattern>')
o('<pattern id="stone" width="4" height="4" patternUnits="userSpaceOnUse"><rect width="4" height="4" fill="#f1ece2"/><path d="M0 2H4M2 0V2M0 4V2M4 2V4" stroke="#cfc6b5" stroke-width=".15"/></pattern>')
o('<pattern id="deck" width="2" height="2" patternUnits="userSpaceOnUse"><rect width="2" height="2" fill="#efe3cf"/><path d="M0 .1H2" stroke="#d8c4a3" stroke-width=".2"/></pattern>')
o('<pattern id="road" width="4" height="4" patternUnits="userSpaceOnUse"><rect width="4" height="4" fill="#d4d4d1"/></pattern>')
o('<linearGradient id="water" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#a8d8e8"/><stop offset="1" stop-color="#6fb7d3"/></linearGradient></defs>')
o('<rect x="-75" y="-60" width="345" height="245" fill="#fff"/>')
# Sir Francis Drake Blvd along the west side
ux,uy=(D[0]-A[0])/124.7,(D[1]-A[1])/124.7; nx,ny=-uy,ux  # normal pointing west (left)
def off(p,d,t=0): return (p[0]+nx*d+ux*t,p[1]+ny*d+uy*t)
o(f'<polygon points="{pts([off(A,22,-28),off(A,52,-28),off(D,52,40),off(D,22,40)])}" fill="url(#road)"/>')
o(f'<polyline points="{pts([off(A,37,-28),off(D,37,40)])}" stroke="#fff" stroke-width=".6" stroke-dasharray="4 4"/>')
cx,cy=off((A[0]*.5+D[0]*.5,A[1]*.5+D[1]*.5),42); ang=math.degrees(math.atan2(uy,ux))
o(f'<text x="{cx:.1f}" y="{cy:.1f}" transform="rotate({ang-180:.1f} {cx:.1f} {cy:.1f})" font-size="4.6" letter-spacing=".6" text-anchor="middle" fill="#555" font-style="italic">SIR FRANCIS DRAKE BLVD</text>')
# sidewalk
o(f'<polygon points="{pts([off(A,12,-28),off(A,20,-28),off(D,20,40),off(D,12,40)])}" fill="#eeeeea" stroke="#bbb" stroke-width=".25"/>')
# driveway continuing east to the Ridgeview homes, and out west through the gate
o(f'<path d="M{off((xw(DR[0]),DR[0]),14)[0]:.1f} {DR[0]} L{xe(DR[0])} {DR[0]} C 232 {DR[0]}, 244 2, 252 -14 L 262 -8 C 252 12, 240 {DR[1]}, {xe(DR[1])} {DR[1]} L{off((xw(DR[1]),DR[1]),14)[0]:.1f} {DR[1]} Z" fill="url(#pave)" stroke="#8f8b83" stroke-width=".35"/>')

o(f'<text x="243" y="-20" font-size="3.3" fill="#555" text-anchor="middle" font-style="italic">to Ridgeview Dr. homes</text>')
gx=xw(DR[0])-3
o(f'<line x1="{gx-1}" y1="{DR[0]}" x2="{gx-3}" y2="{DR[1]}" stroke="#333" stroke-width=".9"/>')
o(f'<text x="{gx-8}" y="{DR[0]-3}" font-size="3" fill="#555">GATE</text>')
# lawn fill inside lot
o(f'<polygon points="{pts(LOT)}" fill="#f4f8ef"/>')
# re-draw driveway portion over lawn
o(f'<polygon points="{pts([(xw(DR[0]),DR[0]),(xe(DR[0]),DR[0]),(xe(DR[1]),DR[1]),(xw(DR[1]),DR[1])])}" fill="url(#pave)" stroke="#8f8b83" stroke-width=".35"/>')
# motor court + walk
o(f'<polygon points="{pts(motor)}" fill="url(#pave)" stroke="#8f8b83" stroke-width=".35"/>')
o(f'<polygon points="{pts(rect(112,21,12,12))}" fill="url(#stone)" stroke="#b9ae9a" stroke-width=".25"/>')
# terrace & pool deck
o(f'<polygon points="{pts(terrace)}" fill="url(#stone)" stroke="#b9ae9a" stroke-width=".3"/>')
# walk from pool deck to patio, then patio with pergola dining and outdoor kitchen
o(f'<polygon points="{pts(rect(34,50,12,28))}" fill="url(#stone)" stroke="#b9ae9a" stroke-width=".3"/>')
o(f'<polygon points="{pts(patio)}" fill="url(#stone)" stroke="#b9ae9a" stroke-width=".3"/>')
o('<text x="64" y="77" font-size="3.2" text-anchor="middle" fill="#6b604e" letter-spacing=".5">PATIO</text>')
o('<g stroke="#7a6a52" fill="none"><rect x="48" y="45" width="24" height="17" stroke-width=".5"/>' + "".join(f'<line x1="{48+i*2}" y1="45" x2="{48+i*2}" y2="62" stroke-width=".18"/>' for i in range(1,12)) + '</g>')
o('<rect x="54" y="51.5" width="12" height="4" rx=".4" fill="#fff" stroke="#6b604e" stroke-width=".3"/>')
for cx in (56,60,64):
    for cy in (49.8,57.3): o(f'<rect x="{cx-1}" y="{cy-.8}" width="2" height="1.6" rx=".3" fill="#fff" stroke="#8a7c66" stroke-width=".2"/>')
o('<text x="60" y="66" font-size="2.6" text-anchor="middle" fill="#6b604e">PERGOLA &amp; DINING</text>')
o('<rect x="75" y="44" width="6" height="18" fill="#e3ddd1" stroke="#6b604e" stroke-width=".35"/><rect x="76" y="48" width="4" height="6" fill="#bdb6a8" stroke="#6b604e" stroke-width=".2"/>')
o('<text x="78" y="68" font-size="2.3" text-anchor="middle" fill="#6b604e">OUTDOOR</text><text x="78" y="70.8" font-size="2.3" text-anchor="middle" fill="#6b604e">KITCHEN</text>')
for x in (46,50,54): o(f'<rect x="{x}" y="{42-0}" width="3" height="1.4" fill="#9cbf87" opacity=".0"/>')
# guest / pool house (ADU) in the setback beside the pool
o(f'<polygon points="{pts([(x+1,y+1) for x,y in guest])}" fill="#000" opacity=".12"/>')
o(f'<polygon points="{pts(guest)}" fill="#fbfaf7" stroke="#222" stroke-width=".6"/>')
o('<path d="M-2 100 L6 108 L28 108 L36 100 M-2 116 L6 108 M36 116 L28 108" stroke="#555" stroke-width=".3" fill="none"/>')
o('<rect x="11" y="97.4" width="12" height="2.6" fill="url(#stone)" stroke="#b9ae9a" stroke-width=".25"/>')
o('<text x="17" y="105" font-size="2.8" text-anchor="middle" fill="#222" letter-spacing=".3" stroke="#fbfaf7" stroke-width="1.2" paint-order="stroke">GUEST /</text>')
o('<text x="17" y="108.6" font-size="2.8" text-anchor="middle" fill="#222" letter-spacing=".3" stroke="#fbfaf7" stroke-width="1.2" paint-order="stroke">POOL HOUSE</text>')
o('<text x="17" y="112.2" font-size="2.3" text-anchor="middle" fill="#555" stroke="#fbfaf7" stroke-width="1.2" paint-order="stroke">(ADU)</text>')
# stepping stones from the driveway to the pool
for yy in (23,27,31): o(f'<rect x="25" y="{yy}" width="5" height="2.2" rx=".8" fill="#e6e0d4" stroke="#b9ae9a" stroke-width=".25"/>')
# pool, spa and deck, turned to run parallel with Sir Francis Drake
o(f'<g transform="translate({PC[0]} {PC[1]}) rotate({PA})">')
o('<rect x="-29" y="-12" width="58" height="29" fill="url(#deck)" stroke="#b9a07a" stroke-width=".3"/>')
o('<rect x="-21.2" y="-9.7" width="42.4" height="19.4" rx="1" fill="#f7f4ee" stroke="#9a9a9a" stroke-width=".3"/>')
o('<rect x="-20" y="-8.5" width="40" height="17" rx=".6" fill="url(#water)" stroke="#4d8fa8" stroke-width=".35"/>')
for i in range(3): o(f'<path d="M{-15+i*11} {-4+i*3} q2 -1 4 0 t4 0" stroke="#fff" stroke-width=".35" fill="none" opacity=".8"/>')
o('<circle cx="25" cy="0" r="5.2" fill="#f7f4ee" stroke="#9a9a9a" stroke-width=".3"/><circle cx="25" cy="0" r="4.2" fill="url(#water)" stroke="#4d8fa8" stroke-width=".35"/>')
o('<text x="0" y="1.2" font-size="3.4" text-anchor="middle" fill="#1f5870" letter-spacing=".5">POOL</text>')
o('<text x="25" y="8.6" font-size="2.4" text-anchor="middle" fill="#1f5870">SPA</text>')
for i in range(4): o(f'<rect x="{-16+i*8}" y="10.5" width="3" height="5" rx=".6" fill="#fff" stroke="#999" stroke-width=".25"/>')
o('</g>')
# house: shadow, footprint, hip roof lines
o(f'<polygon points="{pts([(x+1.2,y+1.2) for x,y in house])}" fill="#000" opacity=".12"/>')
o(f'<polygon points="{pts(garage)}" fill="#fbfaf7" stroke="#222" stroke-width=".6"/>')
o(f'<polygon points="{pts(house)}" fill="#fbfaf7" stroke="#222" stroke-width=".7"/>')
o('<g stroke="#555" stroke-width=".3" fill="none"><path d="M88 36 L104 52 L134 52 L150 36 M88 68 L104 52 M150 68 L134 52"/><path d="M150 36 L162 48 L174 36 M150 60 L162 48 L174 60"/><path d="M122 33 L126 37 L132 37 L136 33"/></g>')
o('<rect x="126" y="41" width="3" height="3" fill="none" stroke="#555" stroke-width=".3"/>')
o('<text x="119" y="60.5" font-size="4" text-anchor="middle" fill="#222" letter-spacing=".4">2-STORY HOME</text>')
o('<text x="119" y="65" font-size="3" text-anchor="middle" fill="#555">about 4,000 sq ft</text>')
o('<text x="162" y="56" font-size="2.8" text-anchor="middle" fill="#555">GARAGE</text>')
o('<g fill="#fff" stroke="#222" stroke-width=".3"><rect x="115" y="31" width="6" height="2"/></g><text x="129" y="31.2" font-size="2.6" text-anchor="middle" fill="#555">ENTRY</text>')
for i in range(3): o(f'<line x1="{112.5}" y1="{22.5+i*1.3}" x2="{123.5}" y2="{22.5+i*1.3}" stroke="#b9ae9a" stroke-width=".2"/>')
# trees and shrubs
def tree(x,y,r,col="#9a9a96"):
    s=f'<g><circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" fill="#fff" fill-opacity=".85" stroke="{col}" stroke-width=".3"/>'
    for k in range(10):
        a=k*math.pi/5+random.random()*.3
        s+=f'<line x1="{x:.1f}" y1="{y:.1f}" x2="{x+r*.95*math.cos(a):.1f}" y2="{y+r*.95*math.sin(a):.1f}" stroke="{col}" stroke-width=".22"/>'
        s+=f'<path d="M{x+r*.95*math.cos(a):.1f} {y+r*.95*math.sin(a):.1f} l{math.cos(a+2.4)*r*.18:.2f} {math.sin(a+2.4)*r*.18:.2f}" stroke="{col}" stroke-width=".22"/>'
    return s+f'<circle cx="{x:.1f}" cy="{y:.1f}" r=".5" fill="{col}"/></g>'
def shrub(x,y,r=1.8):
    s=''
    for k in range(7):
        a=k*2*math.pi/7
        s+=f'<line x1="{x:.1f}" y1="{y:.1f}" x2="{x+r*math.cos(a):.1f}" y2="{y+r*math.sin(a):.1f}" stroke="#5f9a4a" stroke-width=".7" stroke-linecap="round"/>'
    return f'<g>{s}<circle cx="{x:.1f}" cy="{y:.1f}" r=".6" fill="#3f7a30"/></g>'
# grass tufts over open lawn
for _ in range(900):
    x=random.uniform(-19,222); y=random.uniform(22,124)
    if not inside(x,y,[(p[0]*.97+3,p[1]*.96+2) for p in LOT]) or any(inside(x,y,[(px-2,py-2) if i==0 else (px+2,py-2) if i==1 else (px+2,py+2) if i==2 else (px-2,py+2) for i,(px,py) in enumerate(b[:4])]) for b in blocked[4:]): continue
    if any(inside(x,y,b) for b in blocked): continue
    if inside(x,y,rect(84,33,94,48)): continue
    if random.random()<.55: continue
    o(f'<path d="M{x:.1f} {y:.1f} l-.6 -1.1 M{x:.1f} {y:.1f} l0 -1.4 M{x:.1f} {y:.1f} l.6 -1.1" stroke="#9cbc86" stroke-width=".22" fill="none"/>')
# planting beds along the south line and in front of the house
for x in range(-8,186,7):
    if x<36: continue
    y=ys(x)-4.5+random.uniform(-1,1)
    o(shrub(x,y,random.uniform(1.4,2.1)))
for y in range(30,112,7):
    o(shrub(xe(y)-4.5,y,random.uniform(1.4,2)))
for x in (91,96,101,106,131,137,143): o(shrub(x,33.5 if x<122 else 33.2,1.3))
for x in (88,94,100,106,112,138,144,150): o(shrub(x,81.5,1.4))
# pool hedge
for y in range(34,97,5): o(shrub(xw(y)+5,y,1.6))
# trees: along the south and east edges, a few in the lawn
for x,y,r in [(47,114,5.2),(84,110,7.5),(110,106,8),(150,104,7),(178,98,7),(196,60,7),(198,34,6.5),(4,29,5.5),(76,30,6),(186,78,6.5),(170,110,5)]:
    o(tree(x,y,r))
o(f'<text x="100" y="{(DR[0]+DR[1])/2+1.4}" font-size="3.6" fill="#555" text-anchor="middle" letter-spacing=".4">SHARED DRIVEWAY</text>')
# lot line on top
o(f'<polygon points="{pts(LOT)}" fill="none" stroke="#111" stroke-width=".8" stroke-dasharray="6 1.5 1.5 1.5"/>')
# labels
o('<text x="100" y="-4" font-size="3.4" text-anchor="middle" fill="#666" letter-spacing=".4">NEIGHBOR</text>')
o('<text x="95" y="134" font-size="3.4" text-anchor="middle" fill="#666" letter-spacing=".4">NEIGHBOR</text>')
o('<text x="222" y="88" font-size="3.4" text-anchor="middle" fill="#666" letter-spacing=".4">PARCEL 1</text>')
o('<text x="-19" y="96" font-size="3" fill="#555" transform="rotate(-81.4 -19 96)" letter-spacing=".4">101&#8242; SIDE</text>')
# north arrow: north is 35.65° above +x
na=math.radians(-35.65); ax,ay=236,130
o(f'<g transform="translate({ax} {ay}) rotate({-35.65+90})"><circle r="7" fill="#fff" stroke="#333" stroke-width=".35"/><path d="M0 -6 L2 3 L0 1.6 L-2 3 Z" fill="#222"/><line y1="1.6" y2="5.5" stroke="#222" stroke-width=".5"/><text y="-8.2" font-size="3.4" text-anchor="middle" fill="#222">N</text></g>')
# title block
o('<text x="-65" y="-44" font-size="8" fill="#1f3528" font-weight="bold">3 RIDGEVIEW DRIVE</text>')
o('<text x="-65" y="-36" font-size="3.8" fill="#555" letter-spacing=".6">CONCEPT SITE PLAN &#183; PARCEL 2 &#183; 23,500 SQ FT &#183; ROSS, CA</text>')
o('<text x="-65" y="178" font-size="3" fill="#777" font-style="italic">Illustration only, not to scale. Shows one possible layout; not an approved design. Buyers must confirm what can be built with the Town of Ross.</text>')
o('</svg>')
open(__import__('os').path.join(__import__('os').path.dirname(__file__),'..','images','concept-plan.svg'),'w').write("\n".join(out))
