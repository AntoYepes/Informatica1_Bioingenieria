#%%#%% Dados tres numeros decida cual esta en medio
#Analisis del problema

#Entradas
a = int(input('Ingrese el primer numero:'))  
b = int(input('Ingrese el segundo numero:'))
c = int(input('Ingrese el tercer numero:'))

#Proceso
if a<b and b<c:
    print('El numero que esta en medio es: {b}')
if c<b and b<a:
    print('El numero que esta en medio es: {b}')
if b<a and a<c:
    print('El numero que esta en medio es: {a}')
if c<a and a<b:
    print('El numero que esta en medio es: {a}')
if a<c and c<b:
    print('El numero que esta en medio es: {c}')
if b<c and c<a:
    print('El numero que esta en medio es: {c}')
else:
    print('ingreso numeros iguales')
    
#%%CICLOS
while True:
    print('Este programa le calculara la nota final de una materia')
    print('Recuerde que las notas deben estar entre 0 y 5. Si se equivoca debe intentar de nuevo')

    n1 = float(input('Ingrese la nota 1 (30%): '))
    n2 = float(input('Ingrese la nota 2 (15%): '))
    n3 = float(input('Ingrese la nota 3 (15%): '))
    n4 = float(input('Ingrese la nota 4 (20%): '))
    n5 = float(input('Ingrese la nota 5 (20%): '))
   
    if n1<0 or n1>5:
        n1 = float(input('Ingrese la nota 1 (30%): '))
    if n2<0 or n2>5:
        n2 = float(input('Ingrese la nota 2 (15%): '))
    if n3<0 or  n3>5:
        n3 = float(input('Ingrese la nota 3 (15%):'))
    if n4<0 or n4>5:
        n4 = float(input('Ingrese la nota 4 (20%): '))
    if n5<0 or n5>5:
        n5 = float(input('Ingrese la nota 5 (20%): '))
    
    promedio = n1*0.3 + n2*0.15 + n3*0.15 + n4*0.2 + n5 *0.2
    print(promedio)
        
    op = int(input('Desea ingresar otro estudiante 1-Si o 2-No: '))
    if op == 1:
        continue
    else:
        break
    
    
#%%EJERCICIO CON FOR
hce  = [] #Requerimiento 4
paciente = [] #Requerimiento 4

for j in range(1000):
    nombre = input('Ingrese el nombre del paciente:')
    cc = int(input('Ingrese el documento de identidad:'))
    edad = int(input('Ingrese la edad del paciente:'))
    eps = input('Ingrese la EPS:')
    
    #Requerimiento 3
    paciente = [nombre, cc, edad, eps]
    hce.append(paciente)
    
    #Requerimiento 5
    op = int(input('desea ingresar mas pacientes 1-Si o 2-No:'))
    if op == 1:
        continue
    else:
        break
print(hce)

for p in hce:
    print('nombre:', p[0])
    print('cc:', p[1])
    print('edad:', p[2])
    print('eps:', p[3])
    
#%%Algoritmo que pida dos numeros enteros y que calcule su division
dividendo = int(input('Ingrese el numero: '))
divisor = int(input('Ingrese el otro numero: '))

if dividendo % divisor == 0 :
    division = dividendo/divisor
    print(f'La division es exacta y su cociente es: {division}')
else:
    division = dividendo/divisor
    print(f'La division no es exacta y el cociente es: {division}')
#%%Algoritmo que pida dos numeros enteros y escriba si el mayor es multiplo del menor
num_1 = int(input('Ingrese el primer numero entero: '))    
num_2 = int(input('Ingrese el segundo numero entero: '))

if num_1 >= num_2 and num_1 % num_2 != 0:
    print(str(num_1) + 'no es multiplo de' + str(num_2))
    
elif num_1 >= num_2 and num_1 % num_2 == 0:
    print(str(num_1) + '\nes multiplo de\n' + str(num_2))
    
else:
    print(str(num_2) + '\nes multiplo de\n' + str(num_1))

