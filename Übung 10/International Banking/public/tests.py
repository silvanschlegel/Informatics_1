#!/usr/bin/env python3
from unittest import TestCase

# You need to add missing imports to make the test work!
from bank_account import BankAccount
from currency_converter import convert


class PrivateFunctionalTestSuite(TestCase):

    def test_0_convert(self):
        actual = convert(1.0, "EUR", "CHF")
        expected = 1.10
        self.assertAlmostEqual(expected, actual, delta=0.0001)
        
    def test_1_basic_banking(self):
        sut = BankAccount("CHF")
        sut.deposit(100.0, "CHF")
        sut.withdraw(10.0, "EUR")
        actual = sut.get_balance()
        expected = 89.0
        self.assertAlmostEqual(expected, actual, delta=0.0001)

    def test_deposit_amount_not_number(self):
        sut = BankAccount("CHF")
        self.assertRaises(Warning, sut.deposit,"100.0", "CHF")

    def test_deposit_currency_not_str(self):
        sut = BankAccount("CHF")
        self.assertRaises(Warning, sut.deposit,100.0, 10)

    def test_withdraw_amount_not_number(self):
        sut = BankAccount("CHF")
        self.assertRaises(Warning, sut.deposit, "100.0", "CHF")

    def test_withdraw_currency_not_str(self):
        sut = BankAccount("CHF")
        self.assertRaises(Warning, sut.deposit, 100.0, 10)

    def test_withdraw_currency_not_in_Exchange_Rates(self):
        sut = BankAccount("CHF")
        self.assertRaises(Warning, sut.deposit, 100.0, "Lira")

    def test_deposit_not_in_Exchange_Rates(self):
        sut = BankAccount("CHF")
        self.assertRaises(Warning, sut.deposit,100.0, "Lira")

    def test_withdraw_negative(self):
        sut = BankAccount("CHF")
        self.assertRaises(Warning, sut.withdraw, -1, "CHF")

    def test_deposit_negative(self):
        sut = BankAccount("CHF")
        self.assertRaises(Warning, sut.deposit, -1, "CHF")

    def test_deposit_GBP(self):
        sut = BankAccount("CHF")
        sut.deposit(100, "GBP")
        actual = sut.get_balance()
        expected = 128.865979381
        self.assertAlmostEqual(actual,expected,delta=0.0001)

    def test_deposit_EUR_to_CAD(self):
        sut = BankAccount("CAD")
        sut.deposit(100, "EUR")
        actual = sut.get_balance()
        expected = 146.198830409
        self.assertAlmostEqual(actual,expected,delta=0.0001)

    def test_withdraw_CHF_to_JPY(self):
        sut = BankAccount("JPY")
        sut.deposit(100, "CHF")
        actual = sut.get_balance()
        expected = 109.649122807
        self.assertAlmostEqual(actual,expected,delta=0.0001)

    def test_convert_1(self):
        self.assertRaises(Warning, convert, 100, "Lira", "CHF")
    def test_convert_2(self):
        self.assertRaises(Warning, convert, 100,"CHF", "Lira")

    def test_withdraw_too_big(self):
        sut = BankAccount("CHF")
        sut.deposit(100, "CHF")
        self.assertRaises(Warning, sut.withdraw, 100.0, "EUR")
    # This current test suite only contains one very basic test case. By now,
    # you have some experience in writing test cases. We strongly encourage
    # you to implement further test cases. The additional tests can be run via
    # 'Test&Run' in ACCESS. These tests won't affect the grading of your solution
    # directly, but they can help you with identifying relevant corner cases
    # that you have to consider in your implementation.
