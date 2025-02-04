#%%DIAPOSITIVAS EJERCICIOS
#EJERCICIOS DE ESTRUCTURA SECUENCIAL
#Elabore un algoritmo que lea un numero y obtenga su cuadrado y su cubo
x = int(input('Ingrese un numero entero: '))
cuadrado_x = x**2
cubo_x = x**3
print(cuadrado_x)
print(cubo_x)
#%%Al sueldo de 3 empleados se les aplica un aumento del 10%, 12& y 15%. diseñe un algoritmo que muestre el nuevo salario.
trabajador_1 = int(input('Ingrese el sueldo actual: '))
trabajador_2 = int(input('Ingrese el sueldo actual: '))
trabajador_3 = int(input('Ingrese el sueldo actual: '))

aumento_sueldo1 = trabajador_1 * 0.1
aumento_sueldo2 = trabajador_2 * 0.12
aumento_sueldo3 = trabajador_3 * 0.15

print(aumento_sueldo1)
print(aumento_sueldo2)
print(aumento_sueldo3)
#%%Diseñe algoritmo que promedie las 5 notas de un curso
#nota1: 30 nota2:15 nota3:15, nota4:20 nota5:20
estudiante = input('Ingrese el nombre del estudiante: ')
nota_1 = int(input('Ingrese la primera nota del estudiante: '))
nota_2 = int(input('Ingrese la segunda nota del estudiante: '))
nota_3 = int(input('Ingrese la tercera nota del estudiante: '))
nota_4 = int(input('Ingrese la cuarta nota del estudiante: '))
nota_5 = int(input('Ingrese la quinta nota del estudiante: '))

porcentaje_nota1 = nota_1 * 0.3
porcentaje_nota2 = nota_2 * 0.15
porcentaje_nota3 = nota_3 * 0.15
porcentaje_nota4 = nota_4 * 0.2
porcentaje_nota5 = nota_5 * 0.2

promedio_notas = porcentaje_nota1 + porcentaje_nota2 + porcentaje_nota3 + porcentaje_nota4 + porcentaje_nota5

print(f'La nota promedio de {estudiante} es: {promedio_notas}')
#%%Elabora un algoritmo para calcular el area y perimetro de una circunferencia
radio = int(input('Ingrese el radio de la circunferencia: '))
pi = 3.14

area = pi*(radio**2)
circunferencia = 2*(pi*radio)

print(area)
print(circunferencia)
#%%Una persona promedo avanza 45cm.Dado el numero de pasos, determinar cuantos kilometros, metros y centimetros avanza una persona.
numero_pasos = int(input('Ingrese el numero de pasos dados: '))
avanza = 45 * numero_pasos #cm

kilometros = avanza * (1/100000)
metros = avanza * (1/100)
centimetros = avanza

print(kilometros)
print(metros)
print(centimetros)
#%%Realice un algoritmo que convierta de grados a radianes
grados = int(input('Ingrese el dato del grado que desea convertir: '))
pi = pi

convert = ((grados/180) + pi)

print(convert)
#%%EJERCICIOS DE ESTRUCTURA CONDICIONAL
#Algoritmo que dados dos valores numericos A y B, esciba un msm diciendo si A es mayor, menor o igual a B 
A = int(input('Ingrese el primer numero: '))                       
B = int(input('Ingrese el segundo numero: '))

if A > B:
    print('A es mayor que B')
elif A < B:
    print('A es menor que B')
elif A == B:
    print('A igual a B')
#%%Obtener el promedio de 5 notas, valoradas de 0 a 5 y ponderadas 30,15,15,20,20.
#escriba aprobado si la calificacion es mayor o igual a 3. Independiente de si gano o perdio muestre el promedio.
estudiante = input('Ingrese el nombre del estudiante: ') 
print('\nRecuerde que las notas van en un rango de 0-5') 
nota_1 = float(input(f'Ingrese la nota numero uno de {estudiante}: '))   
nota_2 = float(input(f'Ingrese la nota numero dos de {estudiante}: '))
nota_3 = float(input(f'Ingrese la nota numero tres de {estudiante}: '))
nota_4 = float(input(f'Ingrese la cuarta nota de {estudiante}: '))
nota_5 = float(input(f'Ingrese la quinta nota de {estudiante}: '))

prom_1 = nota_1 * 0.3
prom_2 = nota_2 * 0.15
prom_3 = nota_3 * 0.15
prom_4 = nota_4 * 0.2
prom_5 = nota_5 * 0.2

promedio_total = prom_1 + prom_2 + prom_3 + prom_4 + prom_5

if promedio_total >= 3:
    print(f'{estudiante} aprobo la materia, su promedio es: {promedio_total}')    
else:
    print(f'{estudiante} reprobo la materia, su promdeio es: {promedio_total}')
#%%Algoritmo  que calcule y muestre el valor de x de acuerdo a lo sigte= 
#X = 1 si Y>Z
#X = 2 si Y=Z
#X = 3 si Y<Z
Y = int(input('Ingrese el valor de Y: '))
Z = int(input('Ingrese el valor de Z: '))

