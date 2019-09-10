n = int(input('Ingrese un numero cualquiera: -> '))
if n <= 0:
    print('Esta cantidad no es valida, por favor intentelo de nuevo')
else:
    m = 0
    p = 0
    while m < n:
        a = int(input('Ingrese un numero: -> '))
        p= p+a
        m += 1
    print('Usted ingreso ' + str(n) + ' numeros y la suma total es ' + str(p) + '.')   


