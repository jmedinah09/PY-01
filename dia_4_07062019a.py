#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 17:32:32 2019

@author: jmedinah09
"""

# En la programacion estructurada no hay relacion entre variables y funciones.
# En la POO se trata de solucionar esto a traves de las clases.
# Las clases son un conjunto de datos asociados a un conjunto de funcionamientos.
# Instancia: cuando se crea un objeto a partir de una clase.
# El operador '.' permanece permite acceder a las funcionalidades de la clase.
# Clase: molde atravez del que se crea un objeto. Es un concepto, plano, molde...
# Clase: representacion conceptual del objeto. Ej. int, str, bool..., 
# Funcion constructora o metodo constructor: no necesita ser llamado, se ejecuta con\
# la instancia, sirve para construir la clase.
# Self: para cualquier instancia de la clase.
# Los argumentos no necesariamente deben llamarse igual que los atributos, \
# es recomendable.


# class Perro:
#     cantidad_de_patas = 4
#     raza = ''
#     def ladrar(self):
#         print('El perro ladra.')
#     def morder(self):
#         print('El perro muerde.')
# lazie = Perro() #instanciacion  
# print(lazie.cantidad_de_patas)
# lazie.ladrar()

class Employee:
	def __init__(self, first, last, pay):
		self.first = first
		self.last  = last
		self.pay = pay
		self.email = f'{self.first}.{self.last}@company.com' 
		self.fullname = f'{self.first} {self.last}'


# emp_1 = Employee()
# emp_2 = Employee()
# emp_1.first = 'Corey'
# emp_1.last  = 'Schafer'
# emp_1. pay  =  50000
# emp_1.email = 'Corey.Schafer@company.com'
emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Jose', 'Medina', 90000)
print(f'{emp_1.first} y {emp_2.first}')







     