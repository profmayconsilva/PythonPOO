from uuid import main

from rich import print, inspect

class Pessoa:
    def __init__(self, nome = "", idade = 0):
        self.nome = nome
        self.idade = idade

    def fazer_aniversario(self):
        self.idade += 1

class Aluno(Pessoa):
    def __init__(self, nome, idade, curso, turma):
        super().__init__(nome, idade)
        self.curso = curso
        self.turma = turma

    def fazer_matricula(self):
        print(f"{self.nome} acabou de se matricular no curso {self.curso}, entrando na turma {self.turma}.")

class Professor(Pessoa):
    def __init__(self, nome, idade, especialidade, nivel):
        super().__init__(nome, idade)
        self.especialidade = especialidade
        self.nivel = nivel

    def dar_aula(self):
        print(f'Professor(a) {self.nome} está iniciando sua aula')
class Funcionario(Pessoa):
    def __init__(self, nome, idade, cargo, setor):
        super().__init__(nome, idade)
        self.cargo = cargo
        self.setor = setor

    def bater_ponto(self):
        print(f'{self.nome} bateu ponto')

a1 = Aluno(nome="Fernando", idade=20, curso="Curso de Python", turma="Curso de Python")
inspect(a1, methods=True)

p1 = Professor(nome="Aparecido", idade=50, nivel="Médio", especialidade="Python")
inspect(p1, methods=True)

f1 = Funcionario(nome="Francisco", idade=25, cargo="Assistente Administrativo", setor="Administrativo")
inspect(f1, methods=True)

a1.fazer_aniversario()
f1.fazer_aniversario()

if __name__ == "__main__":
    main()