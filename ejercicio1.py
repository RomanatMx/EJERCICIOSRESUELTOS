'''
Creación de un módulo para validación de nombres de usuarios
'''

import os

def validar_alfanumerico(usuario):
    if usuario.isalnum() == True:
        print('Nombre de usuario válido')
        ingres_contraseña()
    else:
        print('El nombre de usuario puede contener solo letras y números') 

def ingres_contraseña():
    print('                                 VALIDACIÓN DE CONTRASEÑA')
    contr = input('Escribe tu contraseña: ')
    if len(contr) > 8:
        if contr.islower() == True:
            print('La contraseña debe contener minúsculas y mayúsculas')
        elif contr.isupper() == True:
            print('La contraseña debe contener minúsculas y mayúsculas')
        else:
            if contr.isalnum() == True: 
                print('La contraseña debe de contener al menos un carácter no alfanumérico') 
            else:    
                for letra in contr:
                    if letra == ' ':
                        print('La contraseña no puede tener espacios')
                        break      
                else:
                    print('La contraseña es válida')
                      
    else:
        print('La contraseña debe contener igual o más de 8 caráteres')  

def main():
    os.system('cls')
    print('                                    VALIDACIÓN DE NOMBRE DE USUARIO')
    nombre = input('Introduce tu nombre de usuario: ')
    continuar = True
    os.system('cls')
    while continuar == True:
        if len(nombre) < 6:
            print('El nombre del usuario debe contener al menos 6 caracteres')
            continuar = False
        elif len(nombre) > 12:
            print('El nombre de usuario no debe contener más de 12 caracteres')
            continuar = False     
        else:
            validar_alfanumerico(nombre)
            continuar = False
    input('Presiona enter para continuar')
    
        
if __name__ == '__main__':
    main()

   
    




