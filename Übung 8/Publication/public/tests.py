#!/usr/bin/env python3

from unittest import TestCase
from script import Publication


class PublicTestSuite(TestCase):

    def test_example(self):
        a = Publication(["A"], "B", 1234)
        b = Publication(["A"], "B", 1234)
        self.assertEqual(a, b)

    def test_repr_(self):
        a = Publication(["A"], "B", 1234)
        b = "Publication([\"A\"], \"B\", 1234)"
        self.assertEqual(str(a), b)

    def test_str_(self):
        a = Publication(["A"], "B", 1234)
        b = "Publication([\"A\"], \"B\", 1234)"
        self.assertEqual(str(a), b)

    def test_gt_1(self):
        p1 = Publication(["Schlegel", "Waltenspül"], "Wurmhöhle 17", 2022)
        p2 = Publication(["Schlegel"], "Wurmhöhle 17", 2022)
        self.assertEqual(p1 > p2, True)

    def test_gt_2(self):
        p1 = Publication(["Schlegel", "Waltenspül"], "Wurmhöhle 17", 2022)
        p2 = Publication(["Schlegel", "A", "B"], "Wurmhöhle 17", 2022)
        self.assertEqual(p1 > p2, False)

    def test_gt_3(self):
        p1 = Publication(["Schlegel"], "Wurmhöhle 17", 2021)
        p2 = Publication(["Schlegel"], "Wurmhöhle 17", 2022)
        self.assertEqual(p1 > p2, False)

    def test_gt_3(self):
        p1 = Publication(["Schlegel"], "b", 2021)
        p2 = Publication(["Schlegel"], "a", 2022)
        self.assertEqual(p1 > p2, True)

    def test_lt_1(self):
        p1 = Publication(["Schlegel", "Waltenspül"], "Wurmhöhle 17", 2022)
        p2 = Publication(["Schlegel"], "Wurmhöhle 17", 2022)
        self.assertEqual(p2 < p1, True)

    def test_lt_2(self):
        p1 = Publication(["Schlegel", "Waltenspül"], "Wurmhöhle 17", 2022)
        p2 = Publication(["Schlegel"], "Wurmhöhle 17", 2022)
        self.assertEqual(p1 < p2, False)

    def test_lt_3(self):
        p1 = Publication(["Schlegel"], "ab", 2022)
        p2 = Publication(["Schlegel"], "aa", 2022)
        self.assertEqual(p1 < p2, False)

    def test_lt_4(self):
        p1 = Publication(["Schlegel"], "aaa", 2022)
        p2 = Publication(["Schlegel"], "aa", 2022)
        self.assertEqual(p1 < p2, False)

    def test_lt_5(self):
        p1 = Publication(["Schlegel"], "a", 2022)
        p2 = Publication(["Schlegel"], "aa", 2022)
        self.assertEqual(p1 < p2, True)

    def test_ge_1(self):
        p1 = Publication(["Schlegel", "Waltenspuel"], "Wurmhoehle 17", 2022)
        p2 = Publication(["Schlegel"], "Wurmhoehle 17", 2022)
        self.assertEqual(p1 >= p2, True)

    def test_ge_2(self):
        p1 = Publication(["Schlegel", "Waltenspuel"], "Wurmhoehle 17", 2022)
        p2 = Publication(["Schlegel", "Waltenspuel", "Zuerich"], "Wurmhoehle 17", 2022)
        self.assertEqual(p1 >= p2, False)

    def test_ge_3(self):
        p1 = Publication(["Schlegel", "Waltenspuel"], "aa", 2022)
        p2 = Publication(["Schlegel", "Waltenspuel"], "a", 2022)
        self.assertEqual(p1 >= p2, True)

    def test_ge_4(self):
        p1 = Publication(["Schlegel", "Waltenspuel"], "aa", 2022)
        p2 = Publication(["Schlegel", "Waltenspuel"], "aaa", 2022)
        self.assertEqual(p1 >= p2, False)

    def test_ge_5(self):
        p1 = Publication(["Schlegel", "Waltenspuel"], "a", 2020)
        p2 = Publication(["Schlegel", "Waltenspuel"], "a", 2022)
        self.assertEqual(p1 >= p2, False)

    def test_ge_6(self):
        p1 = Publication(["Schlegel", "Waltenspuel"], "aa", 2022)
        p2 = Publication(["Schlegel", "Waltenspuel"], "aa", 2022)
        self.assertEqual(p1 >= p2, True)


    def test_le_1(self):
        p1 = Publication(["Schlegel", "Waltenspül"], "Wurmhöhle 17", 2022)
        p2 = Publication(["Schlegel"], "Wurmhöhle 17", 2022)
        self.assertEqual(p2 <= p1, True)

    def test_le_2(self):
        p1 = Publication(["Schlegel", "Waltenspül"], "Wurmhöhle 17", 2022)
        p2 = Publication(["Schlegel"], "Wurmhöhle 17", 2022)
        self.assertEqual(p1 <= p2, False)

    def test_le_3(self):
        p1 = Publication(["Schlegel"], "aaa", 2022)
        p2 = Publication(["Schlegel"], "aa", 2022)
        self.assertEqual(p1 <= p2, False)

    def test_le_4(self):
        p1 = Publication(["Schlegel"], "aa", 2022)
        p2 = Publication(["Schlegel"], "aa", 2022)
        self.assertEqual(p1 <= p2, True)

    def test_le_5(self):
        p1 = Publication(["Schlegel"], "a", 2022)
        p2 = Publication(["Schlegel"], "aa", 2022)
        self.assertEqual(p1 <= p2, True)

    def test_ne1(self):
        p1 = Publication(["Schlegel", "Waltenspül"], "Wurmhöhle 17", 2022)
        p2 = Publication(["Schlegel"], "Wurmhöhle 17", 2022)
        self.assertEqual(p1 != p2, True)

    def test_ne2(self):
        p1 = Publication(["Schlegel"], "Wurmhöhle 17", 2022)
        p2 = Publication(["Schlegel"], "Wurmhöhle 17", 2022)
        self.assertEqual(p1 != p2, False)

    def test_eq_1(self):
        p1 = Publication(["Schlegel", "Waltenspül"], "Wurmhöhle 17", 2022)
        p2 = Publication(["Schlegel"], "Wurmhöhle 17", 2022)
        self.assertEqual(p1 == p2, False)

    def test_eq_2(self):
        p1 = Publication(["Schlegel"], "Wurmhöhle 17", 2022)
        p2 = Publication(["Schlegel"], "Wurmhöhle 17", 2022)
        self.assertEqual(p1 == p2, True)

    def test_eq_3(self):
        p1 = Publication(["Schlegel"], "Wurmhöh", 2022)
        p2 = Publication(["Schlegel"], "Wurmhöhle 17", 2022)
        self.assertEqual(p1 == p2, False)










    # This current test suite only contains one very basic test case. By now,
    # you have some experience in writing test cases. We strongly ecncourage
    # you to implement further test cases. The additional tests can be run via
    # 'Test&Run' in ACCESS. These tests won't affect the grading of your solution
    # directly, but they can help you with identifying relevant corner cases
    # that you have to consider in your implementation.
