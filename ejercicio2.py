# MÓDULO DE VALIDACIÓN DE CONTRASEÑAS #
import os 

def ingresar_contraseña():
    print('                                 VALIDACIÓN DE CONTRASEÑA')
    contr = input('Escribe tu contraseña: ')
    if len(contr) > 8:
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
    input('Presiona enter para coninuar')       
    

def ingres_contraseña():
    print('                                 VALIDACIÓN DE CONTRASEÑA')
    contr = input('Escribe tu contraseña: ')
    if len(contr) > 8:
        if contr.islower() == True:
            print('La contraseña dedebe contener minúsculas y mayúsculas')
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
    input('Presiona enter para coninuar')       
    

ingres_contraseña()
