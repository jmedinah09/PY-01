
import sqlite3
    

def clear():
    """Funcion para limpiar la pantalla de la consola."""
    from os import system
    system('clear')

def crear_tabla():
    '''Funcion para crear la tabla en la base de datos'''
    sql = ''' 
    CREATE TABLE agenda (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    Nombre VARCHAR (25) NOT NULL,
    Apellido VARCHAR (25) NOT NULL,
    Telefono VARCHAR (15) NOT NULL)'''
    if c.execute(sql):
        print('Tabla creada con exito!')
    else:
        print('Ocurrio un error al crear la tabla.')

def insertar_contactos():
    '''Funcion para insertar una cantidad arbitraria de contactos en la agenda.'''
    while True:
        nombre = input('Introduzca el nombre: -> ')
        apellido = input('Introduzca el apellido: -> ')
        tel = input('Introduzca el telefono: -> ')
        argumentos = (nombre, apellido, tel)

        sql = '''
        INSERT INTO agenda (Nombre, Apellido, Telefono)
        VALUES (?, ?, ?)
        '''
        c.execute(sql, argumentos)
        print('')
        opcion = input('Desea agregar otro contacto a la agenda? (Si/No) -> ')
        if opcion in ('Si', 'SI', 'si', 's', 'S'):
            continue
        else:
            break

def listar_contactos():
    while True:
            print('-*-'*25)
            print('''
Categorias de busqueda: 
1. ID
2. Nombre
3. Apellido
4. Ver todos
0. Regresar al menu principal''', end = '\n\n')
            print('-*-'*25, end = '\n\n')
            OPCION = int(input('Indique la opcion deseada (0-4): -> '))
            print('')
            print('-*-'*25, end = '\n\n')

            if OPCION == 0:
                clear()
                break
            if OPCION == 1:
                clear()
                n = int(input('Escriba el ID: -> '))
                c.execute ('SELECT * FROM agenda WHERE id=?', (n,))
            elif OPCION == 2:
                clear()
                n = input('Escriba el nombre: -> ')
                c.execute ('SELECT * FROM agenda WHERE Nombre=?', (n,))
            if OPCION == 3:
                clear()
                n = input('Escriba el apellido: -> ')
                c.execute ('SELECT * FROM agenda WHERE Apellido=?', (n,))
            elif OPCION == 4:
                clear()
                c.execute('SELECT * FROM agenda') 
            filas = c.fetchall()
            print('-*-'*25, end = '\n\n')
            for fila in filas:
                print(fila[0],'----', fila[1], fila[2],'----', fila[3])
            print('')
            input('Presione un numero o letra cualquiera para continuar: -> ')

def editar():
    ID       = input('Escriba el id del contacto que desea editar: -> ')
    nombre   = input('Introduzca el nuevo nombre: -> ')
    apellido = input('Introduzca el nuevo apellido: -> ')
    tel      = input('Introduzca el nuevo telefono: -> ')
    sql      = '''UPDATE agenda
                  SET Nombre=?, Apellido=?, Telefono=?
                  WHERE id=?'''
    valores  = (nombre, apellido, tel, int(ID))
    c.execute(sql,valores)

def borrar():
    while True:
        print('''Borrar:

        1. Toda la agenda
        2. Un contacto
        3. Regresar al menu principal''')
        op = int(input('        -> '))
        print('')
        if op == 1:
            op = input('Se borraran todos los datos de la agenda, desea continuar? (Si/No) -> ')
            if op in ('SI', 'si', 'Si'):
                c.execute('DELETE FROM agenda')
                print('')
                input('Se han borrado todos los contactos de la agenda. Presione una tecla para continuar: -> ')
                break
            else:
                continue
        elif op == 2:
            op = int(input('Indique el id del contacto que desea eliminar'))
            c.execute('DELETE FROM agenda WHERE ID=?', (op, ))
        elif op == 3:
            break
        else:
            continue
                  
def cerrar():
    '''Funcion para guardar y cerrar la conexion en la base de datos'''
    conn.commit()
    conn.close()

while True:
    clear()
    conn = sqlite3.connect('agenda_telefonica.db')
    c = conn.cursor()
    #crear_tabla()
    print('''--------------------------------------------------------------
    ****Agenda Telefonica****

    1. Agregar contactos.
    2. Buscar contactos.
    3. Editar contactos.
    4. Eliminar contactos.
    0. Salir.

--------------------------------------------------------------''')

    OPCION = int(input('Ingrese una de las opciones anteriores (0-4): -> '))

    print('------------------------------------------------------------------')
    
    if OPCION == 0:
        clear()
        print('Gracias, regrese pronto!')
        break
    elif OPCION < 0 or OPCION > 4:
        print('       Esta no es una opcion valida. Intentelo denuevo.')
        print('--------------------------------------------------------------')
        continue
        
    elif OPCION == 1:
        clear()
        insertar_contactos()
        cerrar()

    elif OPCION == 2:
        clear()
        listar_contactos()
        cerrar()

    elif OPCION == 3:
        clear()
        editar()
        cerrar()

    elif OPCION == 4:
        clear()    
        borrar()
        cerrar()
        
        
        
        










