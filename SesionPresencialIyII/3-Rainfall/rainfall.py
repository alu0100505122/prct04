#!/usr/bin/python
# -⁻- coding: UTF-8 -*-
# Alexandra Rivero 

import matplotlib.pyplot as pl

def extract_data(filename):
    infile = open(filename, 'r')    
    infile.readline() # skip the first line
    numbers = []
    for line in infile:
        words = line.split()
        number = float(words[1])
        numbers.append(number)
    infile.close()
    return numbers

values = extract_data('rainfall.dat')

month_indices = range(1, 13)
pl.plot(month_indices, values[:-1])
pl.title(' o2 ')
pl.show()



