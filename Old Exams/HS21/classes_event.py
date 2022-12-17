class Event:
    def __init__(self, seats,):
        self.__seats = ["" for i in range(seats)]
        self.__name = ""

    def enter(self, seat_number , person):
        if seat_number < 1 or seat_number > len(self.__seats):
            raise IndexError
        if self.__seats[seat_number-1] != "":
            raise NameError
        self.__seats[seat_number-1] = person
    def get(self, seat_number):
        if seat_number < 1 or seat_number > len(self.__seats):
            raise IndexError
        if self.__seats[seat_number-1] == "":
            return None
        return self.__seats[seat_number-1]
    def occupied(self):
        occ = 0
        for i in self.__seats:
            if i != "":
                occ += 1
        return occ

    def empty(self):
        empty = 0
        for i in self.__seats:
            if i == "":
                empty+= 1
        return empty
    def __lt(self, other):
        return self.occupied() < other.occupied()
    def __gt__(self, other):
        return self.occupied()>other.occupied()
    def __eq__(self, other):
        return self.occupied()==other.occupied()
    def get_name(self):
        return self.__name
    def set_name(self,name):
        self.__name = name






# DO NOT SUBMIT THE LINES BELOW!
e1 = Event(150)
e1.enter(45, "Alice")
assert e1.get(45) == "Alice"
e1.enter(42, "Bob")
assert e1.occupied() == 2
assert e1.empty() == 148
e2 = Event(40)
assert e2.get(40) == None
e2.enter(1, "Andrea")
#
e2.enter(2, "Beatrice")
assert e2 == e1
e2.enter(20, "Charly")
assert e2 > e1
