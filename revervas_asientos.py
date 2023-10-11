'''
Prueba técnica resuelta, consiste en crear un sistema de asientos para un anfiteatro. El teatro cuenta con 10 filas y
10 columnas de asiento, este sistema debe de permitir al cliente poder elegir de entre los asientos libres el que desee 
ocupar y a su vez reservar el asiento. 
'''
import os 

#1er Paso. Creamos la matriz 10*10 la cual representa los asientos en el anfiteatro...
asientos_anfiteatro = [
                        ['L']*10,
                        ['L']*10,
                        ['L']*10,
                        ['L']*10,
                        ['L']*10,
                        ['L']*10,
                        ['L']*10,
                        ['L']*10,
                        ['L']*10,
                        ['L']*10]
#2do Paso. Creamos el menú que nos permitirá mostrar el estado de los asientos, reservar asiento o salir del programa...
RESERVAR = 1
MOSTRAR = 2
SALIR = 3
def mostrar_menú():
    os.system('cls')
    print('                                                 Bienvenido al Anfiteatro')
    print(f'''
        {RESERVAR} Reservar asiento
        {MOSTRAR} Mostrar asientos disponibles
        {SALIR} Salir
    ''')
#3er Paso. Definimos la función para la impresión del estado actual de asientos disponibles
def MostrarAsientosDisponibles():
    print(asientos_anfiteatro)

#4to Paso. Definimos la función para solicitar al cliente el asiento por fila y columna que desea ocupar
#si el asiento se encuentra libre podrá ocuparlo y este se reservará con 'X' como señal de asiento ocupado
#si el asiento se encuentra ocupado, enviará devuelta al cliente a la selección de la fila y columna 
def ReservarAsientos():
    print('                                                             Reserva tu asiento!')
    fila = int(input('Fila, del 0 al 9: '))
    columna = int(input('Columna, del 0 al 9: '))
    if asientos_anfiteatro[fila][columna] == 'L':
        print('El asiento está disponible, disfrute su película')
        asientos_anfiteatro[fila][columna] = 'X'
    elif asientos_anfiteatro[fila][columna] == 'X':
        print('Lo sentimos el asiento está reservado')
        ReservarAsientos()
#5to Paso. Definimos la función main o principal que es la que nos imprimirá el menu y nos permitirá elegir las opciones disponibles
def main():
    continuar = True
    while continuar: 
        os.system('cls')
        mostrar_menú()
        opc = int(input("Elige una opción: "))
        os.system('cls')
        if opc == RESERVAR:
            ReservarAsientos()
        elif opc == MOSTRAR:
            MostrarAsientosDisponibles()
        elif opc == SALIR:
            continuar = False
            print ('Te esperemos pronto!')
        else:
            print('Opción no válida.')
        input('Presiona enter para continuar')

#6to Paso. Llamamos la la funcion main como la principal para la ejecución en la terminal
if __name__ == '__main__':
    main()
        
        
