#!/usr/bin/python
import math as pl
import numpy as np

values = [0, np.pi/4, np.pi/2, 3*np.pi/3, np.pi]
#print 'Funcion Sen(x)'

print '\n ---   Sen^2(x) + Cos^2(x)   --- '
for v in values:
  print 'Sen^2(', v, ') + Cos^2(', v ,') = ' , pl.sin(v)**2 + pl.cos(v)**2


print '\n'