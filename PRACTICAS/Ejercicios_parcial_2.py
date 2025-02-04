#%%DIAPOSITIVAS PARCIAL 2
#%%CALCULADORA
#permita escoger las opciones como el sigt menu:
#1.suma 2.resta 3.mult 4.division 5. salir
def suma(a,b):
    return a + b

def resta(a,b):
    return a - b

def multiplicacion(a,b):
    return a * b

def division(a,b):
    return a/b

while True:
    menu = input('''
    1.Suma
    2.Resta
    3.Multiplicacion
    4.Division
    5.Salir
    ''')
   
    if menu == '1':
        a = int(input('Ingrese el valor de a: '))
        b = int(input('Ingrese el valor de b: '))
        print(suma(a,b))
    elif menu == '2':
        a = int(input('Ingrese el valor de a: '))
        b = int(input('Ingrese el valor de b: '))
        print(resta(a,b))
    elif menu == '3':
        a = int(input('Ingrese el valor de a: '))
        b = int(input('Ingrese el valor de b: '))
        print(multiplicacion(a,b))
    elif menu == '4':
        a = int(input('Ingrese el valor de a: '))
        b = int(input('Ingrese el valor de b: '))
        print(division(a,b))
    elif menu == '5':
        break


#%%HISTORIA CLINICA
#Almacenar nombre, cc, edad, eps
#ciclo de prefer, tuplas anidadas, en listas, lista inicia vacia, menu con opciones 
#buscar si paciente esta con in
def registro():
    paciente = []
    for i in ['nombre', 'identificacion', 'edad', 'eps']:
        a = input(f'Ingrese el {i} del paciente: ')
        paciente.append(a)    
    return tuple(paciente)


def busqueda():
    search = str(input('Ingrese el nombre del paciente que desea buscar: '))
    for i in lista_registro:
        if search in i:
            print(i)
    return search
    
 



while True:
    menu = input('''
    1.Ingresar datos del paciente
    2.Ingresar otro paciente
    3.Buscar algun paciente
    4.Salir
    ''')
    
    if menu == '1':
        print(registro())
    elif menu == '2':
        print(busqueda())
    elif menu == '3':
        print()
        break
    
#            
#prueba = [('Antonia', '1234', '12', 'Sura'),
         # ('Ruben', '6789', '59', 'Sura'),
          #('Beatriz', '567', '12', 'Sura'),
          #('Gabriel', '345', '34', 'Sura')]

#busqueda = 'Antonia'
#reg_prueba = ('Ruben', '6789', '59', 'Sura')
#busqueda(prueba, 'Antonia')
#%%HISTORIA CLINICA
#prueba para buscar paciente
paciente = ('Lia', '234', '9', 'sura')
lista_registro = [('Lia', '234', '9', 'sura'),
                 ('Rube', '987', '26', 'sura'),
                 ('More', '27653', '30', 'sura'),
                 ('gabriel', '98552', '27', 'sura')]

for i in lista_registro:
    if 'Lia' in i:
        print(i)
        
busqueda = 'Rube'
for i in lista_registro:
    if busqueda in i:
        print(i)

#almacenar tupla en lista
lista = []
paciente = ('Lia', '234', '9', 'sura')
lista.append(paciente)
print(lista)

#almacenar base_Datos
base_datos = []
paciente = ('Lia', '234', '9', 'sura')
base_datos.append(paciente)
#%%TEOREMA SEN Y COS
from math import sin, cos, sqrt, radians, degrees
#Lado-Angulo-Lado 
#Angulo-Lado-Angulo

while True:
    menu = input('''
    1.Lado-Angulo-Lado
    2.Angulo-Lado-Angulo
    3.Salir
    ''')
    
    if menu == '1':
        a = float(input('Ingrese el valor del lado a: '))
        C = float(input('Ingrese el valor del angulo C: '))
        b = float(input('Ingrese el valor del lado b: '))
        
        c = sqrt(a**2 + b**2 - 2*a*b*cos(radians(C)))
        A = a*sin((a*sin(radians(c)))/c)
        A = degrees(A)
        B = 180 - (A + C)
        
        print(f'El valor de c es : {c} ')
        print(f'El valor de A es : {A}')
        print(f'El valor de B es : {B}')
        
    elif menu == '2':
        A = float(input('Ingrese el valor del angulo A: '))
        c = float(input('Ingrese el valor del lado c: '))
        B = float(input('Ingrese el valor del lado B: '))
        
        C = 180 - (A + B)
        a = (c*sin(radians(A))/sin(radians(C)))
        b = (c*sin(radians(B))/sin(radians(C)))
        
        print(f'El valor de c es: {c}')
        print(f'El valor de A es: {A}')
        print(f'El valor de B es: {B}')
        
    elif menu == '3':
        break
    
