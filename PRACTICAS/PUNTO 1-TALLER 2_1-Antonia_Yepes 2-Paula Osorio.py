#%%TALLER ENTREGABLE #2
#Punto numero_1:
    #numeral a
L = [9,8,-9,-6,-8,7,0,3,-8]

def filtrar(lista, P=[]):
    for i in lista:
        if (i>0):
            P+=[i]
    return (P)

L = [9,8,-9,-6,-8,7,0,3,-8,1,-2,6,-7,0,3,10]
filtrar(L)
#EXPLICACION PASO A PASO
#Paso 1:
    #Se crea la funcion llamada filtrar que tiene como argumentos una lista 
    #que sera dada por el usuario y otra lista vacia (explicada en el paso 4)
#Paso 2:
    #se usa el ciclo FOR para que dentro de la lista que el usuario ingrese
    # el i vaya corriendo uno por uno los items de la lista y asi pueda hacer
    #el filtro deseado y explicado a continuacion
#Paso 3:
    #Dentro del for se usa un condicional IF el cual restringe y solo
    #selecciona los numeros que sean positivos, los numeros que no cumplan
    #dicha condicion, no seran tomados en cuenta
#Paso 4:
    #Se usa una lista vacia como argumento, justamente para que dentro del if
    #se inicie desde cero con la lista dada y se le añada otra vez la misma.
#Paso 5:
    #Se imprime utilizando el siguiente codigo ***filtrar(L)***
    
    
#%%
#Punto numero 1:
    #numeral b:
def validar_numero():
        while True:
            try:
                x = int(input('Ingrese el numero: '))
                break
            except:
                print('Ingreso un dato no valido')
                continue
        return x
    
def ingrese_lista():    
    numberList = []
    n = int(input("Enter the list size : "))
    print("\n")
    for i in range(0, n):
        print("Enter number at location", i, ":")
        item = int(input())
        numberList.append(item)
       
    print("User List is ", numberList)
    return numberList
    
#ingrese_lista()

while True:
    menu = int(input('''
    1. Ingrese la lista que quiere duplicar.
    2. Salir
    '''))
    if menu == 1:
        numberList = ingrese_lista()
        P = [x for x in numberList if x > 0 ] 
        print(P + P)  
    elif menu == 2:
        print('Fin del programa')
        break


      


