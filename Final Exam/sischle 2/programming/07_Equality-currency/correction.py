class Currency:
    def __init__(self, name, amount, rate):
        self.__name = name
        self.__amount = amount
        self.__rate = rate

    def __eq__(self, other):
        if not isinstance(other,Currency):
            return NotImplemented
        if self.__amount*self.__rate == other.__amount*other.__rate:
            return True
        return False