#%%CALENDARIO
def ingreso_fecha():
    fecha = []
    for i in ['dia','mes','año']:
        a = input(f'Ingrese el {i} corespondiente: ')
        fecha.append(a)
    return fecha

#ingreso_fecha()

def prueba_año_bis(fecha, año):
    for i in fecha:
        if año in i:
            if int(año) % 4 == 0:
                if int(año) % 100 == 0:
                    if int(año) % 400 == 0:
                        print(True)
                    else:
                        print(False)
                else:
                    print(True)
            else:
                print(False)
            
#fecha = ['24','04', '2005'] 
#año = '2005'    

#prueba_año_bis(fecha, año)

def fecha_dia_despues(fecha):
    cambio_fecha = []
    x = 0
    x = fecha[0]
    x = int(x) + 1
    cambio_fecha.append(str(x))
    cambio_fecha.append(fecha[1])
    cambio_fecha.append(fecha[2])
    print(cambio_fecha)

#date = ['24', '07', '2004']
#fecha_dia_despues(date)
 
while True:
    menu = input('''
    1.Ingrese la fecha.
    2.Salir.
    ''')
    
    if menu == '1':
        fecha = ingreso_fecha()
        año = fecha[2]
        prueba_año_bis(fecha, año)
        fecha_dia_despues(fecha)
    elif menu == '2':
        print('Gracias por utilizar nuestro calendario :v')
        break
    

#%%2nd OPCION CALENDARIO  
#f'{}-{}-{}'  
def ingreso_fecha():
    from datetime import datetime    
    date_str = str(input('Ingrese la fecha que desea modificar asi mm-dd-aaaa: '))
    date_object = datetime.strptime(date_str, '%m-%d-%Y')
    fecha = date_object.date()    
    año = date_object.year
    return (fecha, año)
        
#ingreso_fecha()

def prueba_año_bis(fecha, año):
    for i in fecha:
        if año in i:
            if int(año) % 4 == 0:
                if int(año) % 100 == 0:
                    if int(año) % 400 == 0:
                        print(True)
                    else:
                        print(False)
                else:
                    print(True)
            else:
                print(False)
                
def conversion_fecha(fecha):
    day = 0
    change_date = []
    from datetime import datetime    
    date_object = datetime.strptime(fecha, '%m-%d-%Y')
    day = date_object.day
    day = day + 1
    change_date.append(date_object.month)
    change_date.append(day)
    change_date.append(date_object.year)
    return change_date

#fecha = '04-24-1997'
#conversion_fecha(fecha)

while True:
    menu = input('''
    1.Ingrese la fecha a convertir.
    2.Salir.
    ''')
    if menu == '1':
        fecha = ingreso_fecha()
        prueba_año_bis(fecha, año)
        conversion_fecha(fecha)
    elif menu == '2':
        print('Gracias por utilizar nuestra plataforma :v')
        break
    
#%%CALCULADORA CON FUNCION LAMBDA Y TRY AND EXCEPT  
while True:
    menu = input('''
    1.Suma.
    2.Resta.
    3.Multiplicacion.
    4.Division.
    5.Salir.
    ''')
    if menu == '1':
        while True:
            suma = lambda x , y : x + y
            try: 
                x = int(input('Ingrese el primer numero: '))
                y = int(input('Ingrese el segundo numero: '))
                print(suma(x, y))
                break
            except ValueError: 
                print('ERROR')

    elif menu == '2':
        while True:
            resta = lambda x , y : x - y
            try: 
                x = int(input('Ingrese el primer numero: '))
                y = int(input('Ingrese el segundo numero: '))
                print(resta(x, y))
                break
            except ValueError:
                print('ERROR')

    elif menu == '3':
        while True:
            multip = lambda x , y : x * y
            try:
                x = int(input('Ingrese el primer numero: '))
                y = int(input('Ingrese el segundo numero: '))
                print(multip(x, y))
                break
            except ValueError:
                print('ERROR')
                
    elif menu == '4':
        while True:
            division = lambda x , y : x / y
            try:
                x = int(input('Ingrese el primer numero: '))
                y = int(input('Ingrese el segundo numero: '))
                print(division(x, y))
                break
            except ZeroDivisionError:
                print('Esta division no es posible')
            except ValueError:
                print('ERROR')

    elif menu == '5':
        print('Gracias por utilizar la calculadora :v')
        break
    

