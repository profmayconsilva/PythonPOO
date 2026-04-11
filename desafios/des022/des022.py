from rich import print
from rich.panel import Panel


class ControleRemoto:
    canal_min: int = 1
    canal_max: int = 5
    volume_min: int = 1
    volume_max: int = 5

    def __init__(self, canal=1, volume=2):
        self.canal_atual: int = self._validar(canal, self.canal_min, self.canal_max)
        self.volume_atual: int = self._validar(volume, self.volume_min, self.volume_max)
        self.ligado: bool = False

    def _validar(self, valor, minimo, maximo):
        return max(minimo, min(valor, maximo))

    def ligar_desliga(self):
        self.ligado = not self.ligado

    def _circular(self, valor, minimo, maximo, passo):
        if valor == maximo and passo > 0:
            return minimo
        if valor == minimo and passo < 0:
            return maximo
        return valor + passo

    def canal_mais(self):
        if self.ligado:
            self.canal_atual = self._circular(
                self.canal_atual, self.canal_min, self.canal_max, 1
            )

    def canal_menos(self):
        if self.ligado:
            self.canal_atual = self._circular(
                self.canal_atual, self.canal_min, self.canal_max, -1
            )

    def volume_mais(self):
        if self.ligado:
            self.volume_atual = self._circular(
                self.volume_atual, self.volume_min, self.volume_max, 1
            )

    def volume_menos(self):
        if self.ligado:
            self.volume_atual = self._circular(
                self.volume_atual, self.volume_min, self.volume_max, -1
            )

    def mostrar_tv(self):
        if not self.ligado:
            conteudo = ":prohibited: [red]A TV está desligada[/red]"
        else:
            canais = " ".join(
                f"[black on yellow] {c} [/black on yellow]" if c == self.canal_atual else f" {c} "
                for c in range(self.canal_min, self.canal_max + 1)
            )

            volume = "".join(
                "[black on cyan] [/black on cyan]" if v <= self.volume_atual else "[black on white] [/black on white]"
                for v in range(self.volume_min, self.volume_max + 1)
            )

            conteudo = f"CANAL = {canais}\nVOLUME = {volume}"

        tv = Panel(conteudo, title="[ TV ]", width=40)
        print(tv)


c = ControleRemoto()

while True:
    c.mostrar_tv()
    comando = str(input(f" < CH >  - VOL +  "))
    match comando:
        case '0':
            break
        case '@':
            c.ligar_desliga()
        case '<':
            c.canal_menos()
        case '>':
            c.canal_mais()
        case '-':
            c.volume_menos()
        case '+':
            c.volume_mais()
    print("\n" * 10)