from rich import inspect
from aluno import Aluno
from professor import Professor
from funcionario import Funcionario


a1 = Aluno(nome="Fernando", idade=20, curso="Curso de Python", turma="Curso de Python")
inspect(a1, methods=True)

p1 = Professor(nome="Aparecido", idade=50, nivel="Médio", especialidade="Python")
inspect(p1, methods=True)

f1 = Funcionario(nome="Francisco", idade=25, cargo="Assistente Administrativo", setor="Administrativo")
inspect(f1, methods=True)

a1.fazer_aniversario()
f1.fazer_aniversario()