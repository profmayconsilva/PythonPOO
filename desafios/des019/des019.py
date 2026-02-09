from rich import print
from rich.live import Live
from rich.text import Text
import time


class Livro:
    def __init__(self, titulo, paginas):
        self.titulo = titulo
        self.paginas = paginas
        self.pag_atual = 1

    def avancar_paginas(self, quant_pag, delay=0.8):
        print(
            f':book: [blue]Você acabou de abrir o livro [red]"{self.titulo}"[/] '
            f'que tem [green]{self.paginas} páginas[/] no total.\n'
            f'Agora você está na [yellow]página {self.pag_atual}[/]\n'
        )

        texto = Text()

        with Live(texto, refresh_per_second=10) as live:
            for _ in range(quant_pag):
                time.sleep(delay)

                if self.pag_atual < self.paginas:
                    self.pag_atual += 1
                    texto.append(" > ", style="dim")
                    texto.append(f"pág {self.pag_atual}", style="bold yellow")
                    live.update(texto)
                else:
                    texto.append("\nVocê chegou ao final do livro", style="bold red")
                    live.update(texto)
                    break


livro1 = Livro(titulo='Reis 1', paginas=20)
livro2 = Livro(titulo='Reis 2', paginas=30)

livro1.avancar_paginas(quant_pag=21)
livro2.avancar_paginas(quant_pag=20)