#%%Algoritmo que pida dos numeros enteros y escriba que numeros son pares y cuales impares desde el primero hasta el segundo.
x = int(input('Ingrese un numero entero: '))
y = int(input(f'Ingrese otro numero entero que sea mayor que {x}: '))
i = 0

if y < x:
    print('El valor ingresado no es correcto')
    
else:
    for i in range(x, y+1):
        if i % 2 == 0:
            print(f'El numero {i} es par')
        else:
            print(f'El numero {i} es impar')
            
#%%Algoritmo que pida un numero entero mayor que cero y que escriba sus divisores.
numero_1 = int(input('Ingrese un numero entero mayor que cero: '))

if numero_1 <= 0:
    print('Recuerde que el numero debe ser mayor que cero: ')
else:
    print(f'los divisores de {numero_1} son:')
    for i in range (1, numero_1 + 1) :
        if numero_1 % i == 0:
            print(i, end='')

#%%
for i in range(1, 5): # con range el numero 5 no se incluye por eso en el ejercicio anterior le sumaron 1
    print(i)

#%% Ejercicio propuesto en clase
# contador
i = 1
t = 0

#Requerimiento #1
x = int(input('Favor digite cuantas mediciones va a ingresar: '))

#Requerimiento #2
while (i < x):
    temp = float(input('Ingrese la temperatura del equipo '))
    i = i + 1 #contador
    t = t + temp #Acumulador
    
    #Requerimiento #3
    if(temp < 15):
        print('ALERTA!!! Temperatura menor a 15°C ')
    if(temp > 30):
        print('ALERTA!!! Temperatura mayor a 30°C')

print('La temperatura promedio es: {0}.format (t/x)')
#%%TALLER TIPO PARCIAL
#Clinica veterinaria
#Listas vacias
historia_clinica = []
mascota = []

#contadores
cat = 0 #cat = cat + 1
dog = 0 #dog = dog + 1
grave = 0
critico = 0

while True:
    record = input('''
    1. Ingresar paciente.
    2. Mostrar cantidades de pacientes.
    3. Buscar paciente.
    4. Salir.
    ''')
    if record == '1':
        nombre = input('Ingrese el nombre de la mascota: ')
        id_mascota = int(input('Ingrese el numero de identificacion de la mascota:'))
        tipo_de_mascota = input('Ingrese 1. si es perro o 2. si es gato: ')
        if tipo_de_mascota == '1':
            tipo = 'perro'
        else:
            tipo = 'gato'
        edad = int(input('Ingrese la edad de la mascota: '))
        estado= input('Ingrese el estado de la mascota 1-grave o 2-critico: ')
        if estado == '1':
            est = 'grave'
        else:
            est = 'critico'
                  
        #almacenar informacion de listas individuales
        mascota = [nombre, id_mascota, tipo_de_mascota, edad, estado]
        #almacenar la informacion en el historial
        historia_clinica.append(mascota)
              
        #contar cuantos son perros y cuantos gatos
        if tipo == '1':
            dog = dog + 1
        else:
            cat = cat + 1
        
        #contar cuantos son graves y cuantos son criticos
        if estado == '1':
            grave = grave + 1
        else:
            critico = critico + 1
            
        #mostrar los contadores de gatos y perros    
    elif record == '2':
        print('Gatos: ', cat)
        print('Perros: ', dog)
        print('Mascotas graves: ', grave)
        print('Mascotas criticas: ', critico)
        
        #buscar la mascota usando el numero de identificacion
    elif record == '3':
        buscar_id = input('Ingrese el ID a buscar:')
        for i in historia_clinica:
            print('Nombre: ', i[0])
            print('Id_mascota: ', i[1])
            print('Tipo:', i[2])
            print('Edad:', i[3])
            print('Estado: ', i[4])
            
    elif record == '4':
        break
    else:
        print('ALERTA!!! Ingreso una opcion no valida. \nIntente de nuevo.')
        
print('Fin del programa')
#%%
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
               