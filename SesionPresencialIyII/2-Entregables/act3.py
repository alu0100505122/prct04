#!/usr/bin/python
# -⁻- coding: UTF-8 -*-
# Derivadas 
# Alexandra Rivero 


import os
import math 
import sympy
from sympy import *

def error(a, b):
	return abs(b-a)

def f(f, a):
	return eval(str(f.subs('x', a)))

def diff(fx, x, h):
	return (f(fx, x + h) - f(fx, x - h)) / 2 * h


def main():

	points = [0, 0, 2 * math.pi, 1]
	h = 0.01
	x = symbols('x')
	fucions = [math.e**x, math.e**((-2*x)**2), cos(x), ln(x)]
	os.system('clear')
	print ' ------------------------------------------------------------ '
	print ' ------       Resultados de las operaciones        ---------- '
	print ' ------------------------------------------------------------ '
	
	for fx, p in zip(fucions, points):
		print ' ------------------------------------------------------------ '
		print ' --- Para la fucion = ', fx
		print ' --- ( en x = ', p, ' y h = ', h, " )   "
		a = diff(fx, p, h)
		print ' --- My diff es     = ', a
		b = sympy.diff(fx).subs(x, p)
		print ' --- Python diff es = ', b
		print ' -----------> Error = ', error(a, b) 
		print ' ------------------------------------------------------------ '
	
	
main()
