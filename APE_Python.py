przebieg = -100

class Samochod:
    def __init__ (self, marka, kolor):
        self.marka = marka
        self.kolor = kolor
        przebieg = 0

    def przejedz_trase(self, odleglosc):
        przebieg =+ odleglosc

    def __str__(self):
        return f'To jest samochod'
    
samochod = Samochod('Fiat', 'Czerwony')
samochod_sluzbowy = Samochod

print(samochod)
samochod.przejedz_trase(100)
#print(samochod.przebieg)
print(przebieg)