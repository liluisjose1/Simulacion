#!/usr/bin/env python

def medios ():
	#recibe un unico parametro
	""" Function doc """
	print "Metodo de Cuadrados Medios TS-2018 IM15005 \n"
	n=int(raw_input("Cuantos numeros pseudoaleatorios desea generar:"))
	seed=int(raw_input("Ingrese Valor de Semilla:"))
	print"\nPseudo Aleatorios Generados"
	lista=[]
	for i in range(n):
		s2=str(seed**2)
		x=2*len(str(seed))
		ls=len(s2)
		if (ls<x):
			dif=x-ls
			for j in range(dif):
				s2="0"+ s2		
		s22=len(s2)/2
		izq=s22-2
		der=s22+2
		s3=s2[izq:der]
		s4=int(s3)/10000.0
	#print s3,s4
		seed=int(s3)
		lista.append(str(seed))
		if (lista.count(str(seed))==2):
			print "Comienza a repetir en iteracion ", i
			break
		else:
			print "n=",i,s3,s4
			
def mixto ():
	""" Function doc """
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
def  aditivo():
	""" Function doc """
	print "Metodo Congruencial Aditivo  TS-2018 Luis Jose Iraheta Medrano IM15005 \n"
	print "Ejemplo 5 numeros 65,89,98,3,69 modulo=100"
#iniciamos la lista donde almacenaremos los valores
	lista=[]
#pedir la cantidad de numeros en lista
	n=int (raw_input("Numeros en la lista: "))
	n1=int (raw_input("Numero de iteraciones: "))
#pedir el valor del modulo
	m=int (raw_input("Valor de el modulo: "))
#veces en que se llenara la lista 
	#veces en que se llenara la lista 
	for j in xrange(n):
		print "Ingrese Valor de X"+str(j+1)
		x= int(raw_input(""))
		lista.append(x)

#valores muestra
#lista=[65,89,98,3,69]
#m=100
#X n+1 = X n + X n-k (mod M)

#contando los elementos de la lista
	elementos = len(lista)
#generando pseudo aleatorio veces +2 
	for i in range(n1) :
	#ultimo elemento de la lista Xn-k
		xnk=lista[-1]
	#recorriendo la lista ciclicamente
		xn=lista[i]
	#generando xn+1 con la formula y diviendo su parte entera
		xn1= (xn+xnk) % m
	#encontrando el pseudo aleatorio
		r= float(xn1)/float(m)
	#imprimiendo valores 
		print ("X"+str(elementos+(i+1))+"="+str(xn1)+" r"+str(i+1)+"="+str(r))
	#agregando a la lista el ultimo xn+1
		lista.append(xn1)

	
if __name__ == '__main__':
	respuesta = True
	print "Tecnicas de Simulacion TS-2018 IM15005"
	print "1- Metodo de Cuadrados Medios"
	print "2- Metodo de Congruencial Mixto"
	print "3- Metodo de Congruencial Aditivo"
	print "4- Salir"
	
	s=(int(raw_input("Elige una opcion:")))
	if s==1:
		medios()
	elif s==2:
		mixto()
	elif s==3:
		aditivo()
	"""else:
		aditivo()"""
		
		
