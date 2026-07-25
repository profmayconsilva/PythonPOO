from classes import Quadrado, Circulo

def main():
    a = Quadrado(4)
    b = Quadrado(5)
    c = Circulo(3)
    d = Circulo(4)

    a.area()
    a.perimetro()

    b.area()
    b.perimetro()

    c.area()
    c.perimetro()

    d.area()
    d.perimetro()


if __name__ == '__main__':
    main()