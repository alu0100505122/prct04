#!/usr/bin/python

# Fibonacci Function
# Alexandra Rivero 

a = []

def fibonacci(n):
  if(n in (0,1)):
    return n
  else:
    return fibonacci(n-1) + fibonacci(n-2)

    
print '----------------------------------------------------'
print '-----------  Introduzca un valor     ---------------'	
n = input('')

for i in range(n):
	a.append(fibonacci(i))

print '------------ Resultado de Fibonacci de ', n ,'---------- '
print a
