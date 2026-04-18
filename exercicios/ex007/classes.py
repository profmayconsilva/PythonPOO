from abc import ABC, abstractmethod

class Pessoa(ABC):
    def __init__(self, nome = "", idade = 0):
        self.nome = nome
        self.idade = idade

    def fazer_aniversario(self):
        self.idade += 1

    @abstractmethod
    def estudar(self):
        pass

class Aluno(Pessoa):
    def estudar(self):
        print(f'{self.nome} está estudando {self.curso} na turma {self.turma}')

    def __init__(self, nome, idade, curso, turma):
        super().__init__(nome, idade)
        self.curso = curso
        self.turma = turma

    def fazer_matricula(self):
        print(f"{self.nome} acabou de se matricular no curso {self.curso}, entrando na turma {self.turma}.")

class Professor(Pessoa):
    def estudar(self):
        print(f'Profº {self.nome} é especialista em {self.especialidade}')

    def __init__(self, nome, idade, especialidade, nivel):
        super().__init__(nome, idade)
        self.especialidade = especialidade
        self.nivel = nivel

    def dar_aula(self):
        print(f'Professor(a) {self.nome} está iniciando sua aula')
class Funcionario(Pessoa):
    def estudar(self):
        pass

    def __init__(self, nome, idade, cargo, setor):
        super().__init__(nome, idade)
        self.cargo = cargo
        self.setor = setor

    def bater_ponto(self):
        print(f'{self.nome} bateu ponto')