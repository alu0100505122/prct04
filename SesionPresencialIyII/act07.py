#!/usr/bin/python
# -⁻- coding: UTF-8 -*-
# List Function
# Alexandra Rivero 

import os


list = []

def printlist():
	print '---> Lista ', list

def addelement(pos, e):
	list.insert(pos, e)
	printlist()

def deleteelement(pos):
	if(pos <= len(list)):
		list.pop(pos)
	else:
		print ' No se puede eliminar un elemento de esa posicion'
	printlist()

def menudeleteelement():
	os.system('clear')
	print '----------------------------------------------------'
	print '-----------  Introduzca una opcion   ---------------'	
	print '1) Eliminar el primer elemento de la lista  --------'
	print '2) Eliminar el último elemento de la lista   -------'
	print '3) Eliminar un elemento en una posicion específica -'
	print '----------------------------------------------------'
	printlist()
	opc = input('')
	if opc == 1:
		deleteelement(0)
	elif opc == 2:
		deleteelement(len(list)-1)
	elif opc == 3:
		print 'Introduzca la posicion en la que quiere añadir el elemento'
		pos = input('')
		deleteelement(pos-1)
	else:
		return	
	raw_input("Pulse Enter para continuar...") # to catch enter key

def menuaddelement():
	os.system('clear')
	print '----------------------------------------------------'
	print '-----------  Introduzca una opcion   ---------------'	
	print '1) Añadir un elemento al inicio de la lista  -------'
	print '2) Añadir un elemento al final de la lista   -------'
	print '3) Añadir un elemento en una posicion específica ---'
	print '0) Volver al Menu Principal                  -------'
	print '----------------------------------------------------'
	printlist()
	opc = input('')
	if opc != 0:
		print 'Introduzca el elemento que quiere añadir a la lista'
		e = input('')
	if opc == 1:
		addelement(0,e)
	elif opc == 2:
		addelement(len(list), e)
	elif opc == 3:
		print 'Introduzca la posicion en la que quiere añadir el elemento'
		pos = input('')
		addelement(pos-1, e)
	else:
		return	
	raw_input("Pulse Enter para continuar...") # to catch enter key
	

def menu():
	opc = 1
	while (opc != 0):
		os.system('clear')
		print '----------------------------------------------------'
		print '------------  Introduzca una opcion   --------------'	
		print '1) Para añadir un elemento a la lista      ---------'
		print '2) Para eliminar un elemento en la lista   ---------'
		print '3) Para mostrar el estado actual de la lista   -----'
		print '4) Para eliminar la lista                  ---------'
		print '5) Para ordenar la lista                   ---------'
		print '6) Para revertir la lista                  ---------'
		print '0) Para salir del programa                 ---------'
		print '----------------------------------------------------'

		opc = input('')
		if opc == 1:
			menuaddelement()
		elif opc == 2:
			menudeleteelement()
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