if Y > Z:
    print('X es igual a: 1')
elif Y == Z:
    print('X es igual a: 2')
elif Y < Z:
    print('X es igual a: 3')
#%%dados los dato A,B,C num enteros, construir para esscribir estos numeros de manera descendente
A = int(input('Ingrese el primer numero entero: '))
B = int(input('Ingrese el segundo numero entero: '))
C = int(input('Ingrese el tercer numero entero: '))

if A>B>C:
    print(A)
    print(B)
    print(C)
elif A>C>B:
    print(A)
    print(C)
    print(B)
elif B>A>C:
    print(B)
    print(A)
    print(C)
elif B>C>A:
    print(B)
    print(C)
    print(A)
elif C>A>B:
    print(C)
    print(A)
    print(B)
elif C>B>A:
    print(C)
    print(B)
    print(A)
#%%numero de inscripcion, nombre, patrimonio, estrato. cobra cte: 50mil
# patrimonio > 2millones  y estrato > 3 incrementa 3% sobre el patrimonio.
#salidas numero inscripcion, nombres, pago de matricula.    
cobro_u = 50000
numero_inscripcion = int(input('Ingrese el numero de la inscripcion: '))
nombre = input('Ingres su nombre completo con apellidos: ')
patrimonio = int(input('Ingrese el valor total del patrimonio: '))
estrato = int(input('Ingrese el numero de su estrato actual: '))

print(numero_inscripcion)
print(nombre)

if patrimonio > 2000000 and estrato > 3:
    patrimonio_modify = (patrimonio * 0.03) + 50000
    print(patrimonio_modify)
else:
    print(cobro_u)
#%%Algoritmo que dados dos valores A y B, escriba un mensaje diciendo si A es mayor, menor o igual a B.
A = int(input('Ingrese el valor de A: '))
B = int(input('Ingrese el valor de B: '))

if A > B:
    print('A es mayor que B')
elif A == B:
    print('A es igual a B')
else:
    print('A es menor que B')
#%% Segunda opcion punto 1- numeros enteros de 3 digitos
#El numero g
g = int(input('Ingrese el segundo numero entero de 3 digitos:'))
reversed = 0

while(g!=0):
    r = int(g%10)
    reversed = reversed*10 + r
    g = int(g/10)
    
print(reversed)

#El numero f
f = int(input('Ingrese el segundo numero entero de 3 digitos:'))
reversed = 0

while(f!=0):
    r = int(f%10)
    reversed = reversed*10 + r
    f = int(f/10)
    
print(reversed)
#%%Algoritmo que determine la suma del valor menor y mayor en un grupo de 4 datos.
x = int(input('Ingrese el primer valor: '))
y = int(input('Ingrese el segundo valor: '))
z = int(input('Ingrese el tercer valor: '))
w = int(input('Ingrese el cuarto valor: '))

if x>y>z>w or x>z>y>w:
    print(x + w)
elif x>y>w>z or x>w>y>z:
    print(x + z)
elif x>w>z>y or x>z>w>y:
    print(x + y)
elif y>x>z>w or y>z>x>w:
    print(y + w)
elif y>x>w>z or y>w>x>z:
    print(y + z)
elif y>z>w>x or y>w>z>x:
    print(y + x)
elif z>x>y>w or z>y>x>w:
    print(z + w)
elif z>y>w>x or z>w>y>x:
    print(z + x)
elif z>x>w>y or z>w>x>y:
    print(z + y)
elif w>y>z>x or w>z>y>x:
    print(w + x)
elif w>x>z>y or w>z>x>y:
    print(w + y)
elif w>x>y>z or w>y>x>z:
    print(w + z)
#%%Algoritmo que determine la suma del valor menor y mayor en un grupo de 4 datos.

x = int(input('Ingrese el primer valor: '))
y = int(input('Ingrese el segundo valor: '))
z = int(input('Ingrese el tercer valor: '))
w = int(input('Ingrese el cuarto valor: '))

lista = [x, y, z, w]
minimo = min(lista)
maximo = max(lista)
print(minimo + maximo)

#%%Algoritmo que determine la suma del valor menor y mayor en un grupo de 4 datos.

x = int(input('Ingrese el primer valor: '))
y = int(input('Ingrese el segundo valor: '))
z = int(input('Ingrese el tercer valor: '))
w = int(input('Ingrese el cuarto valor: '))

lista = [x, w, y, z]
minimo = lista[0]
maximo = lista[0]

for i in lista:
    if i < minimo:
        minimo = i
    if i > maximo:
        maximo = i
        
print(minimo)
print(maximo)
print(minimo + maximo)

#%%Algoritmo que determine la suma del valor menor y mayor en un grupo de 4 datos.

lista = []
for i in ['x', 'y', 'z', 'w']:
    i = int(input(f'Ingrese el valor {i}:')) 
    lista.append(i)
print(lista)
    
