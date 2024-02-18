import json

dane = [123, 'dada', True]

file = open("moje_dane.json", "wt")

json.dump(dane, file)

file = open("moje_dane.json", "rt")

dane = json.load(file)

print(dane)

file.close