#%%EJERCICIO HISTORIA CLINICA
#creacion paciente crear tupla
def ingresar_paciente():
    paciente = []
    for i in ['nombre', 'identificacion', 'edad', 'eps']:
        a = input(f'Ingrese {i} del paciente: ')
        paciente.append(a)    
    return tuple(paciente)
   
ingresar_paciente()

#buscar paciente que el output sea la tupla donde esta el paciente        
def busqueda_paciente(base_datos, paciente):    
    for i in base_datos:
        if paciente in i:
            print(i)
        
#datos = [('Lia', '234', '9', 'sura'),
#                 ('Rube', '987', '26', 'sura'),
#                 ('More', '27653', '30', 'sura'),
#                 ('gabriel', '98552', '27', 'sura')]

#busqueda_paciente(datos, 'gab')
    
#meter la tupla del paciente en la lista base de datos
def almacenamiento(base_datos, paciente):
    base_datos.append(paciente)
    return base_datos


#pax = ('Lia', '234', '9', 'sura')
#datos = [('Lia', '234', '9', 'sura'),
#                 ('Rube', '987', '26', 'sura'),
#                 ('More', '27653', '30', 'sura'),
#                 ('gabriel', '98552', '27', 'sura')]
#almacenamiento(datos, pax)

datos = []
while True:
    menu = input('''
    1.Ingresar datos del paciente.
    2.Buscar paciente.
    3.Salir.
    ''')
     
    if menu == '1':
        paciente = ingresar_paciente()
        print(paciente)
        datos = almacenamiento(datos, paciente)
        print(datos) 
    elif menu == '2':
        pax = str(input('Ingrese el paciente de busqueda: '))
        busqueda_paciente(datos, pax)
    
    elif menu == '3':
        print(datos)
        break

    