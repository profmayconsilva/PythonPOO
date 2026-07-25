from fretes import *
from rich import print
from rich.table import Table

def main():
    dist:float = 10
    viagem = [Moto(dist), Caminhao(dist), Drone(dist)]

    table = Table(title="Tabela de Fretes")
    table.add_column("Distância", justify="center", style="green bold")
    table.add_column("Tipo", justify="center")
    table.add_column("Frete", justify="right", style="cyan")

    for transporte in viagem:
        table.add_row(f'{dist} km', type(transporte).__name__, transporte.calcular_frete())

    print(table)

if __name__ == '__main__':
    main()