from rpg import *

def main():
    guerreiro = Guerreiro('Thorin', 10000.0)
    mago = Mago('Gandalf', 6000.0)

    guerreiro.atacar(mago, 2000.0)
    mago.curar()
    mago.atacar(guerreiro, 2500.0)
if __name__ == '__main__':
    main()