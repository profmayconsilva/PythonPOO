from fretes import *

def main():
    dist:float = 20
    entrega = Moto(dist)
    print(f"Frete de {type(entrega).__name__} em {dist:.2f} km")
    entrega.calcular_frete()

    entrega = Caminhao(dist)
    print(f"Frete de {type(entrega).__name__} em {dist:.2f} km")
    entrega.calcular_frete()

    entrega = Drone(dist)
    print(f"Frete de {type(entrega).__name__} em {dist:.2f} km")
    entrega.calcular_frete()

if __name__ == '__main__':
    main()