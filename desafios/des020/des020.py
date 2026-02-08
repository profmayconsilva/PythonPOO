from rich import print
from rich.panel import Panel

class Gamer:
    def __init__(self, nome, nick):
        self.nome = nome
        self.nick = nick
        self.jogos_favoritos = []

    def add_jogo_favorito(self, jogo):
        if jogo not in self.jogos_favoritos:
            self.jogos_favoritos.append(jogo)
            print(f'O jogo "{jogo}" foi adicionado aos favoritos do jogador {self.nick}')
        else:
            print(f'O jogo "{jogo}" já foi adicionado ao jogador {self.nick}')

    def ficha(self):
        if not self.jogos_favoritos:
            lista_jogos = "Nenhum jogo favorito cadastrado."
        else:
            lista_jogos = ""
            for jogo in self.jogos_favoritos:
                lista_jogos += f"🎮 {jogo}\n"

        ficha_texto = (
            f"[bold]Nome Real:[/bold] [black on blue]{self.nome}[/]\n\n"
            f"[bold]Jogos Favoritos:[/bold]\n[blue bold]{lista_jogos}[/]"
        )

        ficha = Panel.fit(
            ficha_texto,
            title=f"Ficha do Jogador {self.nick}",
            border_style="green"
        )

        print(ficha)


jogador = Gamer(nome='Maycon Antony Silva Dias', nick='latam.202')
jogador.add_jogo_favorito('Mario')
jogador.add_jogo_favorito('Minecraft')
jogador.add_jogo_favorito('Hytale')
jogador.add_jogo_favorito('Hytale')
jogador.ficha()
