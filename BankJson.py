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

    def add_user(self, nazwa)

    def add_money(self, new_amount):
        file = open(self.filename, "rt")
        balance = int(file.read())
        file.close()
        file = open(self.filename, "wt")
        file.write(str(balance + new_amount))
        file.close()

    def print_balance(self):
        file = open(self.filename, "rt")
        balance = file.read()
        print(f'The balance is: {balance} PLN')
        file.close()

bank = Bank('Bank.json')

while(True):
    answer = input("Co chcesz zrobić? Wyświetl/Dodaj/Zamknij")
    if answer == "W":
        bank.print_balance()
    elif answer == "Z":
        break