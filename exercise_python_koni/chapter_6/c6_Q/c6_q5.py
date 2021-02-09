class Element:
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number


dic = {"name": "Hydrogen", "symbol": "H", "number": 1}

classobj = Element(**dic)

print(classobj.name)
print(classobj.symbol)
print(classobj.number)




