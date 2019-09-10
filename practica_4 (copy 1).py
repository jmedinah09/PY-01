#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  11 11:40:40 2019

@author: jmedinah09
"""

def clear():
    """Funcion para limpiar la pantalla de la consola."""
    from os import system
    system('clear')


while True:
    clear()
    print('--Menu para la practica IV--')
    print('')
    print('1. Ejercicio 4.1 - Sumar listas.')
    print('2. Ejercicio 3.2 - Multiplicar listas.')
    print('3. Ejercicio 3.3 - Mayor numero de una lista.')
    print('4. Ejercicio 3.4 - Numero mas pequenio de una lista.')
    print('5. Ejercicio 3.5 - Numeros palindromicos.')
    print('0. Salir.')
    print('------------------------------------------------------------------')
    OPCION = int(input('Ingrese una de las opciones anteriores (0-12): -> '))
    print('------------------------------------------------------------------')
    
    if OPCION == 0:
        clear()
        print('Gracias, regrese pronto!')
        break
    
    elif OPCION == 1:
        clear()

        a = []
        b = []
        c = []          # c =  a + b
        num_elementos = int(input('Por favor ingrese el numero de elementos '
                                  'que contendra la lista: -> '))
        for i in range(1, num_elementos + 1):
            a_i = int(input('Ingrese el elemento a(' + str(i) + ') de la lista: -> '))
            a.append(a_i)
        print('----------------------------------------------------------------')
        print('a', ' = ', a)
        print('----------------------------------------------------------------')
        for i in range(1, num_elementos + 1):
            b_i = int(input('Ingrese el elemento b(' + str(i) + ') de la lista: -> '))
            b.append(b_i)
        print('----------------------------------------------------------------')
        print('b', ' = ', b)
        print('----------------------------------------------------------------')
        for i in range(num_elementos):
            c.append(a[i] + b[i])
        print('----------------------------------------------------------------')    
        print('La suma de las listas a y b introducidas es: ')
        print('')
        print('a + b = ', a, '+', b, '=', c)
        print('----------------------------------------------------------------')












        
