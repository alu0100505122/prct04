#!/usr/bin/python
# -⁻- coding: UTF-8 -*-
# Alexandra Rivero 

infile = open('data1.txt', 'r')
numbers = [float(w) for w in infile.read().split()]
print numbers
mean = sum(numbers)/len(numbers)
print mean
infile.close()

