import random
import time
print('Este es un juego, dónde tratarás de adivinar el número aleatorio entre 1 y 10')
input('Da click para generar un número aleatrio... ')
time.sleep(.35)
print('Listo!!, ahora adivina el número aleatorio...')
numero_aleatorio = random.randint(1,10)
def adivinar_numero():
    continuar = 0
    while continuar < 3:
        numero_adivinado = int(input('Ingrese el número que pensó'))
        if numero_adivinado == numero_aleatorio:
            print('Felicidades Ganaste')
            break
        else:
            if numero_adivinado < numero_aleatorio:
                print('El número ingresado es menor')
                print('Inténtalo de nuevo!...')
                continuar += 1
                print(f'Te quedan {3-continuar} turnos') 
            elif numero_adivinado > numero_aleatorio:
                print('El número ingresado es mayor')
                print('Inténtalo de nuevo!...')
                continuar += 1
                print(f'Te quedan {3-continuar} turnos')
    else:
        print(f'Te gané, el número correcto era el {numero_aleatorio}, sigue participando')
        print('Hasta luego!')
adivinar_numero()



