#!/usr/bin/python

# Conversor de unidades
# Alexandra Rivero 

# 1pulgada = 2.54cm 
# 1pie = 12pulgadas
# 1yarda = 3pies
# 1milla = 1560yardas

# 640 metros se corresponde con 25196.85 pulgadas, 2099.74 pies, 699.91 yardas, o 0.3977 millas.

def metros2cm(m):
  return (m*100)


def metros2pulgadas(m):
  return (metros2cm(m)/2.54)
 
def pulgadas2pies(m):
  return (metros2pulgadas(m)/12)
  
def pies2yarda(m):
  return (pulgadas2pies(m)/3)
  
def yarda2milla(m):
  return (pies2yarda(m)/1560)
  
metros = 0

while(metros == 0):
  print 'Introduce el valor a convertir (metros)'
  metros = input('')
  print '------------ Resultados ---------- '
  print metros2pulgadas(metros), 'pulgadas'
  print pulgadas2pies(metros), 'pies'
  print pies2yarda(metros), 'yarda'
  print yarda2milla(metros), 'millas'

  

 
