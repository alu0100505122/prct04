#!/usr/bin/python
# -⁻- coding: UTF-8 -*-
# Show Functions 
# Alexandra Rivero 


import os
import math 
from decimal import *


limitk = 1e-100

def calcularerror(n):
	return Decimal(1/math.pi) - n

def factorial(k):
    if k == 0:
        return 1
    else:
        return k * factorial(k-1)

def calculatepart1():
	return Decimal((2 * math.sqrt(2))/9801)

def calculatepart2(k):
	suma = 0
	for i in range(k+1):
		# print i, ' -- ', suma
		a = Decimal(factorial(4*k) * (1103 + (26390*k)))
		b = Decimal(((factorial(k))**4) * ( 396**(4*k) ))
		suma += Decimal(a/b)
	return Decimal(suma)

def estimar_pi():
	p1 = calculatepart1()
	# print 'p1 = ', p1
	k = 0
	while True:
		# Init value
		p2 = calculatepart2(k)
		print '   --->  Resultado iteracion(', k+1,') = ', p1*p2
		print '   ------->  Error : ', calcularerror(p1*p2)
		if(p1*p2) < limitk:
			return k	
			break
		k += 1
	


def main():
	os.system('clear')
	print '   ------------------------------------------------'
	print '   ----  Funcion de Srinivasa Rmanujan      -------'
	print '   ------------------------------------------------'
	k = estimar_pi()
	print '   ------------------------------------------------'
	print '   -- El valor de k que estamos buscando es : ', k
	print '   ------------------------------------------------'
		

main()


   