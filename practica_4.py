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
    '''Esta funcion puede crear hasta dos listas con un numero arbitrario de 
    elementos enteros que se utilizan para varios de los ejercicios'''
    
    clear()
    global numero_de_listas, a, b, c, num_elementos
    a = []
    b = []
    c = []
    num_elementos = 0
    num_elementos = int(input('Por favor ingrese el numero de elementos '
                                            'que contendra la lista: -> '))
    for i in range(num_elementos):
        a_i = int(input('Ingrese el elemento a(' + str(i) + ') de la lista: -> '))
        a.append(a_i)
    print('----------------------------------------------------------------')
    print('a', ' = ', a)
    print('----------------------------------------------------------------')
    
    if numero_de_listas == 2:
        for i in range(num_elementos):
            b_i = int(input('Ingrese el elemento b(' + str(i) + ') de la lista: -> '))
            b.append(b_i)
        print('----------------------------------------------------------------')
        print('b', ' = ', b)
        print('----------------------------------------------------------------')
    return (a, b, num_elementos)

def crear_listas_de_cadenas():
    ''' Esta funcion puede crear una lista con un numero arbitrario de 
    elementos tipo cadenas que se utiliza para varios de los ejercicios'''

    clear()
    global lista
    lista = []
    num_elemento = int(input('Por favor ingrese el numero de elementos '
                                        'que contendra la lista: -> '))
    for i in range(num_elemento):
        a_i = input('Ingrese el elemento a(' + str(i) + ') de la lista: -> ')
        lista.append(a_i)
    print('----------------------------------------------------------------')
    print('lista', ' = ', lista)
    print('----------------------------------------------------------------')
    return lista

