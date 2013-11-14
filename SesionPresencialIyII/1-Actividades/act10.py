#!/usr/bin/python
# -⁻- coding: UTF-8 -*-
# Sucesion Function 
# Alexandra Rivero 
import os

def un(a, b, u0, n):
	if n == 0:
		return u0
	return (a * un(a, b, u0, n-1) + b)

def main():
	os.system('clear')
	print '----------------------------------------------------'
	print '--- Introduzca el valor de a           -------------'
	print '----------------------------------------------------'	
	a = input('')
	print '----------------------------------------------------'
	print '--- Introduzca el valor de b           -------------'
	print '----------------------------------------------------'	
	b = input('')
	print '----------------------------------------------------'
	print '--- Introduzca el valor de U0           ------------'
	print '----------------------------------------------------'	
	u0 = input('')
	print '----------------------------------------------------'
	print '--- Introduzca el valor de n           -------------'	
	print '----------------------------------------------------'
	n = input('')
	print '----------------------------------------------------'
	result = []
	for i in range(n):
		# print un(a, b, u0, i)
		result.append(un(a, b, u0, i))
		
	print result
	print '----------------------------------------------------'
	print '---------------- Alexandra Rivero ------------------'
	print '----------------------------------------------------'


if __name__ == '__main__':
	main()