class Brewery:
    def __init__(self, name):
        self.__name = name
        self.__items = {}
    @staticmethod
    def to_gram(quantity, einheit):
        if einheit == "t":
            return quantity*1000000
        if einheit == "kg":
            return quantity*1000
        return quantity

    def add_stock(self,item, quantity, einheit):
        if item in self.__items.keys():
            self.__items[item] += Brewery.to_gram(quantity, einheit)
        else:
            self.__items[item] = Brewery.to_gram(quantity,einheit)

    def show_stock(self, item):
        if item not in self.__items.keys():
            return 0
        else:
            return self.__items[item]

    def brew(self, recipe):
        for i,j in recipe.items():
            if i not in self.__items or j > self.__items[i]:
                raise LookupError
        for i, j in recipe.items():
            self.__items[i] -= j




# DO NOT SUBMIT THE LINES BELOW!
assert Brewery.to_gram(1, "t") == 1000000
assert Brewery.to_gram(1, "kg") == 1000
assert Brewery.to_gram(1, "g") == 1
b = Brewery("KegOverflow")
assert b.show_stock("Syrup") == 0
b.add_stock("Malt", 5, "kg")
b.add_stock("Malt", 5, "kg")
b.add_stock("Water", 50, "kg")
b.add_stock("Hops", 30, "g")
assert b.show_stock("Malt") == 10000
b.brew({"Malt": 8000, "Water": 40000, "Hops": 20})
assert b.show_stock("Malt") == 2000
b.brew({"Water": 10000})
assert b.show_stock("Water") == 0
