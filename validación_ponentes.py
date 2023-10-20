"""
Este código permite introducir el nombre de 5 persona y reconocer si alguno de ellos es ponente y su orden en la lista...

declarar lista de nombres de ponentes ['']
contador = 0
Para contador < rango máximo de ponentes en la lista:
    solicitar nombre del ponente
    guardar nombre del ponente en la lista de nombres de ponentes
    contador + 1
solicitar nombre de ponente
Para contador < rango máximo de ponentes en la lista:
    buscar el nombre de ponente ingresado en la lista si coincide: 
        imprime el nombre ingresado es un ponente y el orden de participación
    contador + 1
"""
def validarPonentes():
    nombres_ponentes = [''] * 5
    contador = 0
    for contador in range(len(nombres_ponentes)):
        nombre_ponente = input('Ingresa el nombre: ')
        nombres_ponentes[contador] = nombre_ponente 
        contador += 1
    print(nombres_ponentes)
    busqueda = input('Ingresa el nombre del ponente: ')
    contador2 = 0
    for contador2 in range(len(nombres_ponentes)):
        if busqueda == nombres_ponentes[contador2]:
            print(f'{busqueda} es un ponente, y su participación es la número {contador2+1} ')
        contador2 += 1
    

validarPonentes()


