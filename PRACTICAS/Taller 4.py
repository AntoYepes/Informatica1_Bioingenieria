# ENTREGABLE 3:
    # Maria Paula Osorio
    # Antonia Yepes
#%% Se importa mysql y se hace la conexión
import mysql.connector 
servidor = 'localhost' 
usuario = 'root'
passwd = ''
db = 'entregable_3'
cnx = mysql.connector.connect(host = servidor, user = usuario, password = passwd, database = db)
cursor = cnx.cursor() 
    
#%% Funcion para que al presionar enter el algoritmo no se salga
def error():
    print('\nERROR. Intente de nuevo por favor.')
#error()
#%% Funcion para validar si el No de documento es un numero 
def docu():
    while True:
        try:
            doc = int(input('Ingrese el No de documento, recuerda max 10 numeros:'))
            return doc
        except ValueError:
            print('Error. \nIngrese un valor númerico')
# Funcion para validar si el contacto es  un numero          
def cont():
    while True:
        try:
            contacto = int(input('Ingrese el No de Contacto, recuerde max 10 numeros:'))
            return contacto
        except ValueError:
            print('Error. \nIngrese un valor númerico')
            
#%%Funcion para almacenar e importar los datos del proveedor
def info_proveedor():
    print('Ingresar un nuevo proveedor')
    d = docu()
    nombre = input('Nombre:')
    apellido = input('Apellido:')
    empresa = input('Empresa:')
    c = cont()
    email = input('Email:')
    
    var = '''INSERT INTO datos (ID, NOMBRE, APELLIDO, EMPRESA, CONTACTO, EMAIL) 
                VALUES (%s, %s, %s, %s, %s, %s) '''
    
    cursor.execute(var, (d, nombre, apellido, empresa, c, email))
    cnx.commit()
    
#info_proveedor()    
#%% Funcion para solucionar errores
# Funcion que tiene el menu principal y se importan el resto de funciones
def menu():
    while True:
        menu  = input('''Seleccione una de las siguientes opciones:
                   1. Ingresar nuevo proveedor.
                   2. Ver todos los proveedores.
                   3. Salir.
                   :''')
                   
        if menu == '1':
            info_proveedor()
        elif menu == '2':
            read = 'SELECT * FROM datos ORDER BY NOMBRE ASC'
            cursor.execute(read)
            result =cursor.fetchall() 
            for i in result:
                print('Proveedor' + '\n' +'Id:',str(i[0])+'\n'+'Nombre:',str(i[1])+'\n'+'Apellido:',str(i[2])+'\n'+'Empresa:',str(i[3])+'\n'+'Contacto:',str(i[4])+'\n'+'Email:',str(i[5]+'\n'))
                print('-'*60)
        elif menu == '3':
            break
        else:
            error()
            
if __name__ == "__main__":
    menu()