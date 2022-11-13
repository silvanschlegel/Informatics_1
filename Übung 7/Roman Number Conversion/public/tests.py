#!/usr/bin/env python3
from unittest import TestCase
from script import convert_roman_to_int


# You are supposed to develop the functionality in a test-driven way.
# Think about relevant test cases and extend the following test suite
# until all requirements of the description are covered. The test suite
# will be run against various correct and incorrect implementations, so
# make sure that you only test the `move` function and stick strictly
# to its defined signature.
#
# Make sure that you define test methods and that each method
# _directly_ includes an assertion in the body, or -otherwise- the
# grading will mark the test suite as invalid.
class ConversionTestSuite(TestCase):

    def _assert(self, roman, expected):
        actual = convert_roman_to_int(roman)
        m = f"should be {expected} but was {actual}"
        self.assertEqual(expected, actual, m)

    def test_simple_numeralI(self):
        self._assert("I", 1)

    def test_simple_numeralV(self):
        self._assert("V", 5)

    def test_simple_numeralX(self):
        self._assert("X", 10)

    def test_simple_numeralL(self):
        self._assert("L", 50)

    def test_simple_numeralC(self):
        self._assert("C", 100)

    def test_simple_numeralD(self):
        self._assert("D", 500)

    def test_simple_numeralM(self):
        self._assert("M", 1000)

    def test_simple_additive1(self):
        self._assert("XI", 11)

    def test_simple_additive2(self):
        self._assert("MD", 1500)

    def test_simple_subtraction_IV(self):
        self._assert("IV", 4)

    def test_simple_subtraction_CD(self):
        self._assert("CD", 400)

    def test_simple_subtraction_IX(self):
        self._assert("IX", 9)

    def test_simple_subtraction_XL(self):
        self._assert("XL", 40)

    def test_simple_subtraction_XC(self):
        self._assert("XC", 90)

    def test_simple_subtraction_CM(self):
        self._assert("CM", 900)

    def test_long_additive_numerals_VIII(self):
        self._assert("VIII", 8)

    def test_long_additive_numerals_MDC(self):
        self._assert("MDC", 1600)

    def test_long_additive_numerals_XVIII(self):
        self._assert("XVIII", 18)

    def test_long_additive_numerals_XXXIII(self):
        self._assert("XXXIII", 33)

    def test_long_additive_numerals_MXXXIII(self):
        self._assert("MXXXIII", 1033)

    def test_long_additive_subtractive_numerals_XIV(self):
        self._assert("XIV", 14)

    def test_long_additive_subtractive_numerals_XLI(self):
        self._assert("XLI", 41)

    def test_long_additive_subtractive_numerals_CDXLIV(self):
        self._assert("CDXLIV", 444)

    def test_long_additive_subtractive_numerals_CMXLIX(self):
        self._assert("CMXLIX", 949)

    def test_should_raise_warningXLS(self):
        self.assertRaises(Warning, convert_roman_to_int, "XLS")

    def test_should_raise_warningLL(self):
        self.assertRaises(Warning, convert_roman_to_int, "LL")

    def test_should_raise_warningIIMX(self):
        self.assertRaises(Warning, convert_roman_to_int, "IIMX")

    def test_should_raise_warningIVII(self):
        self.assertRaises(Warning, convert_roman_to_int, "IVII")

    def test_should_raise_warningIVIV(self):
        self.assertRaises(Warning, convert_roman_to_int, "IVIV")

    def test_should_raise_warningIXIX(self):
        self.assertRaises(Warning, convert_roman_to_int, "IXIX")

    def test_should_raise_warningVIIII(self):
        self.assertRaises(Warning, convert_roman_to_int, "VIIII")

    def test_throws_warningVV(self):
        self.assertRaises(Warning, convert_roman_to_int, "VV")

    def test_should_raise_warningDD(self):
        self.assertRaises(Warning, convert_roman_to_int, "DD")

    def test_should_raise_warningIVI(self):
        self.assertRaises(Warning, convert_roman_to_int, "IVI")

    def test_should_raise_warningIXI(self):
        self.assertRaises(Warning, convert_roman_to_int, "IXI")

    def test_should_raise_warningILI(self):
        self.assertRaises(Warning, convert_roman_to_int, "ILI")

    def test_should_raise_warningICI(self):
        self.assertRaises(Warning, convert_roman_to_int, "ICI")

    def test_should_raise_warningIDI(self):
        self.assertRaises(Warning, convert_roman_to_int, "IDI")

    def test_should_raise_warningIMI(self):
        self.assertRaises(Warning, convert_roman_to_int, "IMI")

    def test_should_raise_warningXLX(self):
        self.assertRaises(Warning, convert_roman_to_int, "XLX")

    def test_should_raise_warningXCX(self):
        self.assertRaises(Warning, convert_roman_to_int, "XCX")

    def test_should_raise_warningXDX(self):
        self.assertRaises(Warning, convert_roman_to_int, "XDX")

    def test_should_raise_warningXMX(self):
        self.assertRaises(Warning, convert_roman_to_int, "XMX")

    def test_should_raise_warningLDL(self):
        self.assertRaises(Warning, convert_roman_to_int, "LDL")

    def test_should_raise_warningLML(self):
        self.assertRaises(Warning, convert_roman_to_int, "LML")

    def test_should_raise_warningCDC(self):
        self.assertRaises(Warning, convert_roman_to_int, "CDC")

    def test_should_raise_warningCMC(self):
        self.assertRaises(Warning, convert_roman_to_int, "CMC")

    def test_should_raise_warningVIV(self):
        self.assertRaises(Warning, convert_roman_to_int, "VIV")

    def test_should_raise_warningLLX(self):
        self.assertRaises(Warning, convert_roman_to_int, "LLX")

    def test_should_raise_warningDCCCC(self):
        self.assertRaises(Warning, convert_roman_to_int, "DCCCC")

    def test_should_raise_warningIL(self):
        self.assertRaises(Warning, convert_roman_to_int, "IL")

    def test_should_raise_warningIC(self):
        self.assertRaises(Warning, convert_roman_to_int, "IC")

    def test_should_raise_warningID(self):
        self.assertRaises(Warning, convert_roman_to_int, "ID")

    def test_should_raise_warningIM(self):
        self.assertRaises(Warning, convert_roman_to_int, "IM")

    def test_should_raise_warningVX(self):
        self.assertRaises(Warning, convert_roman_to_int, "VX")

    def test_should_raise_warningVL(self):
        self.assertRaises(Warning, convert_roman_to_int, "VL")

    def test_should_raise_warningVC(self):
        self.assertRaises(Warning, convert_roman_to_int, "VC")

    def test_should_raise_warningVD(self):
        self.assertRaises(Warning, convert_roman_to_int, "VD")

    def test_should_raise_warningVM(self):
        self.assertRaises(Warning, convert_roman_to_int, "VM")

    def test_should_raise_warningLC(self):
        self.assertRaises(Warning, convert_roman_to_int, "LC")

    def test_should_raise_warningLD(self):
        self.assertRaises(Warning, convert_roman_to_int, "LD")

    def test_should_raise_warningLM(self):
        self.assertRaises(Warning, convert_roman_to_int, "LM")

    def test_should_raise_warningDM(self):
        self.assertRaises(Warning, convert_roman_to_int, "DM")

    def test_should_raise_warningXLM(self):
        self.assertRaises(Warning, convert_roman_to_int, "XLM")

    def test_any_M_MMMMMMMMI(self):
        self._assert("MMMMMMMMI", 8001)

    def test_CDXC(self):
        self._assert("CDXC", 490)

    def test_XLIX(self):
        self._assert("XLIX", 49)

    def test_easy_XI(self):
        self.assertEqual(convert_roman_to_int("XI"), 11)
