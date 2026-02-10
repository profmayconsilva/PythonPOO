from rich  import print

class FUNCIONARIO:
    empresa = 'Curso em Vídeo'
    def __init__(self, nome, setor, cargo):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo

    def apresentar(self):
        print(f':folded_hands: [blue]Salve Maria[/blue]! Olá irmãos e irmães, eu me chamo [bold] {self.nome}[/bold], sou do(a) {self.setor} e trabalho como {self.cargo} da empresa {__class__.empresa}!')

c1 = FUNCIONARIO('Maria', setor='Sara', cargo="Coordenadora")
c1.apresentar()
c2 = FUNCIONARIO('Matheus', 'Administação', cargo="Auxiliar Administrativo")
c2.apresentar()