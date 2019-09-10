##n=0
##if n>2:                     #if solo ejecuta el bloque de codigo si la condiciones es verdadera.
##    print("es mayor que 2")
##else:
##    print("es menor que 2")    
##    
##




##n=input('Ingrese su usuario -> ')     #Los bloques estan delimitados por expresiones de bloque.
##if n=='admin':
##    print('Bienvenido, ' + n + '!')
##else:
##    print('Acceso denegado')


##
##dia = int(input('Escriba el numero del dia'))
##
##if dia == 1:
##    print('lunes')
##elif dia == 2:
##    print('martes')
##elif dia == 3:
##    print('miercoles')
##else:
##    print('no valido')

##a = int(input('Escriba el numero a: -> '))
##b = int(input('Escriba el numero b: -> '))
##c = int(input('Escriba el numero c: -> '))
##d = int(input('Escriba el numero d: -> '))
##e = int(input('Escriba el numero e: -> '))
##
##if (a%5) == 0:
##    aa = a
##else:
##    aa=0
##if (b%5) == 0:
##    bb = b
##else:
##    bb=0
##if (c%5) == 0:
##    cc = c
##else:
##    cc=0
##if (d%5) == 0:
##    dd = d
##else:
##    dd=0
##if (e%5) == 0:
##    ee=e
##else:
##    e = 0
##print(aa + bb + cc + dd + ee)

##
##n = int(input('Inserte el numero del que desea obtener la tabla: -> '))
##for i in range(5,13):
##    print(n, '*', i, '=', n*i)
##
##
##
##
##
##
##
##m = int(input('Inserte el numero del que desea obtener la tabla: -> '))
##for i in range(n):
## print(n, '*', i, '=', n*i)


from os import system
system('clear')

billetes_de_1000 = 0
billetes_de_500  = 0
billetes_de_100  = 0
intento          = 0

while True:
    if intento == 5:
       print('Usted agoto la cantidad de intentos posibles.')
       break

    monto = int(input('##########-Por favor ingrese el monto a retirar: -> '))

    if (monto <= 0):
        print('--------Este monto no es valido, por favor ingrese otro monto.')
        intento += 1
    elif (monto > 20000):
        print('--------Usted solo puede retirar 20,000 pesos como maximo.')
        intento += 1
    elif (monto%100) > 0:
         print('--------Este cajero solo dispensa billetes igual o mayor a 100 pesos.')
         intento += 1
         
    else:                       # (100 <= monto <= 20000)
        b1 = (monto%1000)
        
        if (b1 == 0):
            billetes_de_1000 = (monto/1000)
            break
        elif (b1 != 0):
            billetes_de_1000 = (monto - (monto%1000))/1000
            
        if (b1 >= 500):
            billetes_de_500 = 1              
            billetes_de_100 = (b1 - 500)/100
            break
        elif (b1 < 500):
             billetes_de_100 = (b1%500)/100
             break

print('Billetes de 1000 pesos: -> ' + str(int(billetes_de_1000)))
print('Billetes de 500 pesos:  -> ' + str(int(billetes_de_500)))
print('Billetes de 100 pesos:  -> ' + str(int(billetes_de_100)))
        
        
        
    
    


























    


    
   


    

