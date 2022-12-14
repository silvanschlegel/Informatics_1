class Student:
    def __init__(self, name):
        if not isinstance(name,str):
            raise Warning
        self.__name = name
        self.__year = 1

    def learn(self):
        self.__year += 1

    def get_name(self):
        return self.__name

    def get_year(self):
        return self.__year


class School:
    def __init__(self, name, years__able_to_educate):
        self.__name = name
        self.__years_able_to_educate = years__able_to_educate
        self.__successful_educated = 0

    national_taught = 0

    def educate(self, student):
        from random import choice
        if not isinstance(student, Student):
            raise Warning
        if student.get_year() not in self.__years_able_to_educate:
            raise ValueError
        probability = [True, True, True, True, True, True,True, True, True, False]
        a = choice(probability)
        if a:
            student.learn()
            self.__successful_educated += 1
            School.national_taught += 1

    def get_taught(self):
        return self.__successful_educated




# DO NOT SUBMIT THE LINES BELOW!
a = Student("Ueli")
assert a.get_name() == "Ueli"
assert a.get_year() == 1
s1 = School("Mätteliwise", [1,2,3,4,5,6])
s2 = School("Blüemlihof", [1,2,3,4,5,6])
assert s1.get_taught() == 0
## the following calls have random outcomes
s1.educate(a)
assert a.get_year() in [1, 2]
assert s1.get_taught() in [0, 1]
s2.educate(a)
assert a.get_year() in [1, 2, 3]
assert s2.get_taught() in [0, 1]
assert s2.national_taught in [0, 1, 2]