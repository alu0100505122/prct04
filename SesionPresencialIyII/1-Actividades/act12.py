#!/usr/bin/python
# -⁻- coding: UTF-8 -*-
# Matrix Function 2
# Alexandra Rivero 

import os

# *************************************
# ** Funcion para imprimir una matriz
# *************************************
def printmatrix(matrix):
	print '----------------------------------------------------'
	print '----->  Matriz  Actual    <-------------------------'
	print '----------------------------------------------------'
	for i in range(len(matrix)):
		print "      ", matrix[i]
	print '----------------------------------------------------'
	
# ******************************************
# ** Funcion para inicializar las matrices 
# ********* (las rellena con 0 )   *********
# ******************************************
def initmatrix(m,n):
	return [[0 for row in range(n)] for col in range(m)]

# ******************************************
# ** Funcion para coger los datos de las
# ** dimensiones m y n de las matrices
# ******************************************
def getmn(nm):
	while True:
		try:
			print "--- Introduzca un valor para ", nm
			v = int(raw_input('>>  '))
			break
		except ValueError:
			print "Oops! Esto no es un número!.  Inténtelo de nuevo..."
	return v


# ******************************************
# ** Funcion para rellenar las matrices 
# ** desde teclado  
# ******************************************
def fillmatrix(matrix):
	for i in range(len(matrix)):
		for j in range(len(matrix[i])):
			while True:
				try:
					print '---   Valor para la posicion ', i, ' ', j
					v = int(raw_input('>>  '))
					matrix[i][j] = v
					break
				except ValueError:
					print "Oops! Esto no es un número!.  Inténtelo de nuevo..."
	
	return matrix


# ********************************************
# ** Funcion de donde se llama a este programa
# ********************************************
def main():
	os.system('clear')
	print '----------------------------------------------------'
	print '--- Creación de matrices A(m x n)     --------------'
	print '----------------------------------------------------'
	print '----------------------------------------------------'
	m = getmn("m")
	n = getmn("n")
	matrix = initmatrix(m, n)
	print '----------------------------------------------------'
	print '---  Su Matriz ha sido inicializada de la forma ----'
	printmatrix(matrix)
	fillmatrix(matrix)
	printmatrix(matrix)
	
	

if __name__ == '__main__':
	
	main()
	
	