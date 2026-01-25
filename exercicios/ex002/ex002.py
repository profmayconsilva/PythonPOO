# Declaração de Classe
class Gafanhoto:
    """
Essa classe cria um Gafanhoto, que é uma pessoa que tem nome e idade.

Para criar uma nova pessoa, use
variavel = Gafanhoto(nome,idade)
    """
    def __init__(self, nome = " ", idade = 0): # Método Construtor
        # Atributos de Instância
        self.nome = nome
        self.idade = idade

    # Métodos de Instância
    def aniversario(self):
        self.idade += 1

    def __str__(self):
        return f"{self.nome} e {self.idade} anos de idade"

    def __getstate__(self):
        return f"Estado: Nome: {self.nome}, Idade: {self.idade}"

# Declaração de Objetos
g1 = Gafanhoto("Gafanho",20)
g2=Gafanhoto("Gafanho")
g3 = Gafanhoto()

g1.aniversario()
print(g1)
print(g1.__doc__) # Dunder attribute
print(g1.__dict__) # Attribute
print(g1.__getstate__()) # Method
print(g1.__class__)
# DUNDER # Double Underline __
# Docstring

