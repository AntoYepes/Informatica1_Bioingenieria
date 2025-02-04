#%%PARCIAL 1
#Banco de sangre

sangre = []
plasma = []
plaquetas = []

# 1er input
while True:
    # Inicialización de la variable registro
    registro = []
    total = 0

    componente = input('''
    Ingrese una opcion:
    1.Sangre total o globulos rojos
    2.Plasma fresco o congelado
    3.Plaquetas
    4.Salir.
    ''')

    # Input - COMPONENTE
    if componente == '1' or componente == '2' or componente == '3':
        fecha_registro = input('Ingrese la fecha del registro aaaa-mm-dd: ')
        registro.append(fecha_registro)

        # Input - RH
        for rh in ['a+:', 'a-:', 'b+:', 'b-:', 'o+:', 'o-:', 'ab+:', 'ab-:']:
            rh = int(input(f'Ingrese cuantos de rh obtuvo {rh}'))
            registro.append(rh)
            total = total + rh
        # Inclusión del total al final del registro
        registro.append(total)

        # Guardado del registro en el componente especificado
        if componente == '1':
            sangre.append(registro)
            # Condicional de la meta para SANGRE
            if total <= 30:
                print('ALERTA!!! No se cumplió la meta de sangre')
        elif componente == '2':
            plasma.append(registro)
            # Condicional de la meta para PLASMA
            if total <= 40:
                print('ALERTA!!! No se cumplió la meta de plasma')
        elif componente == '3':
            plaquetas.append(registro)
            # Condicional de la meta para PLAQUETAS
            if total < 10 or total >15:
                print('ALERTA!!! No se cumplió la meta de plaquetas')
    elif componente == '4':
        break
    else:
        print('ALERTA!!! la opcion que ingreso es incorrecta, favor intentelo de nuevo')

# Impresión de las salidas
# SANGRE
for i in range(len(sangre)):
    print(f'Registro {i+1} de sangre: ', sangre[i])
# PLASMA
for i in range(len(plasma)):
    print(f'Registro {i+1} de plasma: ', plasma[i])
# PLAQUETAS
for i in range(len(plaquetas)):
    print(f'Registro {i+1} de plaquetas: ', plaquetas[i])

#%%
