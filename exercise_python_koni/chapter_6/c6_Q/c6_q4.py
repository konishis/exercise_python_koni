class Element:
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number

classobj = Element("Hydrogen", "H", 1)

print(classobj.name)
print(classobj.symbol)
print(classobj.number)

