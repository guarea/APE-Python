class Zwierze:
    def __init__(self, kolor, nogi, piora):
        self.kolor = kolor
        self.nogi = nogi
        self.piora = piora
    def info(self):
        czyPiora = '' if self.piora else 'nie '
        print(f'To jest zwierze o kolorze {self.kolor}, {self.nogi} nogach i {czyPiora}posiadajace piora')

zwierze = Zwierze('czerwony', 4, False)
zwierze.info()

class Pies(Zwierze):
    def __init__(self, kolor, jakiOgon):
        super().__init__(kolor, 4, False)
        self.jakiOgon = jakiOgon

    def info(self):
        super().info()
        print(f'Ten pies ma {self.jakiOgon} ogon i robi grrrrr')

pies = Pies('bury', 'krotki')
pies.info()
'''
class Golab(Zwierze):
    def __init__(self, kolor, nogi, piora, jakiePiora):
        super().__init__(kolor, nogi, piora)
        self.jakiePiora = jakiePiora

    def piora(self):
        print(f'Ten golab ma {self.jakiePiora} piora')

golab = Golab('szary', 2, True, 'pierzaste')
golab.info()
print(golab.piora)

'''