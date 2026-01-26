from rich import print
from rich.table import Table

tabela = Table(title="Tabela de Preços")
tabela.add_column("Nome", justify="center", style="white", no_wrap=True)
tabela.add_column("Preço", justify="center")
tabela.add_row("Lápis", "R$ 1,50")
tabela.add_row("Caneta", "R$ 2,50")
print(tabela)