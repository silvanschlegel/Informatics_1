#!/usr/bin/env python3

from unittest import TestCase
from knight import Knight
from rogue import Rogue
from mage import Mage


class TestBattle(TestCase):

    def test_get_health_knight(self):
        sut = Knight("Arthur", 3)
        actual = sut.get_health()
        expected = (150, 150)
        self.assertEqual(expected, actual)

    def test_get_health_mage(self):
        sut = Mage("Philipp", 10)
        actual = sut.get_health()
        expected = (500, 500)
        self.assertEqual(expected, actual)

    def test_get_health_rogue(self):
        sut = Mage("Heiri", 1)
        actual = sut.get_health()
        expected = (50, 50)
        self.assertEqual(expected, actual)

    def test_basic_attack(self):
        sut = Knight("Arthur", 3)
        actual = sut.get_health()
        expected = (150, 150)
        self.assertEqual(expected, actual)

    def test_knight_attack(self):
        k = Knight("Arthur", 3)
        r = Rogue("Shades", 3)
        k.attack(r)
        actual = r.get_health()[0]
        expected = 150 - round(0.8 * (3 * 10 + 0))
        self.assertEqual(expected, actual)

    def test_knight_lvl(self):
        k = Knight("Arthur", 6)
        self.assertEqual(6,k.get_lvl())

    def test_mage_attacks_knight(self):
        k = Knight("Arthur", 3)
        r = Mage("Dumbledore", 3)
        r.attack(k)
        actual = k.get_health()[0]
        expected = 150 - round(((3*10)*1.25))
        self.assertEqual(expected, actual)

    def test_knight_attacks_mage(self):
        k = Knight("Arthur", 3)
        r = Mage("Dumbledore", 3)
        k.attack(r)
        actual = r.get_health()[0]
        expected = 150 - round((((3*10)*0.8)*1.5))
        self.assertEqual(expected, actual)

    def test_mage_attacks_mage(self):
        k = Mage("Gandalf", 3)
        r = Mage("Dumbledore", 3)
        k.attack(r)
        actual = r.get_health()[0]
        expected = 150 - round((round((3*10)*1.25)*1.5))
        self.assertEqual(expected, actual)

    def test_knight_dead(self):
        k = Knight("Arthur", 3)
        r = Mage("Dumbledore", 100)
        r.attack(k)
        actual = k.is_alive()
        expected = False
        self.assertEqual(expected, actual)

    # This current test suite only contains very basic test cases. By now,
    # you have some experience in writing test cases. We strongly encourage
    # you to implement further test cases. The additional tests can be run via
    # 'Test&Run' in ACCESS. These tests won't affect the grading of your solution
    # directly, but they can help you with identifying relevant corner cases
    # that you have to consider in your implementation.
