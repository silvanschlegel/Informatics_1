from abc import ABC, abstractmethod

class Actor(ABC):
    def __init__(self, name):
        self.__name = name
    @abstractmethod
    def get_monthly_salary(self):
        pass
    @abstractmethod
    def __str__(self):
        pass

    def get_name(self):
        return self.__name

class Lead(Actor):
    id = 0
    def __init__(self, name, wage):
        super().__init__(name)
        self.__id = Lead.id
        Lead.id += 1
        self.__salary = wage/12

    def get_monthly_salary(self):
        return self.__salary

    def __str__(self):
        return f'Salary: {self.get_monthly_salary()} ({self.__id})'

    def get_id(self):
        return self.__id




class Extra(Actor):
    def __init__(self, name, hourly_wage, hours):
        super().__init__(name)
        if hourly_wage < 9.4:
            raise ValueError
        self.__hourly_wage = hourly_wage
        self.__hours = hours
        self.__salary = self.__hours*self.__hourly_wage

    def get_monthly_salary(self):
        return self.__salary

    def __str__(self):
        return f'Salary: {self.get_monthly_salary()} (temp)'

class Studio:
    def __init__(self, name):
        self.name = name
        self.__actors = []

    def add_actor(self, actor):
        if actor in self.__actors:
            raise ValueError
        self.__actors.append(actor)

    def get_monthly_staff_cost(self):
        total_cost = 0
        for i in self.__actors:
            total_cost += i.get_monthly_salary()
        return total_cost




# DO NOT SUBMIT THE LINES BELOW!
e = Studio("Warmer Sisters")
i1 = Lead("Bob", 60000) # yearly salary
i2 = Lead("Alice", 75000) # yearly salary
i3 = Extra("Taylor", 21.50, 15) # hourly salary, hours per month
assert i1.get_name() == "Bob"
assert i3.get_name() == "Taylor"
assert i1.get_id() == 0
assert i2.get_id() == 1
assert i1.get_monthly_salary() > 4000
assert i3.get_monthly_salary() == 322.50
e.add_actor(i1)
e.add_actor(i2)
e.add_actor(i3)
assert e.get_monthly_staff_cost() > 9000
print(bool("False"))