#!/usr/bin/python
# -⁻- coding: UTF-8 -*-
# Derivadas 
# Alexandra Rivero 


import os
import math 
import sympy
from sympy import *

funcions = ["math.e**x", "math.e**((-2*x)**2)", "cos(x)", "ln(x)"]
points = [0, 0, 2 * math.pi, 1]
h = 0.01

def error(a, b):
	return abs(int(b) - int(a))

def f(f, a):
	return eval(str(f).replace("x", "a"))

def diff(fx, x, h):
	return ( f(fx, x + h) - f(fx, x - h)) / 2 * h

def main():
	os.system('clear')
	x = Symbol("x")
	for fx, p in zip(funcions, points):
		print ' ------------------------------------------------------------ '
		print ' --- Para la fucion = ', fx , ' en x = ', p, ' y h = ', h
		a = diff(fx, p, h)
		print ' --- My diff es     = ', a
		b = sympy.diff(fx, x)
		print ' --- Python diff es = ', b
		c = error(a, b) 
		print ' -------------> Error = ', c
		print ' ------------------------------------------------------------- '
		

main()