while True:
    clear()
    print('''--------------------------------------------------------------
     --Menu para la practica IV--

    1. Ejercicio 4.1 - Sumar listas.
    2. Ejercicio 4.2 - Multiplicar listas.
    3. Ejercicio 4.3 - Mayor numero de una lista.
    4. Ejercicio 4.4 - Menor numero de una lista.
    5. Ejercicio 4.5 - Contar numero de cadenas.
    6. Ejercicio 4.6 - Ordenar lista por ultimo elemento de sus tuplas.
    7. Ejercicio 4.7 - Eliminar duplicados.
    8. Ejercicio 4.8 - Verificar si una lista esta vacia.
    9. Ejercicio 4.9 - Clonar/Copiar una lista.
    10. Ejercicio 4.10 - Palabras mas largas que un numero "n" de caracteres.
    11. Ejercicio 4.11 - Verificar al menos un elemento comun entre dos listas.
    12. Ejercicio 4.12 - Eliminar elementos 0, 4 y 5 de una lista.
    0. Salir.
--------------------------------------------------------------''')
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
        crear_listas()
        for i in range(num_elementos):
            c.append(a[i] + b[i])
        print('----------------------------------------------------------------')    
        print('La suma de las listas "a" y "b" introducidas es: ', end = '\n\n')
        print('a + b = ', a, '+', b, '=', c)
        print('----------------------------------------------------------------')
        input('Ingrese un numero o letra cualquiera para continuar: -> ')


    elif OPCION == 2:
        clear()
        numero_de_listas = 2
        crear_listas()
        for i in range(num_elementos):
            c.append(a[i] * b[i])
        print('----------------------------------------------------------------')    
        print('La multiplicacion de las listas "a" y "b" introducidas es: ', end = '\n\n')
        print('a * b = ', a, '*', b, '=', c)
        print('----------------------------------------------------------------')
        input('Ingrese un numero o letra cualquiera para continuar: -> ')

    elif OPCION == 3:
        clear()
        numero_de_listas = 1
        crear_listas()
        a.sort()
        mayor_elemento = a[num_elementos - 1]
        print('----------------------------------------------------------------')    
        print('El mayor elemento de la lista "a" introducida es: ', end = '\n\n')
        print('Mayor elemento = ', mayor_elemento)
        print('----------------------------------------------------------------')
        input('Ingrese un numero o letra cualquiera para continuar: -> ')

    elif OPCION == 4:
        clear()
        numero_de_listas = 1
        crear_listas()
        a.sort()
        menor_elemento = a[0]
        print('----------------------------------------------------------------')    
        print('El menor elemento de la lista "a" introducida es: ', end = '\n\n')
        print('Menor elemento = ', menor_elemento)
        print('----------------------------------------------------------------')
        input('Ingrese un numero o letra cualquiera para continuar: -> ')

    elif OPCION == 5:
        clear()
        lista_de_muestra = ['abc', 'xyz', 'aba', '1221']
        p = 0
        print('Por favor indique la lista que desea usar (1-2): ', end = '\n\n')
        print('1. Lista de muestra. (Escriba 1.)')
        print('2. Crear una lista. (Escriba cualquier numero o letra)')
        lista = int(input('-> '))
        if lista == 1:
           lista = lista_de_muestra
        else:
            crear_listas_de_cadenas()   
        for i in range(len(lista)):
            elemento = lista[i]
            if len(elemento) >= 2 and elemento[0] == elemento[-1]:
                p += 1
        print('----------------------------------------------------------------')    
        print('El numero de cadenas en lista = ', lista, ' que cumple las condiciones'
                                                      ' dadas es: ' , end = '\n\n')
       
        print('Numero_de_Cadenas = ', p, ' cadenas.')
        print('----------------------------------------------------------------')
        input('Ingrese un numero o letra cualquiera para continuar: -> ')

    elif OPCION == 6:
        clear()
        lista_de_muestra = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
        print('Por favor indique la lista que desea usar (1-2): ', end = '\n\n')
        print('1. Lista de muestra. (Escriba 1.)')
        print('2. Crear una lista. (Escriba cualquier numero o letra)', end = '\n\n')
        print('Nota: para este caso, recuerde que los elementos deben ser tuplas', end = '\n\n')
        num_elementos = int(input('-> '))
        if num_elementos == 1:
           lista = lista_de_muestra
        else:
            l = []
            crear_listas_de_cadenas()
            for i in range(len(lista)):
                e = eval(lista[i])
                l.append(e)
            lista = l
        lista.sort(key = lambda x: x[-1])
        print('----------------------------------------------------------------')    
        print('La lista ordenada por el ultimo elemento de cada tupla es: ', end = '\n\n')
        print('lista = ', lista)
        print('----------------------------------------------------------------')
        input('Ingrese un numero o letra cualquiera para continuar: -> ')


    elif OPCION == 7:
        clear()
        crear_listas_de_cadenas()
        i = 0
        while lista.count(lista[i]) > 1:
            lista.remove(lista[i])
            if lista.count(lista[i]) == 1 and len(lista) > 1:
                i += 1
            elif lista.count(lista[i]) == 1 and len(lista) == 1:
                break
        print('----------------------------------------------------------------')    
        print('La lista sin los elementos duplicados es: ', end = '\n\n')
        print('lista = ', lista)
        print('----------------------------------------------------------------')
        input('Ingrese un numero o letra cualquiera para continuar: -> ')


    elif OPCION == 8:
        clear()
        def verificar_lista_vacia():
            global salida, salida_2
            crear_listas_de_cadenas()
            if lista != []:
                salida = '<<FALSO>>'
                salida_2 = 'no'
            else:
                salida = '<<VERDADERO>>'
                salida_2 = 'si'
            return (salida, salida_2)
        verificar_lista_vacia()
        print('----------------------------------------------------------------')    
        print('El resultado de la verificacion es: ', end = '\n\n')
        print('Verificacion = ', salida)
        print('Por tanto, la lista ', salida_2, 'esta vacia.')
        print('----------------------------------------------------------------')
        input('Ingrese un numero o letra cualquiera para continuar: -> ')

    elif OPCION == 9:
        clear()
        b = []
        a = crear_listas_de_cadenas()
        for i in range(len(a)):
            b.append(a[i])
        print('----------------------------------------------------------------')    
        print('La lista "a" ha sido copiada/clonada a la lista "b": ', end = '\n\n')
        print('a = ', a)
        print('b = ', b)
        print('----------------------------------------------------------------')
        input('Ingrese un numero o letra cualquiera para continuar: -> ')

    elif OPCION == 10:
        clear()
        lista_de_cadenas_mayor_que_n = []
        n = int(input('Ingrese la longitud de los caracteres que desea delimitar: -> '))
        crear_listas_de_cadenas()
        for i in range(len(lista)):
            if len(list(lista[i]))  > n:
                lista_de_cadenas_mayor_que_n.append(lista[i]) 
        print('----------------------------------------------------------------')    
        print('La lista de palabras con mas de ', str(n), ' caracteres es: ', end = '\n\n')
        print('lista_de_cadenas_mayor_que_n = ', lista_de_cadenas_mayor_que_n)
        print('----------------------------------------------------------------')
        input('Ingrese un numero o letra cualquiera para continuar: -> ')

    elif OPCION == 11:
        clear()
        p = 0
        numero_de_listas = 2
        crear_listas()
        for i in range(len(a)):
            if a[i] in b:
                p += 1
                break
            else:
                continue
        if p > 0:
            salida = 'Las listas "a" y "b" poseen al menos un elemento en comun.'
        else:
            salida = 'Las listas "a" y "b" no poseen elementos en comun.'
        print('----------------------------------------------------------------')    
        print(salida, end = '\n\n')
        print('----------------------------------------------------------------')
        input('Ingrese un numero o letra cualquiera para continuar: -> ')

    elif OPCION == 12:
        clear()
        lista_de_muestra = ['Rojo', 'Verde', 'Blanco', 'Negro', 'Rosa', 'Amarillo']
        print('Por favor indique la lista que desea usar (1-2): ', end = '\n\n')
        print('1. Lista de muestra. (Escriba 1.)')
        print('2. Crear una lista. (Escriba cualquier numero o letra)', end = '\n\n')
        lista = int(input('-> '))
        if lista == 1:
           lista = lista_de_muestra
           print('lista_de_muestra = ', lista_de_muestra)
        else:
            crear_listas_de_cadenas()   
        del lista[0]
        del lista[3]
        del lista[3]
        print('----------------------------------------------------------------')    
        print('La lista ha sido modificada: ', end = '\n\n')
        print('lista = ', lista)
        print('----------------------------------------------------------------')
        input('Ingrese un numero o letra cualquiera para continuar: -> ')




       
        
        

    
        









        
