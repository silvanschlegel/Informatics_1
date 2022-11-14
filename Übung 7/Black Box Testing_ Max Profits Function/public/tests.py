#!/usr/bin/env python3
from unittest import TestCase
from script import max_profit

# Implement this test suite. Make sure that you define test
# methods and that each method _directly_ includes an assertion
# in the body, or -otherwise- the grading will mark the test
# suite as invalid.
class MaxProfitTest(TestCase):
    def test_shortintlist(self):
        self.assertEqual(max_profit([1,2,3,4,5]), 4)

    def test_longintlist(self):
        self.assertEqual(max_profit([1,2,3,4,5,6,7,8,9,10]), 9)

    def test_prices_not_always_rising(self):
        self.assertEqual(max_profit([3,4,5,2,1,1,1,10,1,3,4,3,3,3,100]), 99)

    def test_check_if_lowest_price_is_after_highest_price(self):
        self.assertEqual(max_profit([2,10,1]), 8)

    def test_Invalid_Input_Type_Float(self):
        self.assertEqual(max_profit(1.0), "Invalid Input Type")

    def test_Invalid_Input_Type_Int(self):
        self.assertEqual(max_profit(1), "Invalid Input Type")

    def test_Invalid_Input_Type_String(self):
        self.assertEqual(max_profit("string"), "Invalid Input Type")

    def test_Invalid_Input_Type_dict(self):
        self.assertEqual(max_profit({1.0: "a", 2.0: "b", 3.0: "c"}), "Invalid Input Type")

    def test_Empty_Price_List(self):
        self.assertEqual(max_profit([]), "Empty Price List")

    def test_Invalid_Data_Type_in_List_Float(self):
        self.assertEqual(max_profit([1,2,3,4.0]), "Invalid Data Type within List")

    def test_Invalid_Data_Type_in_List_Float_negative(self):
        self.assertEqual(max_profit([1,2,3,-4.0]), "Invalid Data Type within List")

    def test_Invalid_Data_Type_in_List_String(self):
        self.assertEqual(max_profit([1,2,"incorrect"]), "Invalid Data Type within List")

    def test_Invalid_Data_Type_in_List_Tuple(self):
        self.assertEqual(max_profit([1,2,3,(4,)]), "Invalid Data Type within List")

    def test_Invalid_Data_Type_in_List_List(self):
        self.assertEqual(max_profit([1,2,3,[4]]), "Invalid Data Type within List")

    def test_Invalid_Prices_negative_1(self):
        self.assertEqual(max_profit([1,2,3,-4]), "Invalid Prices")

    def test_Invalid_Prices_negative(self):
        self.assertEqual(max_profit([1,2,3,-4]), "Invalid Prices")

    def test_List_only_contains_1_element(self):
        self.assertEqual(max_profit([1]), 0)

    def test_List_only_contains_same_element(self):
        self.assertEqual(max_profit([1,1,1,1,1,1,1]), 0)

    def test_smaller_values_only_after_bigger_values(self):
        self.assertEqual(max_profit([5,4,3,2,1]), 0)



