#!/usr/bin/python
# -⁻- coding: UTF-8 -*-
# Alexandra Rivero 

infile = open('data1.txt', 'r')
numbers = [float(line) for line in infile.readlines()]
infile.close()
print numbers
mean = sum(numbers)/len(numbers)
print mean
