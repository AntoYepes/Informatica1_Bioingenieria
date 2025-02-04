def error():
    print('\nERROR-Ingreso una opcion no valida.\nntentalo de nuevo.')
    
def validar_serial():
        while True:
            try:
                serial = int(input('Ingrese el serial del equipo: '))
                break
            except ValueError:
                print('\nIngreso un dato no valido.\nrecuerde son solo numeros')
        return serial

def validar_factura():
    while True:
        try:
            factura = int(input('Ingrese el numero de la factura: '))
            break
        except ValueError:
            print('\nIngreso un dato no valido.\nRecuerde son solo numeros.')
        return factura

def validar_num_activo():
    while True:
        try:
            valid_activo = int(input('Ingrese la fecha de compra del equipo: '))
            break
        except ValueError:
            print(('\nIngreso un dato no valido.\nRecuerde son solo numeros.'))
    return valid_activo


def mantenimiento():
    d = {}
    for i in ['preventivo','predictivo','calibracion']:
        valores = input(f'Ingrese {i}:') # here i have taken values as integers
        d[f'{i}'] = valores
    return d

#mantenimiento()

def datos_compra():
    f = {}
    
    for j in ['garantia','factura']:
        valores = input(f'Ingrese {j}: ') 
        f[f'{j}'] = valores
    return f
    
#datos_compra()

def activo_1():
    activo = {}
    for k in ['equipo','serial','marca','ubicacion']:
        valores = input(f'Ingrese {k}: ')
        activo[f'{k}'] = valores
    
    activo['mantenimiento'] = mantenimiento()
    activo['datos_compra'] = datos_compra()
    return activo   

activo_1()

#%%
def buscar_activo(diccionario):
    num_activo = int(input('\nIngrese el numero de activo a buscar: '))
    key_list = list(diccionario.keys())
    key = key_list[num_activo - 1]
    value = diccionario.get(key)
    print(value)
    
    
diccionario = {'B-2020-1':{'equipo':'monitor',
                           'serial':'1234556',
                           'marca':'medtech',
                           'ubicacion':'UCI',
                           'mantenimiento':{'preventivo':'anual',
                            'predictivo':'trime',
                            'calibracion':'anual'},
                           'datos_compra':{'garantia':'si','fatura':'123455'}},
               'I-2020-1':{'equipo':'cama',
                           'serial':'9855444',
                           'marca':'roble',
                           'ubicacion':'ECI',
                           'mantenimiento':{'preventivo':'trimesl',
                            'predictivo':'semest',
                            'calibracion':'mensual'},
                           'datos_compra':{'garantia':'no','fatura':'27464585'}}}

#buscar_activo(diccionario)
    
#%%

dicts = {}
cont_b = 1
cont_s = 1
cont_i = 1
while True:  
    select_area = int(input('''
    1. Biomedica.
    2. sistemas.
    3. Infraestructura.
    '''))
    if select_area == 1:
        name_b = 'B-2020-' + str(cont_b)
        cont_b += 1
        dicts[name_b] = activo_1()
        print(dicts)
    elif select_area == 2:
        name_s = 'S-2020' + str(cont_s)
        cont_s += 1
        dicts[name_s] = activo_1()
        print(dicts)
    elif select_area == 3:
        name_i = 'I-2020' + str(cont_i)
        cont_i += 1
        dicts[name_i] = activo_1()
        print(dicts)
        break
        
#%%
ubicaciones_b = {1:'UCI - Unidad de Cuidados Intensivos',
                 2:'UCE - Unidad de Cuidados Especiales',
                 3:'Quirófanos',
                 4:'Urgencias' }

ubicaciones_i = {1:'Sótano 1',
                 2:'Sótano 2',
                 3:'Terraza' }

ubicaciones_s = {1:'Consultorio 1',
                 2:'Contabilidad',
                 3:'Gerencia',
                 4:'Recursos Humanos'}

type(ubicaciones_b.items())
input(''.join(str(x) + '.' + y + '\n' for x, y in ubicaciones_b.items()))

x = input('ingrese \n fdafda')

    
#%%ANALISIS DEL PROBLEMA
#Nos piden que el usurio pueda ingresar la informacion del equipo, como tambien buscarlo o obtener la informacion de uno en especifico
#la solucion dada es crear un meno principal con las opciones anteriores, donde internamente habra otro menu para clasificar de acuerdo a su area
#El usuario al seleccionar cualquiera de las opciones, saldra toda la informacion necesaria, la cual se ira acumulando de manera correcta en sus respectivos diccionarios anidados
#Inclusive si la persona desea ingresar 2 o mas equipos de una sola area, el sistema esta en la capacidad de ir contando cuando van en la historia del registro

#%%
while True:
    menu = int(input('''
    1. Ingresar un activo.
    2. Buscar un activo.
    3. Informe de activos.
    4. Salir.
    '''))
    
    if menu == 1:
        print('ok')
    elif menu == 2:
        print('ok')
    elif menu == 3:
        print('ok')
    elif menu == 4:
        break
