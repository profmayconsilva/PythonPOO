import random
from abc import ABC, abstractmethod
from rich import print

class Personagem (ABC):
    def __init__(self, nome: str, vida:float):
        self.nome = nome
        self.vida = vida
        self.golpes = ['Soco', 'Pulo Giratório', 'Chute', 'Pontapé', 'Magia']

    def atacar(self, alvo, forca):
        cal_dano = random.uniform(0.6, 1.2)
        forca_final = forca * cal_dano

        print(
            f'[green]{self.nome}[/green] atacou [red]{alvo.nome}[/red] com um'
            f' [blue]{random.choice(self.golpes)}[/blue] de força'
            f' [cyan]{forca}[/cyan] e recebeu [red] {forca_final:.2f} de dano [/red].'
        )

        alvo.receber_dano(forca_final)
    def receber_dano(self, d_ano):
        self.vida -= d_ano
        if self.vida < 0:
            self.vida = 0  # Evita vida negativa

    @abstractmethod
    def curar(self):
        pass

class Guerreiro(Personagem):
    def curar(self):
        cura = random.uniform(0, 15)
        self.vida += cura
        print(
            f'[green]{self.nome}[/green] usou poção e recuperou'
            f' [cyan]{cura:.2f}[/cyan] de vida! Vida atual: [green]{self.vida:.1f}[/green]'
        )


class Mago(Personagem):
    def curar(self):
        cura = random.uniform(0, 30)  
        self.vida += cura
        print(
            f'[green]{self.nome}[/green] usou magia de cura e recuperou'
            f' [cyan]{cura:.2f}[/cyan] de vida! Vida atual: [green]{self.vida:.1f}[/green]'
        )

