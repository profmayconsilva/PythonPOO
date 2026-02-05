from rich import print
from rich.panel import Panel
from rich.traceback import install
install()

class PRODUTO:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def etiqueta(self):
        etiqueta = Panel.fit(title="Produto", renderable=f"{self.nome:^40}\n" + f'{".":.^40}\n' +f"{f'R${self.preco:.2f}':.^40}")
        print(etiqueta)

p1 = PRODUTO("Iphone 17 Pro Max", 5_500.00)
p1.etiqueta()
p2 = PRODUTO("Computador Xeon X99", 2_500.00)
p2.etiqueta()
