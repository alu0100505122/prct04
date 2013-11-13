#!/usr/bin/python
# -⁻- coding: UTF-8 -*-
# Matrix Function 2
# Alexandra Rivero 

import os
import random

# *************************************
# ** Funcion para imprimir una matriz
# *************************************
def printmatrix(matrix):
	print '\n----------------------------------------------------'
	for i in range(len(matrix)):
		print "      ", matrix[i]
	print '----------------------------------------------------'

# ******************************************
# ** Funcion para imprimir los resultados
# ** de las multiplicaciones de las matrices
# ******************************************
def printresult(matrixA, matrixB, matrixC):
	print '-----------------------------------------------------'
	print '-- El resultado de la Multiplicación es la matriz C -'
	print '-----------------------------------------------------'
	printmatrix(matrixA)
	print '           X'
	printmatrix(matrixB)
	print '           ='
	printmatrix(matrixC)

# ******************************************
# ** Funcion para esperar un Enter del  
# ** usuario para continuar
# ******************************************
def wait4enter():
	raw_input("Pulse Enter para acabar!!...") # to catch enter key
	os.system('clear')
	
# ******************************************
# ** Funcion para coger los datos de las
# ** dimensiones m y n de las matrices
# ******************************************
def getmn(nm, matrixname):
	while True:
		try:
			print "--- Introduzca un valor para", nm, "(de la matriz ", matrixname,")"
			v = int(raw_input('>>  '))
			break
		except ValueError:
			print "Oops! Esto no es un número!.  Inténtelo de nuevo..."
	return v


# ******************************************
# ** Funcion para inicializar las matrices 
# ********* (las rellena con 0 )   *********
# ******************************************
def initmatrix(m,n):
	return [[0 for j in range(n)] for i in range(m)]


# ******************************************
# ** Las funciones loadA y loadB son las que 
# ** nos ayudan a inicar las matrices con 
# ** parámetros predefinidos (para los test)
# ******************************************
def loadA():
	matrix = initmatrix(3, 3)
	matrix[0][0] = 2
	matrix[0][1] = 0
	matrix[0][2] = 1
	matrix[1][0] = 3
	matrix[1][1] = 0
	matrix[1][2] = 0
	matrix[2][0] = 5
	matrix[2][1] = 1
	matrix[2][2] = 1
	return matrix

def loadB():
	matrix = initmatrix(3, 3)
	matrix[0][0] = 1
	matrix[0][1] = 0
	matrix[0][2] = 1
	matrix[1][0] = 1
	matrix[1][1] = 2
	matrix[1][2] = 1
	matrix[2][0] = 1
	matrix[2][1] = 1
	matrix[2][2] = 0
	return matrix


# ******************************************
# ** Funcion para rellenar las matrices 
# ** desde teclado  
# ******************************************
def fillmatrix(matrix):
	for i in range(len(matrix)):
		for j in range(len(matrix[i])):
			while True:
				try:
					print 'Valor para la posicion ', i, ' ', j
					v = int(raw_input(''))
					matrix[i][j] = v
					break
				except ValueError:
					print "Oops! Esto no es un número!.  Inténtelo de nuevo..."
	
	return matrix

# ***********************************************
# ** Funcion que realiza una multiplicacion entre 
# ** las matrices que le pasemos y nos devuelve 
# ** la matriz resultado de esta operacion  
# ***********************************************
def mul(matrixA, matrixB):
	matrixC = [[0 for j in range(len(matrixB[0]))] for i in range(len(matrixA))]
	for i in range(len(matrixA)): # is the same that matrixC(m)
		for j in range(len(matrixB[0])): # is the same that matrixC(n) or matrixC[0]
			for k in range(len(matrixB)): # is the same that matrixA(m) or matrixC(m)
				matrixC[i][j] = matrixC[i][j] + matrixA[i][k]*matrixB[k][j]
	return matrixC


# ********************************************
# ** Funcion de donde se llama a este programa
# ********************************************
def main():
	os.system('clear')
	print '----------------------------------------------------'
	print '------  Multiplicación de matrices (A x B)  --------'
	print '----------------------------------------------------'
	print '----------------------------------------------------'
	print '------   Datos de la Matriz A      -----------------'
	print '----------------------------------------------------'
	ma = getmn("m", "A")
	na = getmn("n", "A")
	print '---  Su Matriz ha sido inicializada de la forma ----'
	matrixA = initmatrix(ma, na)
	printmatrix(matrixA)
	wait4enter()

	print '----------------------------------------------------'
	print '------   Datos de la Matriz B      -----------------'
	print '----------------------------------------------------'
	while True:
		mb = getmn("m", "B")
		if(mb == na):
			break
		else:
			print "Oops! Este no puede ser el valor de m de B.  Inténtelo de nuevo..."
	nb = getmn("n", "B")
	matrixB = initmatrix(mb, nb)
	print '----------------------------------------------------'
	print '---  Su Matriz ha sido inicializada de la forma ----'
	printmatrix(matrixB)
	wait4enter()
	print '----------------------------------------------------'
	print '---  Rellenemos los valores de la matriz A    ------'
	print '----------------------------------------------------'
	matrixA = fillmatrix(matrixA)
	print '---  Ahora su matriz es de la forma siguiente   ----'
	printmatrix(matrixA)
	wait4enter()
	print '----------------------------------------------------'
	print '---  Rellenemos los valores de la matriz B    ------'
	print '----------------------------------------------------'
	matrixB = fillmatrix(matrixB)
	print '---  Ahora su matriz es de la forma siguiente   ----'
	printmatrix(matrixB)
	wait4enter()
	matrixC = mul(matrixA, matrixB)
	printresult(matrixA, matrixB, matrixC)
	wait4enter()
	

if __name__ == '__main__':
	
	# ******************************************
	# ** Para hacer pruebas con unas matrices 
	# ** predefinidas (las de loadA y loadB)
	# ****************************************** 
	os.system('clear')
	print '----------------------------------------------------'
	print '------  Multiplicación de matrices (A x B)  --------'
	print '----------------------------------------------------'
	print '----------------------------------------------------'
	print '------   Datos de la Matriz A      -----------------'
	print '----------------------------------------------------'
	matrixA = loadA()
	printmatrix(matrixA)
	wait4enter()
	print '----------------------------------------------------'
	print '------   Datos de la Matriz B      -----------------'
	print '----------------------------------------------------'
	matrixB = loadB()
	printmatrix(matrixB)
	wait4enter()
	matrixC = mul(matrixA, matrixB)
	printresult(matrixA, matrixB, matrixC)
	wait4enter()

	# ******************************************
	# ** Para elegir y rellenar las matrices
	# ** por el usuario desde teclado 
	# ****************************************** 
	main()