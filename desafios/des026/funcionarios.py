from abc import ABC, abstractmethod
from rich import print
from rich.panel import Panel

class Funcionaria(ABC):

  def __init__(self, nome: str, sal_bruto: float):
    self.nome = nome
    self.sal_bruto = sal_bruto
    self.sal_min = 1621.0  # Valor atual do salário mínimo
    self.inss = 7.5

  @abstractmethod
  def calc_salario(self):
    pass

  def analisar_sal(self):
    salario_liquido = self.calc_salario()
    # Correção: divisão para achar a quantidade de salários mínimos
    qtd_minimos = salario_liquido / self.sal_min
    # Correção: type(self).__name__ pega 'Horista' ou 'Mensalista'
    nome_classe = type(self).__name__

    print(Panel(
        f'O salário de [cyan]{self.nome}[/cyan] ([red]{nome_classe}[/red]) é de R$'
        f' {salario_liquido:.2f} e corresponde a {qtd_minimos:.2f} salário(s)'
        ' mínimo(s).'
    ))


class Horista(Funcionaria):

  def __init__(self, nome: str, valor_hora: float, horas_trab: int):
    # Correção: passando sal_bruto=0.0 para satisfazer o __init__ de Funcionaria
    super().__init__(nome, 0.0)
    self.valor_hora = valor_hora
    self.horas_trab = horas_trab

  def calc_salario(self):
    salario = self.valor_hora * self.horas_trab
    return salario


class Mensalista(Funcionaria):

  def __init__(self, nome: str, sal_bruto: float):
    super().__init__(nome, sal_bruto)

  def calc_salario(self):
    # Correção: inss / 100 para aplicar os 7.5%
    salario = self.sal_bruto - (self.sal_bruto * (self.inss / 100))
    return salario


# --- Testando o código ---
f1 = Horista('Maria', valor_hora=50.0, horas_trab=160)
f2 = Mensalista('Ana', sal_bruto=3500.0)

f1.analisar_sal()
f2.analisar_sal()