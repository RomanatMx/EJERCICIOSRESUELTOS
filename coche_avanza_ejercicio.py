""" 
Crea la clase Coche que contenga las siguientes propiedades:
• matrícula (string)
• marca (string)
• kilometros_recorridos (float)
• gasolina (float)
La clase tendrá un método llamado avanzar() que recibirá como argumento el número de kilómetros
a conducir y sumará los kilómetros recorridos al valor de la propiedad kilometros_recorridos. El
método también restará al valor de gasolina el resultado de los kilómetros multiplicado por 0’1.
La clase también contendrá otro método llamado repostar() que recibirá como argumento los litros
introducidos que deberán sumarse a la variable gasolina.
Por último, será necesario controlar que el método avanzar nunca obtendrá un número negativo en
la gasolina. En dicho caso, deberá mostrar el siguiente mensaje: “Es necesario repostar para recorrer
la cantidad indicada de kilómetros”.
Ejemplo:
- repostar(50) # gasolina = 50
- recorrer(100) # kilometros_recorridos = 100, gasolina = 40
- recorrer(40) # kilometros_recorridos = 140, gasolina = 36
- recorrer(180) # kilometros_recorridos = 320, gasolina = 18
"""
class Coche:
    gasolina = 0.0
    kilometros_recorridos = 0.0
    @classmethod
    def avanzar(cls, kilometros_por_avanzar):
        cls.kilometros_recorridos += kilometros_por_avanzar
        cls.gasolina -= (kilometros_por_avanzar * 0.1)
        if cls.gasolina < 0:
            print(f'Para recorrer esos kilometros necesitas recargar {kilometros_por_avanzar*0.1} litros')
        else:
            return 'Kilometros recorridos: '+str(cls.kilometros_recorridos)+' Gasolina: '+str(cls.gasolina)
    @classmethod
    def repostar(cls, gasolina_a_cargar):
        cls.gasolina += gasolina_a_cargar
        return 'Cargaste: '+str(gasolina_a_cargar)+' litros.'
