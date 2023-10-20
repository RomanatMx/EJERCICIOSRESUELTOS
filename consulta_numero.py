"""
Consultar en la base el número solicitado por el usuario.
"""

lista = [6,14,11,3,2,1,15,19]
print('Bienvenido!')
numero = int(input("Ingresa el número a consultar: "))

def validar_numero_en_rango(numero):
    if numero not in range(1,20):
        print('El número ingresado no se encuentra en el rango del 1 al 20..')
        return False
def validar_numero_dentro_de_lista(numero):
    if numero in lista:
        print('Tu número se encuentra registrado en nuestra lista')
    else:
        print('Tu número no se encuentra registrado en la lista')

if validar_numero_en_rango(numero) == True:
    validar_numero_dentro_de_lista(numero)
else: 
    print('Hasta luego')