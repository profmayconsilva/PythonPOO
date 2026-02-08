from rich import print

cores = {
    'azul': 'blue',
    'vermelho': 'red',
    'verde': 'green'
}

class Caneta:
    def __init__(self, cor):
        self.cor = cor
        self.destampado = False

    def destampar(self):
        if not self.destampado:
            self.destampado = True
            print('Caneta destampada')
        else:
            print('Caneta já está destampada')

    def escrever(self, frase):
        if self.cor not in cores:
            print(
                f'Cor inválida!\n'
                f'As cores disponíveis são: {list(cores.keys())}'
            )
            return

        cor_em_ingles = cores[self.cor]

        if not self.destampado:
            print(f'A [{cor_em_ingles}]caneta[/] está tampada')
        else:
            print(f'[{cor_em_ingles}]{frase}[/]')
    def pular_lnha (self, quant):
        n = 1
        for i in range(quant):
            print('\n')


caneta_azul = Caneta('azul')
caneta_vermelho = Caneta('vermelho')
caneta_verde = Caneta('verde')
caneta_amarelo = Caneta('amarelo')

caneta_azul.destampar()
caneta_vermelho.destampar()
caneta_verde.destampar()

caneta_verde.escrever('Essa caneta é verde')
caneta_amarelo.escrever('Essa caneta é amarela')
caneta_amarelo.pular_lnha(quant=3)
caneta_azul.escrever('Essa caneta é azul')
caneta_vermelho.escrever('Essa caneta é vermelha')