#%%COMPRADOR ROPA EJERCICIO PROFE
camisetas = {1: ['Polo', 'Blanca', 15], 
             2:['Polo', 'Azul', 15], 
             3: ['Polo', 'Roja', 15], 
             4: ['Polo', 'Amarilla',15],
             5: ['Cuello redondo', 'Gris', 12], 
             6: ['Cuello redondo', 'Negro', 12], 
             7: ['Cuello redondo', 'Verde',12]}

jean = {1: ['Azul', 20], 
        2:['Verde', 20], 
        3:['Café', 20], 
        4:['Negro', 20], 
        5:['Gris', 20]}

zapatos = {1:['Botas', 'Café', 25], 
           2: ['Tenis', 'Azul', 20], 
           3:['Botas', 'Negro', 25], 
           4: ['Tenis', 'Blanco',20]}

compra = []

while True:
    nombre= input('Ingrese su nombre : ')
    compra.append(nombre)
     
    while True:    
        try:
            num_id = int(input('Ingrese su numero de identificacion: '))
            break
        except ValueError:
            print('Ingreso algun dato erroneo')
    compra.append(num_id)
    direccion = input('Ingrese su direccion: ')
    compra.append(direccion)
    telefono = input('Digite el numero de tel o cel: ')
    compra.append(telefono)
    
    print('***seleccione una camiseta***')
    for i in range(1,len(camisetas) + 1):
        print(i, camisetas[i][0], camisetas[i][1], ':', camisetas[i][2])
    while True:    
        try:
            c = int(input('Ingrese la camiseta que selecciono: '))
            break
        except ValueError:
            print('Selecciono una opcion no valida')
    compra.append(camisetas[i])
    
    print('***seleccione un jean***')
    for i in range(1,len(jean) + 1):
        print(i, jean[i][0], ':', jean[i][1])
    while True:
        try:
            c = int(input('Ingrese el jean seleccionado: '))
            break
        except ValueError:
            print('Selecciono una opcion no valida')
    compra.append(jean[i])
            
    print('***seleccione unos zapatos***')
    for i in range(1,len(zapatos) + 1):
        print(i, zapatos[i][0], zapatos[i][1], ':', zapatos[i][2])
    while True:    
        try:
            c = int(input('Ingrese la camiseta que selecciono: '))
            break
        except ValueError:
            print('Selecciono una opcion no valida')
    compra.append(zapatos[i])
            
    print('****INFORMACION DE LA COMPRA***')
    print('comprador:',compra[0])
    print('Id:', compra[1])
    print('direccion:', compra[2])
    print('-----Descripcion de los productos------')
    print(compra[4][0], compra[4][1], compra[4][2])
    print('jean', compra[5][0], compra[5][1])
    print(compra[6][0], compra[6][1], compra[6][2])
    print('TOTAL COMPRA: ', compra[4][2] + compra[5][1] + compra[6][2]) 
    
    op = input('Desea realizar otra compra? 1- si o 2-No')
    if op == '1':
        compra = []
    else:
        break
    #break
        
#%%VALIDAR NUMEROS FUNCION
def validar_numer():
        while True:
            try:
                x = int(input('Ingrese el numero de su producto de seleccion: '))
                break
            except ValueError:
                print('Ingreso un dato no valido')
        return x

#validar_numero()
 
cliente = []
for i in ['nombre', 'cc', 'direccion', 'telefono']:
    a = input(f'Ingrese {i} del cliente: ')
    cliente.append(a)
    
print(cliente)
print('nombre:', cliente[0])    
print('cc: ', cliente[1])
print('direccion: ', cliente[2])
print('telefono: ', cliente[3])



