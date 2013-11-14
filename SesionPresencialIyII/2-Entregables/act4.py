#!/usr/bin/python
# -⁻- coding: UTF-8 -*-
# Integrales 
# Alexandra Rivero 


import os
import math 
from sympy import integrate
from sympy.abc import x, y

funcions = ["e**x", "cos(x)", "sin(x)", "sin(x)"]
points = [[0, math.log(3)], [0, math.pi], [0, math.pi], [0, math.pi/2]]

def error(a, b):
	return b - a

def f(f, a):
	return eval(str(f).replace("x", "a").replace("e", "math.e").replace("sin", "math.sin").replace("cos", "math.cos"))

def integra(fx, a, b):
	return ( (b - a) / 2) * (f(fx,a) + f(fx,b))

def main():
	os.system('clear')
	for fx, p in zip(funcions, points):
		print ' ------------------------------------------------------------ '
		print ' --- Para la fucion = ', fx , ' de a = ', p[0], ' b = ', p[1]
		print ' --- My integra       = ', integra(fx, p[0], p[1])
		print ' --- Python integrate = ', integrate(fx, (x, p[0], p[1]))
		print ' -------------> Error = ', error(integrate(fx, (x, p[0], p[1])), integra(fx, p[0], p[1]))
		print ' ------------------------------------------------------------- '
		

main()