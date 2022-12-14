class BankAccount():
    def __init__(self, limit):
        if limit < 0:
            raise AssertionError
        self.__limit = limit
        self.__balance = 0

    def deposit(self,amount):
        self.__balance+= amount
        self.__limit += amount
    def withdraw(self,amount):
        if amount > self.__limit:
            raise AssertionError
        self.__balance -= amount
        self.__limit -= amount
    def balance(self):
        return self.__balance
    def available(self):
        return self.__limit

from unittest import TestCase
class Test_Bank(TestCase):
    def test_constructor(self):
        self.assertRaises(AssertionError,BankAccount, -10)

    def test_withdraw(self):
        self.assertRaises(AssertionError,BankAccount(100).withdraw,110)

    def test_withdraw_1(self):
        a = BankAccount(100)
        a.withdraw(20)
        self.assertEqual(80, a.available())

    def test_deposit(self):
        a = BankAccount(100)
        a.deposit(10)
        self.assertEqual(110, a.available())

    def test_balance(self):
        a = BankAccount(100)
        a.deposit(10)
        self.assertEqual(10,a.balance())

    def test_available(self):
        a = BankAccount(100)
        a.deposit(10)
        self.assertEqual(110, a.available())

# example usage
acc = BankAccount(100)
print(acc.balance()) # prints ’0’
print(acc.available()) # prints ’100’
acc.deposit(30) # balance: 30, available: 130 (illustration, no "print")
print(acc.balance()) # prints ’0’
print(acc.available()) # prints ’100’
acc.withdraw(40) # balance: -10, available: 90 (illustration, no "print")
print(acc.balance()) # prints ’0’
print(acc.available()) # prints ’100’
#acc.withdraw(91) # AssertionError