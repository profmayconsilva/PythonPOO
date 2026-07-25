from abc import ABC, abstractmethod
from math import pi
from rich import print


class Poligono(ABC):
    def __init__(self, qtd_lados: int):
        self.qtd_lados: int = qtd_lados

    @abstractmethod
    def perimetro(self):
        pass

    @abstractmethod
    def area(self):
        pass


class Quadrado(Poligono):
    def __init__(self, lado: float):
        super().__init__(4)
        self.lado = lado

    def area(self):
        print(
            f'O [bold cyan]quadrado[/] possui lado medindo [yellow]{self.lado}[/], portanto, possui uma área de [bold green on black] {self.lado ** 2:.2f} [/].')

    def perimetro(self):
        print(
            f'O [bold cyan]quadrado[/] possui lado medindo [yellow]{self.lado}[/], portanto, possui um perímetro de [bold green on black] {self.lado * self.qtd_lados:.2f} [/].')


class Circulo(Poligono):
    def perimetro(self):
        print(
            f'O [bold magenta]círculo[/] possui o raio de [yellow]{self.radius}[/], portanto, possui um perímetro aproximado de [bold green on black] {2 * pi * self.radius:.2f} [/].')

    def area(self):
        print(
            f'O [bold magenta]círculo[/] possui o raio de [yellow]{self.radius}[/], portanto, possui uma área aproximada de [bold green on black] {pi * self.radius ** 2:.2f} [/].')

    def __init__(self, radius: float):
        super().__init__(0)
        self.radius = radius
