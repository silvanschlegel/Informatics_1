from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def hunger(self):
        pass

class Dog(Animal,ABC):
    def hunger(self):
        pass
    @abstractmethod
    def bark(self):
        print("woof")

class Golden(Dog):

    def hunger(self):
        return 1

print(Golden.hunger(1))

