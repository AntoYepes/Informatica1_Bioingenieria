# Analisi
#El siguiente algoritmo lee los 3 text files en la carpeta laboratory
#dicha informacion se importa en una nueva carpeta llamada database
#en donde se encuentra lis.txt
#el usuario tiene la opcion de leer los 3txt del laboratory
#y además añadir informacion de cada paciente 
#para asi tener la informacion detallada.
#%% Ruta donde esta el archivo
''''*************************Bienvenido*************************
Recuerde ingresar la ruta en el codigo para que corra de manera adecuada'''
ruta = r'C:/Users/Antonia/Downloads/PARCIAL 3/'

#%% Librerias
import os
import numpy as np
 
if __name__ == '__main__':
    import sys
    sys.path.insert(0, ruta)
    
from funciones import inputs, save_lis, add_info_lis, read_listxt, buscar_pac
#%% Codigo
while True:
    menu = int(input('''
    1. Ingresar un paciente manualmente.
    2. Importar información de archivos.
    3. Buscar paciente.
    4. Ver todos los pacientes.
    5. Salir
    :'''))
    if menu == 1:
        inputs(ruta)
    elif menu == 2:
        add_info_lis(ruta)
    elif menu == 3:
        buscar_pac(ruta)
    elif menu == 4:
        read_listxt(ruta)
    elif menu == 5:
        break
    else:
        print('***ERROR***\nIngreso un valor no valido')
        
        