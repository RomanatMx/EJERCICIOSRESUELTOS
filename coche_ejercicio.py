class Coche:
    marca = ""
    modelo = ""
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


MiCoche = Coche()
print(MiCoche.repostar(60))
print(MiCoche.avanzar(400))

