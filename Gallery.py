# Niech wypisz 

class Galeria:
    def __init__(self, dziela:dict):
        self.dziela = dziela
        self.uzytkownicy = []

    def wypiszUzytkownikow(self):
        print(self.uzytkownicy)

    def wypiszDziela(self):
        print(self.dziela)

class Uzytkownik:
    def __init__(self, nick, przynaleznosc):
        self.nick = nick
        self.przynaleznosc = przynaleznosc
        self.typKonta = 'Uzytkownik'
        self.przynaleznosc.uzytkownicy.append(nick)
    def wyswietlDziela(self, nazwaDziela):
        print(self.przynaleznosc.dziela[nazwaDziela])

class Artysta(Uzytkownik):
    def __init__(self, nick, przynaleznosc):
        super().__init__(nick, przynaleznosc)
        self.typKonta = 'Artysta'
    def dodajDzielo(self, nazwaDziela, dzielo):
        self.przynaleznosc.dziela[nazwaDziela]=dzielo

class Kurator(Uzytkownik):
    def __init__(self, nick, przynaleznosc):
        super().__init__(nick, przynaleznosc)
        self.typKonta = 'Kurator'
        self.wystawa = {}
    def utworzWystawe(self, nazwyDziel:list):
        for x in nazwyDziel:
            self.wystawa.update({x: self.przynaleznosc.dziela[x]})
    

galeria = Galeria(
    {'usmiech':'😀',
     'serce':'❤',
     'ser':'🧀'})

uzytkownikAsia = Uzytkownik('Asia', galeria)
uzytkownikKasia = Artysta('Kasia', galeria)
uzytkownikBasia = Kurator('Basia', galeria)

galeria.wypiszUzytkownikow()
#print(galeria.dziela)
#galeria.wypiszDziela()
uzytkownikAsia.wyswietlDziela('ser')
uzytkownikKasia.dodajDzielo('oko', '👁')
uzytkownikKasia.wyswietlDziela('oko')
uzytkownikBasia.utworzWystawe(['serce', 'oko'])
uzytkownikBasia.utworzWystawe(['ser', 'oko'])
print(uzytkownikBasia.wystawa)
print(uzytkownikKasia.typKonta)