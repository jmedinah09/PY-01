#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  9 11:40:40 2019

@author: jmedinah09

"""
def clear():
    """Funcion para limpiar la pantalla de la consola."""
    from os import system
    system('clear')


while True:
    clear()
    print('--Menu para la practica III--')
    print('')
    print('1. Ejercicio 3.1 - Potenciacion.')
    print('2. Ejercicio 3.2 - Numero a letras.')
    print('3. Ejercicio 3.3 - A;o bisiesto.')
    print('4. Ejercicio 3.4 - Numeros iguales.')
    print('5. Ejercicio 3.5 - Numeros palindromicos.')
    print('6. Salir.')
    print('------------------------------------------------------------------')
    OPCION = int(input('Ingrese una de las opciones anteriores (1-6): -> '))
    print('------------------------------------------------------------------')
    
    if OPCION == 6:
        clear()
        print('Gracias, regrese pronto!')
        break
    
    elif OPCION == 1:
        clear()
        def potenciacion(x,y):
            '''Esta funcion potencia dos numeros'''   
            return x**y
        
        print('Este programa calcula la potencia de un numero "x" elevado a la'
                      ' "y".')
        x = float(input('Ingrese la base "x": -> '))
        y = float(input('Ingrese el exponente "y": -> '))
        RESULT_1 = potenciacion(x,y)
        print('--------------------------------------------------------------')
        print('La potencia es ' + str(x) + "^" + str(y) + " = " + str(RESULT_1))
        print('--------------------------------------------------------------')
        input('Ingrese un numero o letra cualquiera para continuar: -> ')
        
        
    elif OPCION == 2:
        clear()
        
        def num_a_letras(num):
            if not 1<=num<=10:
                print('Esta opcion no es valida. Saliendo del programa.')
            elif num == 1:
                numero = 'Uno.'
            elif num == 2:
                numero = 'Dos.'
            elif num == 3:
                numero = 'Tres.'
            elif num == 4:
                numero = 'Cuatro.'
            elif num == 5:
                numero = 'Cinco.'
            elif num == 6:
                numero = 'Seis.'
            elif num == 7:
                numero = 'Siete.'
            elif num == 8:
                numero = 'Ocho.'
            elif num == 9:
                numero = 'Nueve.'
            elif num == 10:
                numero = 'Diez.'
            return numero
        num = int(input('Ingrese un numero del 1 al 10 para verlo escrito: -> '))
        RESULT_2 = num_a_letras(num)
        print('--------------------------------------------------------------')
        print('El numero ' +'"'+str(num)+'"' + ' se escribe: -> ' + str(RESULT_2))
        print('--------------------------------------------------------------')
        input('Ingrese un numero o letra cualquiera para continuar: -> ')

    elif OPCION == 3:
        clear()

        def a_bisiesto(a):
            '''Año bisiesto es el divisible entre 4, excepto que sea año secular
               (último de cada siglo, terminado en «00»), en cuyo caso también
               ha de ser divisible entre 400. Fuente: Wikipedia'''
            if (a%4 == 0 and (a%100 != 0 or a%400 == 0)):
                b = 'El ano ' + str(a) + ' es bisiesto.'
            else:
                b = 'El ano ' + str(a) + ' no es bisiesto.'
            return b
        a = int(input('Ingrese un ano para saber si es bisiesto: -> '))
        RESULT_3 = a_bisiesto(a)
        print('--------------------------------------------------------------')
        print(RESULT_3)
        print('--------------------------------------------------------------')
        input('Ingrese un numero o letra cualquiera para continuar: -> ')

    elif OPCION == 4:
        clear()

        def numeros_iguales(a,b):
            '''Esta funcion evalua si dos numeros "a" y "b" son iguales'''
            a == b
            if True:
                 c = 'VERDADERO'
            else:
                 c = 'FALSO'
            return c
        a = input('Ingrese un numero cualquiera: -> ')
        b = input('Ingrese otro numero para comparar si son iguales: -> ')
        RESULT_4 = numeros_iguales(a,b)
        print('--------------------------------------------------------------')
        print('Es <<' + RESULT_4 + '>> que ' + a + ' y ' + b + ' son iguales.')
        print('--------------------------------------------------------------')
        input('Ingrese un numero o letra cualquiera para continuar: -> ')
    
    elif OPCION == 5:
        clear()

        def digitos_palindromo():
            '''Esta funcion encuentra el palindromo mas grande del producto de
               dos numeros de 3 digitos'''
            palindromo = 0
            for i in range(100,1000):
                for j in range(100,1000):
                    mult = i*j
                    if str(mult) == str(mult)[::-1] and mult > palindromo:
                        palindromo = mult
            print('--------------------------------------------------------------')
            print('El numero palindromico mas grande del producto de dos numeros'
                  ' de 3 digitos es: -> ' + str(palindromo))
            print('--------------------------------------------------------------')
        digitos_palindromo()
        input('Ingrese un numero o letra cualquiera para continuar: -> ')

        















        
        
        
        
    
