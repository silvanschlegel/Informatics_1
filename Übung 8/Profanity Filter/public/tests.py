#!/usr/bin/env python3

from unittest import TestCase
from script import ProfanityFilter


class PublicTestSuite(TestCase):

    def test_example(self):
        f = ProfanityFilter(["duck", "shot", "batch", "mastard"], "?#$")
        msg = "abc defghi mastard jklmno"
        actual = f.filter(msg)
        expected = "abc defghi ?#$?#$? jklmno"
        self.assertEqual(expected, actual)

    def test_emptyinput(self):
        f = ProfanityFilter(["duck", "shot", "batch", "mastard"], "?#$")
        msg = ""
        actual = f.filter(msg)
        expected = ""
        self.assertEqual(expected, actual)

    def test_input_false(self):
        f = ProfanityFilter(["duck", "shot", "batch", "mastard"], "?#$")
        self.assertRaises(Warning, f.filter, 10)

    def test_keywords_sorted(self):
        f = ProfanityFilter(["duck", "shot", "batch", "mastard"], "?#$")
        msg = "mastardduck"
        actual = f.filter(msg)
        expected = "?#$?#$??#$?"
        self.assertEqual(expected, actual)

    def test_two_words_in_1_string(self):
        f = ProfanityFilter(["duck", "shot", "batch", "mastard"], "?#$")
        msg = "mastardduck"
        actual = f.filter(msg)
        expected = "?#$?#$??#$?"
        self.assertEqual(expected, actual)


    def test_case_insensitive(self):
        f = ProfanityFilter(["duck", "shot", "batch", "mastard"], "?#$")
        msg = "abc defghi MAstard jklmno"
        actual = f.filter(msg)
        expected = "abc defghi ?#$?#$? jklmno"
        self.assertEqual(expected, actual)

    def test_other_template(self):
        f = ProfanityFilter(["instagram", "staudenstrasse9a", "9472Grabs", "mastard"], "silvan")
        msg = "Hallo, mein Name ist Silvan und ich wohne an der Staudenstrasse9a in 9472grabs mastard instagram"
        actual = f.filter(msg)
        expected = "Hallo, mein Name ist Silvan und ich wohne an der silvansilvansilv in silvansil silvans silvansil"
        self.assertEqual(expected, actual)



    # This current test suite only contains one very basic test case. By now,
    # you have some experience in writing test cases. We strongly ecncourage
    # you to implement further test cases. The additional tests can be run via
    # 'Test&Run' in ACCESS. These tests won't affect the grading of your solution
    # directly, but they can help you with identifying relevant corner cases
    # that you have to consider in your implementation.
