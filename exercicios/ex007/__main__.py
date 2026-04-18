from rich import inspect
from classes import *

x1 = Aluno(nome="Paulo", idade=20, curso="Curso de Python", turma="Curso de Python")
inspect(x1, methods=True)

y1 = Professor(nome="Francisco", idade=50, nivel="Médio", especialidade="Python")
inspect(y1, methods=True)

z1 = Funcionario(nome="Pedro", idade=25, cargo="Assistente Administrativo", setor="Administrativo")
inspect(z1, methods=True)

x1.fazer_aniversario()
z1.fazer_aniversario()

if __name__ == '__main__':
    main()