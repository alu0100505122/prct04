#!/usr/bin/python
# -⁻- coding: UTF-8 -*-
# List Function 2
# Alexandra Rivero 

import os


list = []

def printlist():
	print '---> Lista ', list

def addelement(e):
	list.insert(len(list), e)
	printlist()
	raw_input("Pulse Enter para continuar...") # to catch enter key

def menu():
	opc = 1
	while (opc != 0):
		os.system('clear')
		print '----------------------------------------------------'
		print '------------  Introduzca una opcion   --------------'	
		print '1) Añadir un elemento a la lista (final)   ---------'
		print '2) Contar apariciones de un elemento en la lista ---'
		print '3) Para mostrar el estado actual de la lista   -----'
		print '4) Para eliminar la lista                  ---------'
		print '5) Para ordenar la lista                   ---------'
		print '6) Para revertir la lista                  ---------'
		print '0) Para salir del programa                 ---------'
		print '----------------------------------------------------'
		opc = input('')
		if opc == 1:
			print 'Introduzca la palabra que quiere añadir'
			w = raw_input('')
			addelement(w)
		elif opc == 2:
			print 'Introduzca la palabra que quiere contar'
			w = raw_input('')
			printlist()
			print 'Contador de la palabra (', w, ') = ', list.count(w)
			raw_input("Pulse Enter para continuar...") # to catch enter key
		elif opc == 3:
			printlist()
		elif opc == 4:
			del list[0:len(list)]
			printlist()
			raw_input("Pulse Enter para continuar...") # to catch enter key
		elif opc == 5:
			list.sort()
			printlist()
			raw_input("Pulse Enter para continuar...") # to catch enter key
		elif opc == 6:
			list.reverse()
			printlist()
			raw_input("Pulse Enter para continuar...") # to catch enter key
		else:
			print '----------------------------------------------------'
			print '---------------- Alexandra Rivero ------------------'
			print '----------------------------------------------------'


if __name__ == '__main__':
	menu()
