# Stworz klase czworokat,posiadajaca cztery boki (lista) i metodę obwod
class Czworokat:
    def __init__(self, boki):
        self.boki = boki
    def obwod(self):
        return sum(self.boki)
    
czworokat = Czworokat([1, 2, 3, 4])
print(f'Boki czworokata to {czworokat.boki}')
print(f'Obwod czworokata to {czworokat.obwod()}')

#Stworz klase prostokat, posiadajaca metode pole

class Prostokat(Czworokat):
    def __init__(self, a, b):
        super().__init__([a, a, b, b])
        self.a = a
        self.b = b
    def pole(self):
        return self.a*self.b

prostokat = Prostokat(3, 5)
print(f'Pole prostokata to {prostokat.pole()}')
print(f'Obwod prostokata to {prostokat.obwod()}')

#Stworz klase kwadrat

class Kwadrat(Prostokat):
    def __init__(self, a):
        super().__init__(a, a)
        self.a = a

kwadrat = Kwadrat(10)
print(f'Pole kwadratu to {kwadrat.pole()}')
print(f'Obwod kwadratu to {kwadrat.obwod()}')
print(f'{kwadrat.boki}')
