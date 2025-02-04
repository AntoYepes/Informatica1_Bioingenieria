#%% Librerias
import os
import numpy as np

#%% Funion que lee los inputs
def inputs(ruta):
    info_paciente = []
    campos = ['Doc identidad','Nombre','Apellido','Edad','Genero',
              'A1b','Fetal', 'A1c', 'P3','A0', 'S-Window']
    tipos = [int, str, str, int, str, float, float, float, float, float, float]
    for i, val in enumerate(campos):
        while True:
            a = input(f'Ingrese la informacion de {val}: ')
            info_paciente.append(a)
            try:
                if(tipos[i] == int):
                    a = int(a)
                elif(tipos[i]==float):
                    a = float(a)
                break
            except:
                print('ERROR')
      
    info = float(info_paciente[7])
    
    if info <= 5.6:
        info_paciente.append('No Diabetico')
    elif info >= 5.7  and info  <= 6.5:
        info_paciente.append('Controlado')
    elif info >= 6.6:
        info_paciente.append('No Controlado')  
    item = '|'.join(info_paciente)
    
    with open(ruta + '/database/lis.txt', 'a') as lis:
          in_info = str(item)
          lis.write(in_info + '\n' )
            
#inputs()    
#%% Funcion que guarda la informacion en lis.txt  
def save_lis(ingreso, ruta):
    texto = '|'.join(ingreso) 
    with open(ruta + '/database/lis.txt', 'a') as lis:
        lis.write(texto + '\n')

#save_lis(ingreso)  
#%% Funcion que guarda la informacion de los 3txt de la carpeta laboratory en lis.txt
def add_info_lis(ruta):  

    files = os.listdir(ruta + 'laboratory')
    files.sort()
    
    datos = []
    for j in files:
        with open(ruta + 'laboratory/' + j) as f:
            cont = f.readlines()
            for i in cont:
                if i.startswith('3O'):
                    a = i.split('|')
                    doc_id = a[2]
                    datos.append(doc_id)
                    print('Identificacion: ', doc_id)
                    edad = a[4].split('^')[3]
                    datos.append(edad)
                    print('Edad: ', edad)
                    nom = a[12]
                    datos.append(nom)
                    print('Nombre: ',nom)
                    ape = a[13]
                    datos.append(ape)
                    print('Apellido: ', ape)
                    gen = a[27]
                    datos.append(gen)
                    print('Genero: ', gen)
                if i.startswith('4R|1|'):
                    a1b = i.split('|')[3]
                    datos.append(a1b)
                    print('A1b: ', a1b)
                if i.startswith('6R|3|'):
                    f = i.split('|')[3]
                    datos.append(f)
                    print('F: ', f)
                if i.startswith('0R|5|'):
                    a1c = i.split('|')[3]
                    datos.append(a1c)
                    print('A1c: ', a1c)
                if i.startswith('2R|7|'):
                    p3 = i.split('|')[3]
                    datos.append(p3)
                    print('P3: ', p3)
                if i.startswith('4R|9|'):
                    a0 = i.split('|')[3]
                    datos.append(a0)
                    print('A0: ', a0)
                if i.startswith('6R|11|'):
                    s_wind = i.split('|')[3]
                    datos.append(s_wind)
                    print('S-Window: ', s_wind)
                    print('\n')
        x = float(a1c)        
        if x <= 5.6:
            datos.append('No Diabetico')
        elif x >= 5.7  and x  <= 6.5:
            datos.append('Controlado')
        elif x >= 6.6:
            datos.append('No Controlado')  
        
    step = len(datos)/11
    items = np.array_split(datos,step)
    #print(items)
    for i in items:
        save_lis(i, ruta)
    
    #add_info_lis()    
#add_info_lis()        
#%%Funcion que lee el lis.txt
def read_listxt(ruta):
    with open(ruta + 'database/lis.txt', 'r+') as f:
        cont = f.readlines()
        for i in cont:
            x = i.split('|')
            print('ID: ', x[0] )
            print('Age: ', x[1])
            print('Name: ', x[2])
            print('Lastname: ', x[3])
            print('Gender: ', x[4])
            print('A1b: ', x[5])
            print('Fetal: ', x[6])
            print('A1c: ', x[7])
            print('P3:', x[8])
            print('A0: ', x[9])
            print('S_Window: ', x[10])
            print('Estado: ', x[11])
         
#read_listxt()
#%%Funcion que busca al paciente con el ID
def buscar_pac(ruta):  
    num_id = str(input('Ingrese el numero del ID: '))
    with open('C:/Users/Antonia/Downloads/PARCIAL 3/database/lis.txt', 'r') as f:
        linea = f.readlines()
        content = [x.strip() for x in linea]
        if num_id not in content:
            print('El paciente no existe en la base de datos')
        for i in content:
            hemog = []
            if i.startswith(num_id):
                idd = i.split('|')[0]
                print('Identidad:', idd)
                nom = i.split('|')[2]
                print('Nombre:', nom)
                ape = i.split('|')[3]
                print('Apellido: ', ape)
                edad = i.split('|')[1]
                print('Edad: ', edad)
                sex = i.split('|')[4]
                print('Sexo: ', sex)
                a1b = i.split('|')[5]
                hemog.append(a1b)
                f = i.split('|')[6]
                hemog.append(f)
                a1c = i.split('|')[7]
                hemog.append(a1c)
                p3 = i.split('|')[8]
                hemog.append(p3)
                a0 = i.split('|')[9]
                hemog.append(a0)
                s_wind = i.split('|')[10]
                hemog.append(s_wind)
                print('A1b:', hemog[0],'- Fetal: ', hemog[1], '- A1c: ', hemog[2], '- P3: ', hemog[3], '- A0:', hemog[4], '- S-Window: ', hemog[5])

#buscar_pac()
