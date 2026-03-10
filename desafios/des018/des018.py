# Considere:
# Consumo padrão: 400g por pessoa
# Preço: R$82,40/kg

from rich import print
from rich.panel import Panel

class Churrasco:
    consumo_por_pessoa = 0.400  # kg
    preco_por_kg = 82.40
    def __init__(self, title, quantidade):
        self.title = title
        self.participantes = quantidade

    def __str__(self):
        return f"Esse é o {self.title} com {self.participantes} participantes"
    def analisar(self):


        peso_total = self.participantes * Churrasco.consumo_por_pessoa
        valor_gasto = peso_total * Churrasco.preco_por_kg
        valor_por_pessoa = valor_gasto / self.participantes

        panel = Panel(title=f'{self.title}', renderable=(f'Analisando o [green bold]{self.title}[/] com [blue bold]{self.participantes} de convidados[/].\n'
                                                         f'Cada participante comerar 0.4 kg e cada kg custará R$82,40\n'
                                                         f'Recomendo [blue]comprar {peso_total:.2f}kg [/] de carne.\n'
                                                         f'O churras custará [green]R${valor_gasto:.2f}[/]\n'
                                                         f'e ficará [yellow]R${valor_por_pessoa:.2f}[/] por pessoa '))
        print(panel)


c1 = Churrasco("Churrasco", 400)
c1.analisar()
c2 = Churrasco("Churrasco", 3)
c2.analisar()
c3 = Churrasco("Churrasco", 15)
c3.analisar()