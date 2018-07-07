#!/usr/bin/python

n=int(raw_input("Ingrese el numero de pseudo aleatorios a generar:"))
seed=int(raw_input("Ingrese la semilla:"))


lista =[]
for i in range(n):
	s2=str(seed**2)
	x=2*len(str(seed))
	ls=len(s2)
	if (ls<x):
		dif=x-ls
		for j in range(dif):
			s2="0"+s2
	s22=len(s2)/2
	izq=s22-2
	der=s22+2
	s3=s2[izq:der]
	s4=int(s3)/10000.0
	
	print s3,s4
	lista.append(str(seed))
	if (lista.count(str(seed))==2):
		"Comienza a repetir en iteracion ", i
		break
	else:
		print s3,s4
		
print lista
	
