#!/usr/bin/python
# -⁻- coding: UTF-8 -*-
# List Function 2
# Alexandra Rivero 

import os


list = []

def printlist():
	print '---> Lista ', list

def addelements(all):
	for e in all:
		list.insert(len(list), e)
	printlist()
	raw_input("Pulse Enter para continuar...") # to catch enter key

def main():
	opc = 1
	while (opc != 0):
		os.system('clear')
		print '----------------------------------------------------'
		print '------------  Introduzca una opcion   --------------'	
		print '1) Añadir entero(s) a la lista (final)     ---------'
		print '2) Para mostrar el estado actual de la lista   -----'
		print '3) Para eliminar la lista                  ---------'
		print '4) Para ordenar la lista                   ---------'
		print '5) Para revertir la lista                  ---------'
		print '0) Para salir del programa                 ---------'
		print '----------------------------------------------------'
		opc = input('')
		if opc == 1:
			print 'Introduzca el(los) entero(s) que quiere añadir (Separado por espacios)'
			n = raw_input('')
			addelements(n.split())
		elif opc == 2:
			printlist()
			raw_input("Pulse Enter para continuar...") # to catch enter key
		elif opc == 3:
			del list[0:len(list)]
			printlist()
			raw_input("Pulse Enter para continuar...") # to catch enter key
		elif opc == 4:
			list.sort()
			printlist()
			raw_input("Pulse Enter para continuar...") # to catch enter key
		elif opc == 5:
			list.reverse()
			printlist()
			raw_input("Pulse Enter para continuar...") # to catch enter key
		else:
			print '----------------------------------------------------'
			print '---------------- Alexandra Rivero ------------------'
			print '----------------------------------------------------'


if __name__ == '__main__':
	main()
