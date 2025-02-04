#%% Punto 1 - numeros enteros de 3 digitos
#Se debe ingresar un numero de tres digitos, invetir valores, suma,multiplicacion,resta

#Entradas del proceso
f = int(input('Ingrese el primer numero entero de 3 digitos:'))
g = int(input('Ingrese el segundo numero entero de 3 digitos:')) 

if isinstance(f, int) and len(str(f)) == 3:
    print('verdadero')
else:
    print('Falso, ingreso un numero fuera de rango')
    
if isinstance(g, int) and len(str(g)) == 3:
    print('verdadero')
else:
    print('falso, ingreso un numero fuera de rango')
    
#Proceso
#Invertir el numero g
invertir = int(str(g)[::-1])

#intercambiar 1 y 2 de f
last = str(f)[-1::]
exchange = str(f)[:-1]
re_exchange = str(exchange)[::-1]
together = re_exchange + last

#operacion suma y multiplicacion
suma = f + g
multiplicacion = f * g

#Salidas
print(f'El numero g invertido es: {invertir}')
print(f'El numero f invertercambiando el digito 1 y 2 es: {together}')
print(f'La suma de f y g es: {suma}')
print(f'la multiplicacion de f con g es: {multiplicacion}')

#operacion de resta y divison con la condicion dada
if f > g:
    resta_1 = f - g
    division_1 = f / g
    print(f'f es mayor que g: \nResta = {resta_1} \nDivision = {division_1}')
else:
    resta_2 = g - f
    division_2 = g / f
    print(f'g no es mayor que f: \nResta = {resta_2} \nDivision = {division_2}')


#%%Punto 2
#Convertir un numero binario de 8bits a numero decimal

#Entradas
valid = 0
while valid != 8:
    x = str(input('Digite el numero binario de 8bits:'))
    valid = 0
    for i in x:
        if int(i) == 0 and int(i) == 1:
            valid = valid +1

#Proceso
decimal = int(str(x), 2)
Hexadecimal = hex(decimal)
Octal = oct(decimal)

#Salidas
print(f'La conversiones a decimal, hexadecimal y octal respectivamente son: {decimal} , {Hexadecimal}, {Octal}') 

#%%Punto 3

#Entradas
x = int(input('Ingrese el valor de la temperatura de la encubadora:'))
y = int(input('Ingrese el valor de la humedad de la encubaora:'))
z = int(input('Ingrese el valor del ruido de la encubadora:'))

#validacion numero
lista = [x, y, z]
for i in lista:
    if i != 1 and i != 0:
        print('ERROR')
    else:
        print('ok')
        
#Proceso
if y or z == 1:
    print('¡ALARMA! la encubadora se encuentra encendida')
else:
    print('Lo sentimos la encubadora se encuentra apagada')

    



    
    
    
   



        
        