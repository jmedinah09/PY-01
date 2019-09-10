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

def crear_listas():
    '''Esta funcion puede crear hasta dos listas que se utilizan para varios
    de los ejercicios'''
    
    global numero_de_listas
    a = []
    b = []
    num_elementos = int(input('Por favor ingrese el numero de elementos '
                                            'que contendra la lista: -> '))
    for i in range(1, num_elementos + 1):
        a_i = int(input('Ingrese el elemento a(' + str(i) + ') de la lista: -> '))
        a.append(a_i)
    print('----------------------------------------------------------------')
    print('a', ' = ', a)
    print('----------------------------------------------------------------')
    
    if numero_de_listas == 2:
        for i in range(1, num_elementos + 1):
            b_i = int(input('Ingrese el elemento b(' + str(i) + ') de la lista: -> '))
            b.append(b_i)
        print('----------------------------------------------------------------')
        print('b', ' = ', b)
        print('----------------------------------------------------------------')
    return (a, b, num_elementos)


while True:
    clear()
    print('--------------------------------------------------------------')
    print('--Menu para la practica IV--')
    print('')
    print('1. Ejercicio 4.1 - Sumar listas.')
    print('2. Ejercicio 4.2 - Multiplicar listas.')
    print('3. Ejercicio 4.3 - Mayor numero de una lista.')
    print('4. Ejercicio 4.4 - Numero mas pequenio de una lista.')
    print('5. Ejercicio 4.5 - Numeros palindromicos.')
    print('0. Salir.')
    print('------------------------------------------------------------------')
    OPCION = int(input('Ingrese una de las opciones anteriores (0-12): -> '))
    print('------------------------------------------------------------------')
    
    if OPCION == 0:
        clear()
        print('Gracias, regrese pronto!')
        break
    elif OPCION < 0 or OPCION > 12:
        print('       Esta no es una opcion valida. Intentelo denuevo.')
        print('--------------------------------------------------------------')
        continue
        
    elif OPCION == 1:
        clear()
        numero_de_listas = 2
        d = crear_listas()
        a = d[0]
        b = d[1]
        num_elementos = d[2]
        c = []  # c =  a + b
        for i in range(num_elementos):
            c.append(a[i] + b[i])
        print('----------------------------------------------------------------')    
        print('La suma de las listas "a" y "b" introducidas es: ')
        print('')
        print('a + b = ', a, '+', b, '=', c)
        print('----------------------------------------------------------------')
        input('Ingrese un numero o letra cualquiera para continuar: -> ')


    elif OPCION == 2:
        clear()
        numero_de_listas = 2
        d = crear_listas()
        a = d[0]
        b = d[1]
        num_elementos = d[2]
        c = []  # c =  a * b
        for i in range(num_elementos):
            c.append(a[i] * b[i])
        print('----------------------------------------------------------------')    
        print('La multiplicacion de las listas "a" y "b" introducidas es: ')
        print('')
        print('a * b = ', a, '*', b, '=', c)
        print('----------------------------------------------------------------')
        input('Ingrese un numero o letra cualquiera para continuar: -> ')

    elif OPCION == 3:
        clear()
        numero_de_listas = 1
        d = crear_listas()
        a = d[0]
        num_elementos = d[2]
        a.sort()
        mayor_elemento = a[num_elementos - 1]
   
        print('----------------------------------------------------------------')    
        print('El mayor elemento de la lista "a" introducida es: ')
        print('')
        print('Mayor elemento = ', mayor_elemento)
        print('----------------------------------------------------------------')
        input('Ingrese un numero o letra cualquiera para continuar: -> ')

    elif OPCION == 4:
        clear()
        numero_de_listas = 1
        d = crear_listas()
        a = d[0]
        a.sort()
        menor_elemento = a[0]
      
        print('----------------------------------------------------------------')    
        print('El menor elemento de la lista "a" introducida es: ')
        print('')
        print('Menor elemento = ', menor_elemento)
        print('----------------------------------------------------------------')
        input('Ingrese un numero o letra cualquiera para continuar: -> ')
        

    
        









        
