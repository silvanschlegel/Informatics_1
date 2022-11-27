#!/usr/bin/env python3

class Fridge:
    def __init__(self):
        self.__items = []
        self.__product_index = -1

    def __iter__(self):
        """Returns an iterator object with a meaningful
        implementation for __next__"""
        return self

    def __next__(self):
        """return next product in the list"""
        self.__product_index += 1
        try: return self.__items[self.__product_index]
        except: raise StopIteration

    def __len__(self):
        """returns how many items are in the fridge"""
        return len(self.__items)

    def store(self, product):
        if isinstance(product, tuple):
            self.__items.append(product)
            self.__items.sort()
        else: raise Warning

    def take(self, product):
        """Takes out items of the fridge. removes
        first found item in the fridge and returns it."""
        try:
            self.__items.remove(product)
            return product

        except: raise Warning("No such item found in the fridge")

    def find(self, name):
        """Takes a name and searches for the item tuple
        with the same name and the earliest eat-by date."""
        try:
            for i in self.__items:
                if i[1] == name:
                    return i
        except: return None


    def take_before(self, date):
        """ dentify and remove all items from the fridge
        for which the eat-by date is before the provided
        date and return them in a list. """
        abgelaufen = []
        for i in self.__items:
            if i[0] < date:
                abgelaufen.append(i)
        for j in self.__items:
            if j[0]< date:
                self.__items.remove(j)
        return abgelaufen