#%%COMPRADOR ROPA VERSION MIA
def validar_numero():
        while True:
            try:
                x = int(input('Ingrese el numero de su producto de seleccion: '))
                break
            except ValueError:
                print('Ingreso un dato no valido')
        return x

#validar_numero()
                
camisetas = {1: ['Polo', 'Blanca', 15], 
             2:['Polo', 'Azul', 15], 
             3: ['Polo', 'Roja', 15], 
             4: ['Polo', 'Amarilla',15],
             5: ['Cuello redondo', 'Gris', 12], 
             6: ['Cuello redondo', 'Negro', 12], 
             7: ['Cuello redondo', 'Verde',12]}

jean = {1: ['Azul', 20], 
        2:['Verde', 20], 
        3:['Café', 20], 
        4:['Negro', 20], 
        5:['Gris', 20]}

zapatos = {1:['Botas', 'Café', 25], 
           2: ['Tenis', 'Azul', 20], 
           3:['Botas', 'Negro', 25], 
           4: ['Tenis', 'Blanco',20]}

compra = []

while True:
    menu = input('''
    1.Datos cliente
    2.Camisetas.
    3.Jeans.
    4.Zapatos.
    5.Salir.
    ''')
    
    if menu == '1':
        cliente = []
        for i in ['nombre', 'cc', 'direccion', 'telefono']:
            a = input(f'Ingrese {i} del cliente: ')
            cliente.append(a)
    
        compra.append(cliente)
      
    elif menu == '2':
        print('***Seleccione su camisa de preferencia***')
        for i in range(1,len(camisetas) + 1):
            print(i, camisetas[i][0], camisetas[i][1], ':', camisetas[i][2])
        validar_numero()
        compra.append(camisetas[i])   
        
        print()
    elif menu == '3':
        print('***seleccione su jean de preferencia***')
        for i in range(1, len(jean) + 1):
            print(i, jean[i][0], ':',jean[i][1])
        validar_numero()
        compra.append(jean[i])
        
        print('ok')
    elif menu == '4':
        print('***seleccione sus zapatos de preferencia***')
        for i in range(1, len(zapatos) + 1):
            print(i, zapatos[i][0], zapatos[i][1], ':', zapatos[i][2])
        validar_numero()
        compra.append(zapatos[i])
        
        print('ok')
    elif menu == '5':
        print('cliente:',compra[0][0],'\ncedula:', compra[0][1],'\ndireccion:', compra[0][2],'\ncedula:', compra[0][3])
        print('camisetas:',compra[1][0], compra[1][1], compra[1][2])
        print('jean:', compra[2][0], compra[2][1])
        print('zapatos:', compra[3][0], compra[3][1], compra[3][2])
        break  

#%%EJEMPLOS VARIOS DICCIONARIOS COMPRENDIENDO EL TEMA
dicts = {}
keys = range(4)
values = ["Hi", "I", "am", "John"]
for i in keys:
        dicts[i] = values[i]
print(dicts)


dicts = {}
equipo = ['cama','tv','respirador','silla']
for i in keys:
    dicts[i] = equipo
print(dicts)
 
dicts['algo'] = equipo

#OTRO EJEMPLO
diccionario = {}
equipos = ['respirador','rayos_x','pc']
diccionario['equipo1'] = 5555
diccionario['equipo2'] = 1
diccionario['equipo3'] = 3446
print(diccionario)
len(diccionario)


def key_value(equipo):
    dicts = {}
    dicts['x'] = equipo
    print(dicts)
    
#equipos = ['respirador','rayos_x','pc']
#key_value(equipo)
dicts = {}
equipos = ['respirador','rayos_x','pc']
for i in range(10):
    print(f'Activo {i}', equipos)   
    
#%% BUSQUEDA EN DICCIONARIO
diccionario = {'B-2020-1':['tv','cama','silla'],
               'S-2020-1':['ventilador','mueble','mesa'],
               'I-2020-1': ['Ventana','puerta','cuaderno']} 
diccionario.keys()
key_list = list(diccionario)

for key in diccionario.keys():
    x = input('Ingrese el numero del key')
    print('key: {}, index: {}'.format(key, key_list.index(key)))
