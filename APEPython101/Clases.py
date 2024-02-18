class Samochod:
    def __init__ (self, marka, kolor):
        self.marka = marka
        self.kolor = kolor
        self.przebieg = 0

    def przejedz_trase(self, odleglosc):
        self.przebieg =+ odleglosc

    def __str__(self):
        return f'To jest samochod'
    
class SamochodElektryczny(Samochod):
    def __init__(self, marka, kolor):
        super().__init__(marka, kolor)
        self.pojemnosc_baterii = 10000


moj_samochod = Samochod('Fiat', 'Czerwony')
samochod_sluzbowy = SamochodElektryczny('Tesla', 'Biały')

print(moj_samochod)
moj_samochod.przejedz_trase(100)
print(moj_samochod.przebieg)

print(samochod_sluzbowy.pojemnosc_baterii)