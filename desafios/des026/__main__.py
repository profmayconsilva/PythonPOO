from funcionarios import *

def main():
    f1 = Horista("Fernando", 16, 180)
    f1.analisar_sal()

    f2 = Mensalista('Amanda', 3000)
    f2.analisar_sal()

if __name__ == '__main__':
    main()