#%%SEGUNDO INTENTO BUSQUEDA DICCIONARIO
a_dictionary = {"a": 1, "b": 2, "c":3} 
keys_list = list(a_dictionary)
key = keys_list[1]
print(key)

diccionario = {'B-2020-1':['tv','cama','silla'],
               'S-2020-1':['ventilador','mueble','mesa'],
               'I-2020-1': ['Ventana','puerta','cuaderno']} 
print(diccionario.keys())
print(type(diccionario.keys()))
key_list = list(diccionario.keys())
print(type(key_list))
x = int(input('Ingrese el index de la busqueda:'))
key = key_list[x - 1]
print(key)
#%%
diccionary = {}
equipos = ['cama','silla','tv']
equipos_2 = ['tv','ventilador','cableado']
equipos_3 =['cosa','rrrr','iiiii']
diccionary['a'] = equipos
diccionary['b'] = equipos_2
diccionary['c'] = equipos_3
print(len(diccionary.keys()))
print(diccionary)
 
#%%
diccc = {}
equipo =['x','y','z']
equipo_1 = ['w','s','a']
equipo_2 = ['e','r','g']
diccc[len(diccc.keys())] = equipo
diccc[len(diccc.keys())] = equipo_1
diccc[len(diccc.keys())] = equipo_2
print(diccc)
#%%
#MANTENIMIENTO
class my_dictionary(dict):  
  
    # __init__ function  
    def __init__(self):  
        self = dict()  
      
    # Function to add key:value  
    def add(self, key, value):  
        self[key] = value  
  
# Main Function  
dict_obj = my_dictionary()  
  
# Taking input key = 1, value = Geek 
dict_obj.key = input("Enter the key: ") 
dict_obj.value = input("Enter the value: ") 
  
dict_obj.add(dict_obj.key, dict_obj.value)   
  
print(dict_obj)
#%%
ubicaciones_b = {1:['UCI - Unidad de Cuidados Intensivos'],
                 2:['UCE - Unidad de Cuidados Especiales'],
                 3:['Quirófanos'],
                 4:['Urgencias'] }

ubicaciones_i = {1:['Sótano 1'],
                 2:['Sótano 2'],
                 3:['Terraza'] }

ubicaciones_s = {1:['Consultorio 1'],
                 2:['Contabilidad'],
                 3:['Gerencia'],
                 4:['Recursos Humanos']}

 
ubicaciones = []

print('***seleccione la ubicacion del equipo en biomedico***')
for i in range(1, len(ubicaciones_b) + 1):
    print(i, ':', ubicaciones_b[i][0], ubicaciones_b[i][1])
while True:
    try:
        b = int(input('Ingrese la ubicacion del equipo: '))
        break
    except ValueError:
        print('\nselecciono una opcion no valida.\nVuelva a intentarlo.')
ubicaciones.append(ubicaciones_b[i])

print('***seleccione la ubicacion del equipo en infraestructura***')
for i in range(1, len(ubicaciones_i) + 1):
    print(i, ':', ubicaciones_i[i][0])
while True:
    try:
        inf = int(input('Ingrese la ubicacion del equipo: '))
        break
    except ValueError:
        print('\nselecciono una opcion no valida.\nVuelva a intentarlo.')
ubicaciones.append(ubicaciones_i[i])


print('***seleccione la ubicacion del equipo en sistemas***')
for i in range(1, len(ubicaciones_s) + 1):
    print(i, ':', ubicaciones_s[i][0])
while True:
    try:
        s = int(input('Ingrese la ubicacion del equipo: '))
        break
    except ValueError:
        print('\nselecciono una opcion no valida.\nVuelva a intentarlo.')
ubicaciones.append(ubicaciones_s[i])

print(ubicaciones)
print('ubicacion_biomedica:', )
print('ubicacion_infraestructura: ', ubicaciones[1])
print('ubicaciones_sistemas: ', ubicaciones[2])

#%%
a = list(ubicaciones_b.values())
print(ubicaciones_b[1]['UCI'])

for i in a:
    print('1:', a[0], ' \n2:', a[1], '\n3:', a[2], '\n4:', a[3])
    while True:
        try:
            x = input('Ingrese la ubicacion correspondiente: ')
            break
        except ValueError:
           print('Ingreso una opcion no valida.\nIntentelo de nuevo')