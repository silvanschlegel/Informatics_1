
class Animal:
    def talk(self):
        return "Moo!"
class Dog(Animal):
    pass
dog = Dog()
print(type(dog.talk()))

a = input()
print(type(a))
print(a)
raise SyntaxError