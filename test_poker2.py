#!/usr/bin/ env python

	result=['73133','49413','46597','00287','25196','29722','30940','95766','50045','91111','47221','84079','45868','27362','89875','23318','72385','11985','05139','20524','05450','17048','65126','87417','30761','35595','81577','08958','24829','37092']
    #result=[]
    pares=0
    tercias=0
    tienejuego="todos diferentes"
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
		tienejuego="1 par"
	elif pares==2:
		tienejuego="2 pares"
	if pares==0 and tercias==1:
		tienejuego="Tercia"
	if pares==1  and tercias==1:
		tienejuego="Full"
    return tienejuego
