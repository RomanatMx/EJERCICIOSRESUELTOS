"""
Este código válida que una persona cuente con la edad mínima y países de origen determinados
para poder entrar al ejército, si la edad de la persona es mayor o igual a 18 años y su país de origen es 
España puede entrar al ejército o también si la edad de la persona es mayor o igual a 20 y su país de origen
es Colombia también puede entrar al ejército de lo contrario esta persona no sería apta para entrar al ejército.
"""
"""
solicitar datos:
1) edad_persona
2) país_origen
validar datos:
si edad_persona es mayor o igual a 18 y su pais_origen es España o si edad_persona es mayor o igual a 20 y su país_origen es Colombia:    
    imprime que esta persona es apta para entrar al ejército.
si no: 
    imprime que esta persona no es apta para entrar al ejército.
"""
def entrarEjercito():
    edad_persona = int(input("Edad: ")) 
    pais_origen = input('País de origen: ').lower
    if edad_persona >= 18 and pais_origen == 'españa' or edad_persona >= 20 and pais_origen == 'colombia': 
        print('Esta persona puede entrar al ejército')
    else:
        print('esta persona no puede entrar al ejército')

entrarEjercito()







