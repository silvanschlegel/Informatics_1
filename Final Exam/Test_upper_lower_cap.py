def upper_lower_capitalize(string):
    return string.upper(), string.lower(), string.capitalize()

from unittest import TestCase

class TestSuite(TestCase):
    def test_upper(self):
        a = "hallo"
        b = upper_lower_capitalize(a)
        self.assertEqual(a.upper(), b[0])
    def test_lower(self):
        a = "HALLO"
        b = upper_lower_capitalize(a)
        self.assertEqual(a.lower(), b[1])

    def test_cap(self):
        a = "HALLO"
        b = upper_lower_capitalize(a)
        self.assertEqual("Hallo", b[2])


