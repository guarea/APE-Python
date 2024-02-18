#This is Json files in python exercise

import json

class Bank:
    def __init__(self, filename):
        self.filename = filename
        try:
            with open(filename, "rt") as file:
                self.konta = json.load(file)
                print(self.konta)
        except FileNotFoundError:
            print("Otwieramy bank")
            self.konta = {}

    def add_user(self, nazwa):
        self.konta[nazwa] = 0

    def add_money(self, nazwa, wartosc):
       self.konta[nazwa] += wartosc
        
    def print_balance(self, nazwa):
        balance = self.konta[nazwa]
        print(f'The balance is: {balance} PLN')

    def write_file(self):
        with open(self.filename, "wt") as file:
            json.dump(self.konta, self.file)

bank = Bank('Bank.json')

while(True):
    answer = input("Co chcesz zrobić? Stan konta/Wplac pieniadze/Nowy uzytkownik/Zamknij program")
    if answer == "S":
        bank.print_balance()
    elif answer == "W":
        bank.add_money()
    elif answer == "N":
        bank.add_user()
    elif answer == "Z":
        bank.write_file()
        break