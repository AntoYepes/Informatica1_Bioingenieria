#%%TALLER ENTREGABLE # 2
#Segundo punto:
    #Numeral a y b:
def error():
    print('\nErro-Ingreso un dato no valido.\nFavor intentelo de nuevo.')

while True:
    menu = int(input('''
    1. Replicar ADN.
    2. Transcripcion ADN.
    3. Salir.
    :'''))
    if menu == 1:
        adn = str(input('Ingrese la secuencia de ADN deseada: '))
        print(adn.translate(str.maketrans({'A':'T','T':'A','C':'G','G':'C'})))
    elif menu == 2:
        adn = str(input('Ingrese la secuencia de ADN deseada: '))
        print(adn.translate(str.maketrans({'A':'U','T':'A','C':'G','G':'C'})))
    elif menu == 3:
        print('Fin del programa')
        break
    





    


