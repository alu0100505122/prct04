#!/usr/bin/python
# -⁻- coding: UTF-8 -*-
# Derivadas 
# Alexandra Rivero 


import os
import math 
import sympy
from sympy import *
from sympy.abc import x, y

def error(a, b):
	return abs(b-a)

def diff(f, x, h):
	return ( f(x + h) - f(x - h)) / 2 * h


def main():

	points = [0, 0, 2 * math.pi, 1]
	h = 0.01
	x = symbols('x')
	fucions = [math.e**x, math.e**((-2*x)**2), cos(x), ln(x)]
	os.system('clear')
	print ' ------------------------------------------------------------ '
	print ' ------       Resultados de las operaciones        ---------- '
	print ' ------------------------------------------------------------ '
	
	for f, p in zip(fucions, points):
		print ' ------------------------------------------------------------ '
		print ' --- Para la fucion = ', f
		print ' --- ( en x = ', p, ' y h = ', h, " )   "
		a = diff(f, p, h)
		print ' --- My diff es     = ', a
		b = sympy.diff(f).subs(x, p)
		print ' --- Python diff es = ', b
		print ' -----------> Error = ', error(a, b) 
		print ' ------------------------------------------------------------ '
	
	
main()
