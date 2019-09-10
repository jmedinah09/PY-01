name = input('Hola, como te llamas? -> ')                               #Imprime un mensaje en pantalla y pregunta por el nombre.
edad = input('Mucho gusto, ' + name + '. Este programa le'              #Imprime un mensaje en pantalla y pregunta por la edad.
             ' guiara a traves de la practica de laboratorio'
             ' numero 1. Digame su edad por favor para calcular'
             ' si es usted mayor o menor de edad. -> ')                 
test = ((int(edad) - 18) >= 0)                                          #Verifica si es mayor o menor de edad.
d    = input('El resultado de su test de mayoria de edad es el siguiente:'
             '-----------'                                              #Imprime los resultados del test y pide un numero para avanzar.
             '18 years old or more = ' + str(test) + '.'
             ' Therefore, it is ' + str(test) +
             ' that you are 18 years or more.'
             '-----------'
             ' Inserte un numero cualquiera para pasar'
             ' a la otra practica. -> ')
print((int(d) >= 0))                                                    #Muestra si es verdad que se introdujo un numero
print('****************************************************************')
print('****************************************************************')
print('----------------------Practica NO. 2----------------------------')
print('****************************************************************')
print('****************************************************************')
tc   = input('Las temperaturas calurosas son el tema del momento. '     #Imprime un mensaje en pantalla y lee la temperatura en Celsius
             'Para algunas personas es un poco confuso las diferentes'
             ' unidades usadas para medir esta variable. Este programa'
             ' le transformara muy facilmente'
             ' grados Celcius a Farenheit.'
             ' Ingrese la temperatura en Celsius -> ')
tf   =  (int(tc)*(9/5)) + 32                                            #Convierte Celsius a Farenheit.
c    =  input('Esta temperatura equivale a ' + str(tf) + ' Farenheit.'  #Imprime un mensaje en pantalla con las temperaturas convertidas y lee un numero para avanzar.
             '-----------'
              ' Inserte un numero cualquiera para pasar'
              ' a la otra practica. -> ')
print((int(c) >= 0))

print('****************************************************************')
print('****************************************************************')
print('----------------------Practica NO. 3----------------------------')
print('****************************************************************')
print('****************************************************************')

cant_h   =  input('El peso molecular es la suma de las masas atomicas'
                  'de todos los atomos de una molecula de un compuesto'
                  'en especifico. Este programa calculara el peso molecular'
                  'de una molecula compuesta por atmos de hidrogeno y oxigeno.'
                  '---Ingrese la cantidad de atomos de hidrogeno: -> ')
cant_o   =  input('---Ingrese la cantidad de atomos de oxigeno: -> ')
masa_h   =  1.00784 #[u]
masa_o   =  15.999  #[u]
peso_molecular = int(cant_h)*(masa_h) + int(cant_o)*(masa_o)
e        =  input('El peso atomico de H' + str(cant_h) + 'O' + str(cant_o) +
                  ' es igual a: -> ' + str(peso_molecular) +
                  ' -----------'
                  ' Inserte un numero cualquiera para pasar'
                  ' a la otra practica. -> ')
print((int(c) >= 0))

print('****************************************************************')
print('****************************************************************')
print('----------------------Practica NO. 4----------------------------')
print('****************************************************************')
print('****************************************************************')

a1   =  input('Para hacer calculos con vectores es mejor trabajar con sus'          #Imprime un mensaje en pantalla y lee la primera componente del vector.
              ' componentes en muchos casos. Ahora trabajaremos con los vectores a y b'
              ' cuyas componentes son a1, a2, y a3, asi como, b1, b2, b3, respectivamente,'
              'es decir a=(a1,a2,a3) y b=(b1,b2,b3)'
              '---Ingrese la componente a1: -> ')                                   #Se leen las demas componentes de los dos vectores.
a2   =  input('---Ingrese la componente a2: -> ')
a3   =  input('---Ingrese la componente a3: -> ')
b1   =  input('---Ingrese la componente b1: -> ')
b2   =  input('---Ingrese la componente b2: -> ')
b3   =  input('---Ingrese la componente b3: -> ')
a    = (int(a1),int(a2),int(a3))                                                    #Contruye los dos vectores con sus respectivas componentes.
b    = (int(b1),int(b2),int(b3))
dot  =  int(a1)*int(b1) + int(a2)*int(b2) + int(a3)*int(b3)                         #Calcula el producto escalar (a.b).
b    =  input('El producto escalar entre dos vectores cualesquieras es igual a la suma de '    #Imprime un mensaje con los resultados del producto y lee un numero para avanzar.
              'las componentes con el mismo indice multiplicadas entre si. '
              'Por tanto, el producto escalar entre el vector a=' + str(a) +
              ' y el vector b=' + str(b) + ' se denota como a.b=(a1*b1 + a2*b2 + a3*b3)'
              ' y es igual a ' + str(dot) + '.'
            '-----------'
              ' Inserte un numero cualquiera para pasar'
              ' a la otra practica. -> ')
print((int(b) >= 0))

print('****************************************************************')
print('****************************************************************')
print('----------------------Practica NO. 5----------------------------')
print('****************************************************************')
print('****************************************************************')

nota1 =  input('A continuacion requeriremos que ingrese cuatro notas '      #Imprime un mensaje en pantalla y lee la nota 1.
               'a partir de las cuales calcularemos el promedio '
               'y verificaremos si corresponde a: '
               '---Cum Laude (promedio entre 85 y 89) '
               '---Magna Cum Laude (promedio entre 90 y 94) '
               '---Summa Cum Laude (promedio entre 95 y 100). '
               'Por favor, ingrese la nota_1: -> ')                         #Lee las demas notas.
nota2 =  input('Por favor, ingrese la nota_2: -> ')
nota3 =  input('Por favor, ingrese la nota_3: -> ')
nota4 =  input('Por favor, ingrese la nota_4: -> ')
prom  = (int(nota1) + int(nota2) + int(nota3) + int(nota4))/4               #Calcula el promedio
Qmao  = (int(prom) <= 69)
ChC   = (70 <= int(prom) <= 84)                                             #Verifica a cual de las clasificaciones corresponde.
CL    = (85 <= int(prom) <= 89)
MCL   = (90 <= int(prom) <= 94)
SCL   = (95 <= int(prom) <= 100)
print('El promedio es: -> ' + str(prom) + ' por lo tanto: ')                #Imprime en pantalla los resultados de la clasificacion.
print('a. Esta usted quemao? -' + str(Qmao) + '.')
print('b. Es usted Chepa Cum Laude -' + str(ChC) + '.')
print('c. Es usted Cum Laude? -' + str(CL) + '.')
print('d. Es usted Magna Cum Laude? -' + str(MCL) + '.')
print('e. Es usted Summa Cum Laude? -' + str(SCL) + '.')
e     =  input('-----------'                                                #Se despide y lee un numero para terminar.
               'Gracias, regrese pronto ' + name + '!'
               ' Inserte un numero cualquiera para salir -> ')
               
               
