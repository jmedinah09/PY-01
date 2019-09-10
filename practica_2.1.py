
while True:
    
    print('***Elija cual de las siguientes tareas desea realizar:***')
    print('1-Convertir grados Celcius a Farenheit.')
    print('2-Convertir dolares a pesos.')
    print('3-Convertir metros a pies.')
    print('4-Salir.')
    print('')
    opcion = int(input('Ingrese la opcion deseada: -> '))
    print('')

    if opcion == 4:
        print('Gracias, regrese pronto!')
        break
    elif (opcion <= 0 or opcion >= 5 ):
        print('Esta opcion no es valida, por favor ingrese otra opcion.')
        print('')
    elif opcion == 1:
        tc   = input('Ingrese la temperatura en Celsius: -> ')
        print('')
        tf   =  (int(tc)*(9/5)) + 32                                            
        print('---Esta temperatura equivale a ' + str(tf) + ' Farenheit.')
        print('')
    elif opcion == 2:
        dolares = input('Ingrese la cantidad que desea convertir a pesos: -> ')
        print('')
        pesos = int(dolares)*50
        print('---Esta cantidad equivale a ' + str(pesos) + ' pesos.')
        print('')
    elif opcion == 3:
        metros = input('Ingrese la cantidad en metros que desea convertir: -> ')
        print('')
        print('---' + str(metros) + ' metros equivale a ' + str(int(metros)*3.25) + ' pies')
        print('')
           
