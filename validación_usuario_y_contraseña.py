'''
Ejercicio 1:
Crear un módulo para validación de nombres de usuarios. Dicho módulo, deberá
cumplir con los siguientes criterios de aceptación:
• El nombre de usuario debe contener un mínimo de 6 caracteres y un máximo de 12
• El nombre de usuario debe ser alfanumérico
• Nombre de usuario con menos de 6 caracteres, retorna el mensaje “El nombre de
usuario debe contener al menos 6 caracteres”
• Nombre de usuario con más de 12 caracteres, retorna el mensaje “El nombre de
usuario no puede contener más de 12 caracteres”
• Nombre de usuario con caracteres distintos a los alfanuméricos, retorna el mensaje
“El nombre de usuario puede contener solo letras y números”
• Nombre de usuario válido, retorna True

Ejercicio 2: 
Crear un módulo para validación de contraseñas. Dicho módulo, deberá cumplir con
los siguientes criterios de aceptación:
• La contraseña debe contener un mínimo de 8 caracteres
• Una contraseña debe contener letras minúsculas, mayúsculas, números y al menos
1 carácter no alfanumérico
• La contraseña no puede contener espacios en blanco
• Contraseña válida, retorna True
• Contraseña no válida, retorna el mensaje “La contraseña elegida no es segura”

Ejercicio3:
Crear un módulo que solicite al usuario el ingreso de un nombre de usuario y contraseña y
que los valide utilizando los módulos generados en los dos ejercicios anteriores.

'''

import os

def validar_alfanumerico(usuario):
    if usuario.isalnum() == True:
        print('Nombre de usuario válido')
        ingresar_contraseña()
    else:
        print('El nombre de usuario puede contener solo letras y números') 

def ingresar_contraseña():
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

   
    




