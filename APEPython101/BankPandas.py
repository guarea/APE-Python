import json
import pandas as pd
with open('stany_kont.json', 'rt') as file:
    konta = json.load(file)

df = pd.json_normalize(konta)
print(df)
df.to_csv('stany_kont.csv')
df = pd.read_csv('stany_kont.csv')
print(df)S
df.info()

class Bank:

    def __init__(self,filename):
        self.filename = filename
        try:
            with open(filename, "rt") as file:  # do sprawdzania jesli plik jest
                try:
                    self.konta = json.load(file)  # załaduj

                except json.JSONDecodeError:
                    print("Otwieramy Bank")
                self.konta = {}

        except FileNotFoundError:
            print("Otwieramy Bank")
            self.konta = {}


    def add_user(self,nazwa):
        self.konta[nazwa] = 0 #dodanie do słownika użytkownika z zerowym stanem konta

    def add_money(self,nazwa,wartosc):
        if nazwa in self.konta:
            self.konta[nazwa] += wartosc
        else:
            raise KeyError("Nie ma takiego użytkownika")

    def print_balance(self,nazwa):
        balance = self.konta[nazwa]
        print(f'The balance is : {balance} PLN')

    def write_file(self):
        with open(self.filename, "wt") as file:
            json.dump(self.konta, file)


BNPParibas = Bank("stany_kont.json")
while(True): #pętla działa na wieczność, nieskończona pętla
    answer = input("Co chcesz zrobić? S - Stan konta, W - wpłać/wypłać pieniądze, D - dodaj uzytkownika, Z - zakończ")
    if answer == "S":
        x = input("Podaj nazwę użytkownika")
        BNPParibas.print_balance(x)
    elif answer == "W":
        x = input("Komu chcesz wpłacić?")
        y = input("Ile chcesz wpłacić/wypłacić?")
        try:
            BNPParibas.add_money(x,int(y))
        except KeyError:
            print("Nie ma takiego użytkownika")

    elif answer == "Z":
        BNPParibas.write_file()
        break

    elif answer == "D":
        x = input("Jakiego użytkownika dodajesz?")
        BNPParibas.add_user(x)