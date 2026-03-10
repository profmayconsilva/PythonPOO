from rich import print
import time

class Livro:
    def __init__(self, titulo, paginas):
        self.titulo = titulo
        self.total_paginas = paginas
        self.pagina_atual = 1

        print(f":open_book: [blue]Você acabou de abrir o livro [red] {self.titulo} [/] que tem {self.total_paginas} paginas no total. Você agora está na página {self.pagina_atual}. [/]")

    def avancar_paginas(self, qtd = 1):
        cont = 0
        for pg in range(0, qtd, 1):
            if not self.fim_do_livro():
                self.pagina_atual +=1
                print(f"Pág {self.pagina_atual} :arrow_forward: ", end='')
                time.sleep(0.5)
                cont += 1
        print(f"[blue]Você agora está na página [yellow]{self.pagina_atual}[/][/]")
        if self.fim_do_livro():
            print(f":closed_book: Você chegou ao final do livro {self.titulo} ")

    def fim_do_livro(self) -> bool:
       return True if self.pagina_atual == self.total_paginas else False

l1 = Livro("10 coisas que eu aprendi", 20)
l1.avancar_paginas(20)