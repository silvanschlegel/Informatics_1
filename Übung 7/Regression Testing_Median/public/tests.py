#!/usr/bin/env python3
from unittest import TestCase
from script import median

# Extend the test suite with regression tests that cover the
# meaningful bug reports. Make sure that you define test methods
# and that each method _directly_ includes an assertion in the
# body, or -otherwise- the grading will mark the test suite as
# invalid.
class MedianTests(TestCase):

    def test_median_works_for_single_elements(self):
        self.assertEqual(13, median([13]))

    def test_median_works_for_sorted_numbers(self):
        self.assertEqual(2, median([1, 2, 6]))

    def test_median_works_for_unsorted_numbers(self):
        self.assertEqual(2, median([6, 1, 2]))

    def test_median_works_for_odd_lists(self):
        self.assertEqual(2, median([6, 1, 2]))

    def test_median_works_for_even_lists(self):
        self.assertEqual(3, median([5, 1]))

    def test_empty_list(self):
        self.assertEqual(None, median([]))

    def test_list_with_same_elements(self):
        self.assertEqual(0, median([0,0,0,0,0,0,0]))

    def test_list_with_123(self):
        self.assertEqual(2, median([1,2,3]))

    def test_list_with_only_floats(self):
        self.assertAlmostEqual(2.33398, median([1.22,2.33398,2.33398,3.598523]))

    def test_list_with_floats_and_ints(self):
        self.assertAlmostEqual(2.33398, median([1,2.33398,2.33398,3]))
