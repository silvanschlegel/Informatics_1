#!/usr/bin/env python3
# add imports, if necessary
from currency_converter import convert
from exchange_rates import EXCHANGE_RATES
class BankAccount:

    def __init__(self, currency="CHF"):
        if not isinstance(currency,str):
            raise Warning("Currency must be String")
        if not currency in EXCHANGE_RATES.keys() or currency == "":
            raise Warning("Invalid Currency")
        self.__currency = currency
        self.__balance = 0

    def get_currency(self):
        return self.__currency

    def get_balance(self):
        return self.__balance
        
    def deposit(self, amount, currency="CHF"):
        if not isinstance(amount, int) and not isinstance(amount, float):
            raise Warning("Amount must be number!")
        if not isinstance(currency,str):
            raise Warning("Currency must be String!")
        if amount<0:
            raise Warning("Amount must be positive!")
        if currency == "" or currency not in EXCHANGE_RATES.keys():
            raise Warning("Currency invalid!")
        if currency == self.__currency:
            self.__balance += amount
        else:
            self.__balance += convert(amount, currency, self.__currency)
    
    def withdraw(self, amount, currency="CHF"):
        if not isinstance(amount, int) and not isinstance(amount, float):
            raise Warning("Amount must be number!")
        if not isinstance(currency,str):
            raise Warning("Currency must be String!")
        if amount<0:
            raise Warning("Amount must be positive!")
        if currency == "" or currency not in EXCHANGE_RATES.keys():
            raise Warning("Currency invalid!")
        if amount > self.__balance:
            raise Warning("Deposit amount too big!")
        if currency == self.__currency:
            self.__balance -= amount
        else:
            withdraw_amount = convert(amount, currency, self.__currency)
            if withdraw_amount > self.__balance:
                raise Warning("Deposit amount too big!")
            self.__balance -= withdraw_amount
