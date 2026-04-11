from exercicios.ex005.pessoa import Pessoa


class Aluno(Pessoa):
    def __init__(self, nome, idade, curso, turma):
        super().__init__(nome, idade)
        self.curso = curso
        self.turma = turma

    def fazer_matricula(self):
        print(f"{self.nome} acabou de se matricular no curso {self.curso}, entrando na turma {self.turma}.")