#%%EJEMPLO
#resultado de la prueba Hormona Luteinizante. 
#mujer antes menop de 5 a 25 UI/L. mujer desp 14.2 a 52.3 UI/L
#hombre mayor 18 años prueba ok 1.8 a 8.6 UI/L
lh = float(input('Ingrese el valor de la hormona luteinizante: '))
edad = int(input('Ingrese la edad del paciente: '))
sexo = input('Inrese 1. si es mujer y 2. si es hombre: ')
if sexo == '2':
    if edad > 18:
        if 1.8 < lh < 8.6:
            print('El resultado del paciente es normal')
        else:
            print('Resultado fuera de rango, solicitar examen complementario')
            
else:
    if edad >= 18:
        menopausia = print('Indique 1. menopausica 2.no le ha llegado la menopausia')
        if menopausia == '1':
            if 14.2 < lh < 52.3:
                print('El resultado del paciente es normal')
            else:
                print('Resultado fuera de rango, solicitar examen complementario')
        else:
            if 5 < lh < 25:
                print('El resultado del paciente es normal')
            else:
                print('Resultado fuera de rango, solicitar examen complentario')
    else:
        print('Los valores de lh son normales en la infancia')

#%%Otra opcion punto 2 para convertir binario a decimal
binNum = int(input('Ingrese el numero binario de 8bits:'))
def binToDec(binNum):
    decNum = 0
    power = 0
    while binNum > 0:
        decNum += 2 ** power * (binNum % 10)
        binNum //= 10
        power += 1
    return decNum

print (str(binToDec(binNum)))

#%%Realice un algoritmo que permita calcular la multip de dos numeros enteros solo usando sumas
suma = 0
num_1 = int(input('Ingrese el primer numero entero: '))            
num_2 = int(input('Ingrese el segundo numero entero: '))
multiplicacion = num_1 * num_1

#%%EJERCICIO DE FUNCION
#calculadora, escoger una de las 4 operaciones. 1.suma 2.resta 3.mult 4. division 5.salir
#solo se sale si el usuario ingresa 5

def suma(x, y):
    return x + y
def resta(x, y):
    return x - y
def multiplicacion(x, y):
    return x * y
def division(x,y):
    if y != 0:
        print('ERROR')
    else:
        return x / y
    
while True:
    menu = int(input('''
    1.suma
    2.resta
    3.multiplicacion
    4.division
    5.salir
    '''))
    
    if menu == 1:
        a = int(input('Ingrese un dato:'))
        b = int(input('Ingrese otro dato: '))
        print(suma(a,b))
    elif menu == 2:
        a = int(input('Ingrese un dato:'))
        b = int(input('Ingrese otro dato: '))
        print(resta(a,b))
    elif menu == 3:
        a = int(input('Ingrese un dato:'))
        b = int(input('Ingrese otro dato: '))
        print(multiplicacion(a,b))
    elif menu == 4:
        a = int(input('Ingrese un dato:'))
        b = int(input('Ingrese otro dato: '))
        print(division(a,b))
    elif menu == 5:
        break
    else:
        print('ERROR')
#%%
valid = 0
while valid != 8:
    x = str(input('Digite el numero binario de 8bits:'))
    valid = 0
    for i in x:
        if int(i) == 0 or int(i) == 1:
            valid = valid +1
            
#%%
valid = True
while valid:
    x = str(input('Digite el numero binario de 8bits:'))
    for i in x:
        if int(i) != 0 and int(i) != 1:
            break
        valid=False
        
#%%
x = str(input('Digite el numero binario de 8bits:'))
for i in x:
    if i != 1 or i != 0:
        print('El numero es correcto')
    else:
        print('Error')        

    
#%%Obtener el promedio de 5 notas, valoradas de 0 a 5 y ponderadas 30,15,15,20,20.
#escriba aprobado si la calificacion es mayor o igual a 3. Independiente de si gano o perdio muestre el promedio.
estudiante = input('Ingrese el nombre del estudiante: ') 
nota_total = []
nota_base = 0
for i in ['n1', 'n2', 'n3', 'n4', 'n5']:
    a = int(input(f'Ingrese la nota {i} :'))
    nota_total.append(a)
    nota_base = nota_base + 1
print(nota_total) 
     
p1 = nota_total[0]*0.3
p2 = nota_total[1]*0.15
p3 = nota_total[2]*0.15
p4 = nota_total[3]*0.2
p5 = nota_total[4]*0.2
print(p1,p2,p3,p4,p5)
promedio = [p1 + p2 + p3 + p4 + p5]
print(f'El promedio de {estudiante} es: {promedio}')

#%%HISTORIA CLINICA
#almacenar nombre identi,edad,eps.
#use for. rango 1000. listas anidadas iniciar vcias
#dar opcion de ingresar mas o salir(mostrar datos)
while True:
    datos = []
    carpeta = 0
    menu = (input('''
    1. datos
    2. salir
    '''))
    
    if menu == '1':
        for i in ['nombre', '# de identidad', 'edad', 'eps']:
            a = str(input(f'Ingrese su {i}: '))
            datos.append(a)
            carpeta = carpeta + 1
        print(datos)
    elif menu == '2':
        break
    

  

 






    
    
    
    





