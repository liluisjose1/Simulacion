#!/usr/bin/env python

# -*- coding: utf-8 -*-

lista=[59,12,19,05,59,58,83,18,36,00,61,47,24,41,42,98,23,67,84,43,29,71,88,74,60,10,46,23,15,11,78,31,11,91,99,57,28,18,32,21,12,95,38,76,07,96,33,63,10,05]
#lista=[41, 68, 89, 94, 74, 91, 55, 62, 36, 27,19, 72, 75, 9, 54, 2, 1, 36, 16, 28,18, 1, 95, 69, 18, 47, 23, 32, 82, 53,31, 42, 73, 4, 83, 45, 13, 57,63, 29] 
lista1=[]
mas=0
menos=0
n = len(lista)
for i in range(n-1):
	n1=i+1
	if lista[i]<lista[n1]:	
		menos+=1
		lista1.append(1)
	else:
		mas+=1
		lista1.append(0)

print n
print lista1


corridas=0
for k in range (n-1):
	if lista1[k]==1 and lista1[k+1]==0
		corridas+=1
print corridas
