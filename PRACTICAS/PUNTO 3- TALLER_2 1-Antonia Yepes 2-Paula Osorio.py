#%%TALLER ENTREGABLE #2
#Punto numero 3:
    #se presentan dos opciones a la respuesta del problema:
        #Primera opcion:
import random as rdm

caballo_1 = 0
caballo_2 = 0
while True:
    x = rdm.randint(0,1)
    if caballo_1 == 10:
        break
    if caballo_2 == 10:
        break
    if x == 0:
        caballo_1 = caballo_1 + 1
    else:
        caballo_2 = caballo_2 + 1
    continue

print("caballo_1: ", caballo_1,"\ncaballo_2: ", caballo_2)

#%%
#Segunda opcion:
    
import random
recorrido_caballo_1 = 0
recorrido_caballo_2 = 0
while True:
   recorrido_caballo_1 = recorrido_caballo_1 + random.randint(1,3)
   recorrido_caballo_2 = recorrido_caballo_2 + random.randint(1,3)
   caballo_1= ''
   caballo_2= ''
   for i in range(recorrido_caballo_1):
       caballo_1 += '-------C#1-------|RACE'
   for i in range(recorrido_caballo_2):
       caballo_2 += '-------C#2-------|RACE'
   print('caballo 1: ' , caballo_1)
   print('caballo 2: ' , caballo_2)
   if (recorrido_caballo_1 != recorrido_caballo_2):
       if recorrido_caballo_1 >= 1 and recorrido_caballo_1 > recorrido_caballo_2:
           print('GANA EL CABALLO #1')
           break
       if recorrido_caballo_1 >= 1 and recorrido_caballo_2 > recorrido_caballo_1:
           print('GANA EL CABALLO #2')
           break
   elif (recorrido_caballo_1 == recorrido_caballo_2) and (recorrido_caballo_2 >= 1):
       print('Empate !')
       break



    
  