#%%TALLER ENTREGABLE #2
#Punto # 4:
'''
Ejercicio 4
Realice una función que genere las primeras n filas del triángulo de pascal.
El usuario debe tener la opción de ingresar el número de filas deseadas.

 '''
def validar_numero():  
        while True:
            try:
                x = int(input('Ingrese el numero: '))
                break
            except:
                print('Ingreso un dato no valido')
                continue
        return x
#Se crea una función para validar los números en caso de que se ingrese un 
#valor incorrecto 
def triangulo_de_pascal (rows):
            row = [1]
            zero = [0]
            for i in range (rows):
                print(row)
                row = [i + n for i, n in zip(row + zero, zero + row)]
#Función 'ara generar las n filas del triángulo de pascal, el ellase encuentra 
#un bucle for que recorre el valor ingresado por el usuario utulizando la función
#zip para poder usar las variables row y zero retornando un nuevo iterable que
#contine la información almacenada en las variables.

while True:    
    menu = int(input('''
    1.Ingrese numero
    2.Desea ingresar otro numero.
    3.Salir
    '''))
    
    if menu == 1 and 2:
        r = int(input('Ingrese el número de filas:'))
        triangulo_de_pascal(r)
    elif menu == 3:
        print('Fin del programa')
        break
    else:
        validar_numero()
   

#Por último, se crea un ciclo while con el cual, el usuario puede acceder
#al menu en donde  se ejecutarán las funciones validar_numero y 
#triangulo_de_pascal de acuerdo a la opción que elija el usuario


