from abc import ABC, abstractmethod
from rich import print


class BebidaQuente(ABC):

    def preparar(self):
        print("Iniciando o preparo...")
        self._separador()

        if self.precisa_ferver():
            self.ferver()

        self.misturar()
        self.servir()

    def ferver(self):
        print("Fervendo água...")
        self._separador()

    def precisa_ferver(self):
        return True

    @abstractmethod
    def misturar(self):
        pass

    @abstractmethod
    def servir(self):
        pass

    def _separador(self):
        print("=-=" * 15)


class Cafe(BebidaQuente):

    def misturar(self):
        print("Adicionando o pó de café na água...")
        self._separador()

    def servir(self):
        print("Servindo o café")
        self._separador()


class Cha(BebidaQuente):

    def misturar(self):
        print("Adicionando o chá na água...")
        self._separador()

    def servir(self):
        print("Servindo o chá")
        self._separador()


class Leite(BebidaQuente):

    def precisa_ferver(self):
        return False  # 🔥 aqui está a correção conceitual

    def misturar(self):
        print("Aquecendo o leite...")
        self._separador()

    def servir(self):
        print("Servindo o leite")
        self._separador()