from ex008 import *

def main():
    c1 = ContaBancaria("111", "Maria", 5_000)
    c1.depositar(1000)
    c1.titular = "Pedro"
    print(c1)

if __name__ == '__main__':
    main()