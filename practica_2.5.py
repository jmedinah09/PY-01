def clear():
    from os import system
    system('clear')
clear()

while True:
    clear()
    print('**************************************************************')
    print('**************************************************************')
    banco = input('Ingrese el nombre del Banco del que desea debitar: -> ')
    print('--------------------------------------------------------------')
    print('                  Bienvenido al Banco ' + banco + '.')
    
    if banco == 'ABC':
        monto_max = 10000
    else:
        monto_max = 20000
        
    billetes_de_1000_disponibles = 9   # Numero de billetes disponibles en el cajero.
    billetes_de_500_disponibles  = 19
    billetes_de_100_disponibles  = 99
    
    billetes_de_1000 = 0               #Numero de billetes a dispensar al cliente por el cajero
    billetes_de_500  = 0
    billetes_de_100  = 0
    
    intento          = 0

    while True:
        if intento == 5:
            print('--------Usted agoto la cantidad de intentos posibles.')
            break
        monto = int(input('##########-Por favor ingrese el monto a retirar: -> '))
        if (monto <= 0):
            print('--------Este monto no es valido, por favor ingrese otro monto.')
            intento += 1
        elif (monto > monto_max):
            print('--------Lo sentimos, el banco ' + banco + ' solo dispensa ' + str(monto_max) + ' pesos por dia.' )
            intento += 1
        elif (monto%100) > 0:
             print('--------Este cajero solo dispensa billetes igual o mayor a 100 pesos.')
             intento += 1
             
        else:                  #(100 <= monto <= 20000-c/100):
            b1 = (monto%1000)
            
            if (b1 == 0):
                billetes_de_1000 = (monto/1000)
                if billetes_de_1000 > 9:
                    billetes_de_1000 = 9
                    billetes_de_500 = (monto - 9000)/500
                    if billetes_de_500 > 19:
                        billetes_de_500 = 19
                        billetes_de_100  = (monto - (9000+9500))/100
                    break
                    
            if (b1 != 0):
                billetes_de_1000 = (monto - (monto%1000))/1000
                if billetes_de_1000 > 9:
                    billetes_de_1000 = 9
                    billetes_de_500 = ((monto - (monto%1000)) - 9000)/500
                    if billetes_de_500 > 19:
                        billetes_de_500 = 19
                        billetes_de_100  = (monto - (9000+9500))/100
                        break
                
            if (b1 >= 500):
                billetes_de_500 += 1
                billetes_de_100 = (monto%500)/100
                if billetes_de_500 > 19:
                    billetes_de_500 = 19
                    billetes_de_100  = (monto - (9000+9500))/100
                break
            elif (b1 < 500):
                 billetes_de_100 += (b1%500)/100
                 break
    monto_dispensado = (billetes_de_1000*1000) + (billetes_de_500*500) + (billetes_de_100*100)
    print('--------------------------------------------------------------')
    print('--------------------------------------------------------------')
    print('El monto dispensado es ' + str(int(monto_dispensado)) + ' pesos.')
    print('--------------------------------------------------------------')
    print('--------------------------------------------------------------')
    print('Billetes de 1000 pesos: -> ' + str(int(billetes_de_1000)))
    print('Billetes de 500 pesos:  -> ' + str(int(billetes_de_500)))
    print('Billetes de 100 pesos:  -> ' + str(int(billetes_de_100)))
    
    opcion = input('Desea realizar otra transaccion? -Si. -No. -> ')
    if (opcion == 'Si' or opcion == 'si' or opcion == 's' or opcion == 'S'):
        continue
    else:
        print('**************************************************************')
        print('**************************************************************')
        print('Gracias por utilizar nuestros servicios.')
        print('**************************************************************')
        print('**************************************************************')
        break
































   





























