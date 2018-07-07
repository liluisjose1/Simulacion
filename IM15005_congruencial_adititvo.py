#!/usr/bin/env python

print "Metodo Congruencial Aditivo  TS-2018 Luis Jose Iraheta Medrano IM15005 \n"
print "Ejemplo 5 numeros 65,89,98,3,69 modulo=100"
#iniciamos la lista donde almacenaremos los valores
lista=[]
#pedir la cantidad de numeros en lista
n=int (raw_input("Numeros en la lista: "))
#pedir el valor del modulo
m=int (raw_input("Valor de el modulo: "))
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
for i in range(elementos+2) :
	#ultimo elemento de la lista Xn-k
	xnk=lista[-1]
	#recorriendo la lista ciclicamente
	xn=lista[i]
	#generando xn+1 con la formula y diviendo su parte entera
	xn1= (xn+xnk) % m
	#encontrando el pseudo aleatorio
	r=xn1/m
	#imprimiendo valores 
	print ("X"+str(elementos+(i+1))+"="+str(xn1)+" r"+str(i+1)+"="+str(r))
	#agregando a la lista el ultimo xn+1
	lista.append(xn1)
