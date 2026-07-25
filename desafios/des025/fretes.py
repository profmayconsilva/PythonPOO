from abc import ABC, abstractmethod

class Transporte(ABC) :
    def __init__(self, distancia:float):
        self.distancia = distancia

    @abstractmethod
    def calcular_frete(self):
        pass

class Moto(Transporte):
    def __init__(self, distancia: float):
        super().__init__(distancia)
        self.fator = 0.50
    def calcular_frete(self):
        print(f'O valor do frete será de R${self.distancia * self.fator:.2f}')

class Caminhao(Transporte):
    def __init__(self,  distancia: float):
        super().__init__(distancia)
        self.fator = 1.20
    def calcular_frete(self):
        if self.distancia < 50.1:
            print(f'A distância a ser percorrida não atingiu o minimo necessário de 50 km.')
        else:
            print(f'O valor do frete será de R${self.distancia * self.fator:.2f}')

class Drone(Transporte):
    def __init__(self, distancia: float):
        super().__init__(distancia)
        self.fator = 9.50
    def calcular_frete(self):
        if self.distancia > 10.1:
            print(f'A distância máxima a ser percorrida é de 10 km.')
        else:
            print(f'O valor do frete será de R${self.distancia * self.fator:.2f}')