#!/usr/bin/env python3
from unittest import TestCase
from script import evolve


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
class EvolveTestSuite(TestCase):

    def test_glider(self):
        field = (
            "--------------",
            "|            |",
            "|  ###       |",
            "|  #         |",
            "|   #        |",
            "|            |",
            "--------------"
        )
        expected = ((
                        "--------------",
                        "| ###        |",
                        "| #          |",
                        "|  #         |",
                        "|            |",
                        "|            |",
                        "--------------"
                    ), 5)
        actual = evolve(field, 4)
        self.assertEqual(actual, expected)

    def test_world_no_tuple(self):
        field = ["--------------",
                 "|            |",
                 "|  ###       |",
                 "|  #         |",
                 "|   #        |",
                 "|            |",
                 "--------------"]


        self.assertRaises(Warning, evolve, field, 4)

    def test_world_tuple_no_strings(self):
        field = (
            10,
            "|            |",
            "|  ###       |",
            "|  #         |",
            "|   #        |",
            "|            |",
            "--------------"
        )

        self.assertRaises(Warning, evolve, field, 4)

    def test_world_empty_world(self):
        field = ()

        self.assertRaises(Warning, evolve, field, 4)

    def test_world_wrong_character(self):
        field = (
            "--------------",
            "|            |",
            "|  ##+       |",
            "|  #S         |",
            "|   #        |",
            "|            |",
            "--------------"
        )

        self.assertRaises(Warning, evolve, field, 4)

    def test_character_at_wrong_position1(self):
        field = (
            "--------------",
            "-            |",
            "|  ###       |",
            "|  #         |",
            "|   #        |",
            "|            |",
            "--------------"
        )

        self.assertRaises(Warning, evolve, field, 4)

    def test_character_at_wrong_position2(self):
        field = (
            "--------------",
            "#            |",
            "|  ###       |",
            "|  #         |",
            "|   #        |",
            "|            |",
            "--------------"
        )

        self.assertRaises(Warning, evolve, field, 4)

    def test_character_at_wrong_position3(self):
        field = (
            "--------------",
            "|            |",
            "|  ##-       |",
            "|  #         |",
            "|   #        |",
            "|            |",
            "--------------"
        )

        self.assertRaises(Warning, evolve, field, 4)

    def test_character_at_wrong_position4(self):
        field = (
            "--------------",
            "|            |",
            "|  ##|       |",
            "|  #         |",
            "|   #        |",
            "|            |",
            "--------------"
        )

        self.assertRaises(Warning, evolve, field, 4)

    def test_length_of_line_tooLong(self):
        field = (
            "--------------",
            "|            |",
            "|  ###          |",
            "|  #         |",
            "|   #        |",
            "|            |",
            "--------------"
        )

        self.assertRaises(Warning, evolve, field, 4)

    def test_length_of_line_tooShort(self):
        field = (
            "--------------",
            "|            |",
            "|  ##-    |",
            "|  #         |",
            "|   #        |",
            "|            |",
            "--------------"
        )

        self.assertRaises(Warning, evolve, field, 4)

    def test_size_too_small_height_and_length(self):
        field = (
            "--",
            "--"
        )

        self.assertRaises(Warning, evolve, field, 4)

    def test_size_too_small_length(self):
        field = (
            "--",
            "||",
            "||",
            "||",
            "||",
            "||",
            "--"
        )

        self.assertRaises(Warning, evolve, field, 4)

    def test_stepts_negative(self):
        field = (
            "--------------",
            "|            |",
            "|  ###       |",
            "|  #         |",
            "|   #        |",
            "|            |",
            "--------------"
        )

        self.assertRaises(Warning, evolve, field, -4)

    def test_stepts_0(self):
        field = (
            "--------------",
            "|            |",
            "|  ###       |",
            "|  #         |",
            "|   #        |",
            "|            |",
            "--------------"
        )

        self.assertRaises(Warning, evolve, field, 0)

    def test_stepts_float(self):
        field = (
            "--------------",
            "|            |",
            "|  ###       |",
            "|  #         |",
            "|   #        |",
            "|            |",
            "--------------"
        )

        self.assertRaises(Warning, evolve, field, 1.0)
