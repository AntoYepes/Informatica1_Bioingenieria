#%%
def seleccion_area(): 
    while True:
        menu_2 = input('''
        1. Biomedica.
        2. Sistemas.
        3. Infraestructura.
        ''')
        if menu_2 == '1':
            break
        elif menu_2 == '2':
            
            break
        elif menu_2 == '3':
            
            break
        
def ingresar_equipo():
    equipo = []
    for i in ['nombre', 'marca', 'serial', 'frecuencia de mantenimiento','frecuencia de calibracion','numero de archivo']:
        a = input(f'Ingrese {i} para el inventario correspondiente: ')
        equipo.append(a)
    print(equipo)

#ingresar_equipo()

#seleccion_area()   
def validar_serial():
        while True:
            try:
                serial = int(input('Ingrese el numero de serial: '))
                break
            except ValueError:
                print('Ingreso un dato no valido')
        return serial

#%%DICCIONARIO BUSQUEDA

def busqueda_dict(diccionario):
    key_list = list(diccionario.keys())
    x = int(input('Ingrese el index de la busqueda:'))
    key = key_list[x - 1]
    value = diccionario.get(key)
    print(value)
    print('1er equipo:', value[0])
    print('2nd caracter:', value[1])

diccionario = {'B-2020-1':['tv','cama','silla'],
               'S-2020-1':['ventilador','mueble','mesa'],
               'I-2020-1': ['Ventana','puerta','cuaderno']} 

busqueda_dict(diccionario)
#%%ERROR FUNCION DICCIONARIO
dicts = {}
def dicts(equipo):
    dicts[len] = equipo
    print(dicts)

equipo =['x','y','z'] 
dicts(equipo)

#%%INTENTO MIL FUNCION DICCIONARIO
diccionario = {'1' : ['a','b','c'],
               '2' : ['d','e','f'],
               '3' : ['g','h','i']}
x = int(input('''
1. bio
2. sist
3. info
'''))
if x == 1:
    activo = 'B-2020-' + str(len(diccionario) + 1)
    print(activo)
elif x == 2:
    activo = 'S-2020-' + str(len(diccionario) + 1 )
elif x == 3:
    activo = 'I-2020-' + str(len(diccionario) + 1 )
    
    
#%%
d = { 'A' : [1, 2, 3, 4, 5, 6, 7, 8, 9], 
     'B' : 34, 
     'C' : 12, 
     'D' : [7, 8, 9, 6, 4] } 
  
# using dict.items() 
count = 0
for key, value in d.items(): 
    if isinstance(value, list): 
        count += len(value) 
print(count)
