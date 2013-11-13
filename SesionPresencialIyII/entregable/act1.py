#!/usr/bin/python
# -⁻- coding: UTF-8 -*-
# Show Functions 
# Alexandra Rivero 

import os
import math 

n = [10, 100, 1000, 10000, 100000]

numberoffunctions = 3

def funcion1(n):
	return ((n**3) - 1) * (math.log(n))

def funcion2(n):
	return n*((math.log(n))**2)

def funcion3(n):
	return (n**2)*math.log(n)

def makestr(*a):
	#print '--> ', a[0]
	string = str(a[0])
	for s in a[1:]:
		string = string + ' ' + '%.2f' % float(s)
	# print '-->> ', string
	return string

def printtable(table):
	maxvalues = table[len(table)-1].split(" ")
	for s in table:
		values = s.split(" ")
		for v, maxv in zip(values, maxvalues):
			while len(v) < len(maxv):
				v = v + ' '
			print v,	
		print


def main():
	os.system('clear')
	print '----------------------------------------------------------'
	print '------- Soluciones de las funciones F1, F2 y F3  ---------'
	print '----------------------------------------------------------'
	#table = [[0 for i in range(numberoffunctions)] for j in range(len(n))]
	table = []
	table.append('n F1 F2 F3')
	for e in n:
		table.append(makestr(e, funcion1(e), funcion2(e), funcion3(e)))
	printtable(table)
	print '----------------------------------------------------------'
	
main()
