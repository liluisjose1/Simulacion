#!/usr/bin/ env python

'''
Mano de juego poker con 5 cartas
Elabore un script en python que pida un numero de 5 digitos
y que verifique como en el juego de poker si de los cinco
numeros tiene una mano de :
    Todos Diferentes, por ejemplo para n=65490
    un par,  por ejemplo para n=34238
    dos pares, por ejemplo para n=66799
    tercia, por ejemplo para n=55519
    full,  por ejemplo para n=52525
    poker, por ejemplo para n=10111
    pocarin, por ejemplo para n=22222
'''

def mano(valor):
    result=[]
    pares=0
    tercias=0
    tienejuego="td"
    for i in range(10):
        result.append(valor.count(str(i)))
        #print result
    for j in range(10):
        if result[j]==2:
			pares+=1
        if result[j]==3:
			tercias+=1
        if result[j]==4:
			tienejuego="Poker"
        if result[j]==5:
			tienejuego= "Pocarin"

	if pares==1:
		tienejuego="1par"
	elif pares==2:
		tienejuego="2pares"
	if pares==0 and tercias==1:
		tienejuego="Tercia"
	if pares==1  and tercias==1:
		tienejuego="Full"
    return tienejuego


aleatorios=['0.73133','0.49413','0.46597','0.00287','0.25196','0.29722',
			'0.30940','0.95766','0.50045','0.91111',
			'0.47221','0.84079','0.45868','0.27362','0.89875',
			'0.23318','0.72385','0.11985','0.05139','0.20524',
			'0.05450','0.17048','0.65126','0.87417','0.30761',
			'0.35595','0.81577','0.08958','0.24829','0.37092']

probabilidad=[0.3024,0.5040,0.1080,0.0720,0.0090,0.0045,0.0001]
n = len(aleatorios)
fo=[]
td=0
par1=0
par2=0
tercia=0
full=0
poker=0
pocarin=0
p=0
fe=[]	
for i in range (n):
	entero,decimal=aleatorios[i].split('.')
	juego = mano(decimal)
	if juego == "td":
		td+=1
	if juego == "1par":
		par1+=1
	if juego == "2pares":
		par2+=1
	if juego == "Tercia":
		tercia+=1
	if juego == "Full":
		full+=1
	if juego == "Poker":
		poker+=1
	if juego == "Pocarin":
		pocarin+=1
fo.append(td)
fo.append(par1)
fo.append(par2)
fo.append(tercia)
fo.append(full)
fo.append(poker)
fo.append(pocarin)
total=0
for k in range(7):
	p=((n*probabilidad[k]-fo[k])**2)/(n*probabilidad[k])
	fe.append(p)
	total+= fe[k]	
print total

"""listachi6=[22.4575,20.2491,18.5475,16.8119,14.4494,12.5916,10.6446,9.4461,8.5581,7.8408,7.2311,6.6948,6.2108,5.7652,5.3481]
tol= int(raw_input("Ingresa Tolerancia"))"""
if total<10.6446:
	print "Pseudoaleatorios aceptados"
else:
	print "Pseudoaleatorios No aceptados"
	
		
		
	
