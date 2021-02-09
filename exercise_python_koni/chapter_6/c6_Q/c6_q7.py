class Element:
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number
    def __str__(self):
        return("name=%s, symbol=%s, number=%s" %
              (self.name, self.symbol, self.number))

dic = {"name": "Hydrogen", "symbol": "H", "number": 1}

Hydrogen = Element(**dic)

print(Hydrogen)