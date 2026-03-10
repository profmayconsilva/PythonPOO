from rich import print
from rich.panel import Panel
from rich.traceback import install
install()

class PRODUTO:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def etiqueta(self):
        conteudo = f'{self.nome.center(30, " ")}'
        conteudo += f"{'-' * 30}"
        precof = f'R${self.preco:,.2f}'
        conteudo += f'{precof.center(30, ".")}'
        etiqueta = Panel(title="Produto", renderable=conteudo, width=34)
        print(etiqueta)

p1 = PRODUTO("Iphone 17 Pro Max", 5_500)
p1.etiqueta()
p2 = PRODUTO("Computador Xeon X99", 2_500)
p2.etiqueta()
