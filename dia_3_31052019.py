#Teorema de la programacion estructurada: expresiones, condicionales y bucles.
#Bifurcaciones
# ':' Se denomina delimitador de  bloque en Python.
#IntelliCode

##
##def saludar():
##    print('Hola')
##saludar()

##def saludar(nombre):
##    print('Hola,', nombre, '!')
##saludar('Jose')

##def ver_tabla(numero):
##    for i in range(12):
##        i+=1
##        print(i, 'x', numero, '=', numero*i)
##ver_tabla(12)
##
##def op_aritmeticas(x,y):
##    while True:
##        print('***Elija cual de las siguientes operaciones desea realizar:***')
##        print('1-Suma.')
##        print('2-Restar.')
##        print('3-Multiplicar.')
##        print('4-Dividir.')
##        print('5-Salir.')
##        print('')
##        opcion = int(input('Ingrese la opcion deseada: -> '))
##        print('')
##        if opcion == 5:
##            print('Gracias, regrese pronto!')
##            break
##        elif opcion == 1:
##            return x+y
##        elif opcion == 2:
##            return x-y
##        elif opcion == 3:
##            return x*y
##        elif opcion == 4:
##            return x/y
##result = op_aritmeticas(8,6)
##
##print(result)

def op_aritmeticas(x,y):
    while True:
##        n1 = int(input('Escriba un numero: ->'))
##        n2 = int(input('Escriba un numero: ->'))
        print('***Elija cual de las siguientes operaciones desea realizar:***')
        print('1-Sumar.')
        print('2-Restar.')
        print('3-Multiplicar.')
        print('4-Dividir.')
        print('5-Salir.')
        print('')
        opcion = int(input('Ingrese la opcion deseada: -> '))
        print('')
        if opcion == 5:
            print('Gracias, regrese pronto!')
            break
        elif opcion == 1:
            a = x+y
            print(a)
        elif opcion == 2:
            a = x-y
            print(a)
        elif opcion == 3:
            a = x*y
            print(a)
        elif opcion == 4:
            a = x/y
            print(a)
        
result = op_aritmeticas(n1,n2)











































    
    
        
