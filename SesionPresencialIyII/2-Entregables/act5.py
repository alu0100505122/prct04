#!/usr/bin/python
# -⁻- coding: UTF-8 -*-
# Graficas
# Alexandra Rivero 

import numpy as np 
import matplotlib.pyplot as pl

x = np.linspace(-np.pi, np.pi, 256, endpoint=True)
functions = [(2**x), (x**2), (x**3)]

pl.title('Representacion de x frente a y') 

# Poner etiquetas en los ejes 
pl.xlabel('Algunos enteros positivos')
pl.ylabel('Funcion de algunos enteros')

for f in functions: 
	pl.plot(x, f, label=f)

pl.show()