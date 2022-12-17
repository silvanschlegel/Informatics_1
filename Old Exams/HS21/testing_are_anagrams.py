import unittest

class MyTestSuite(unittest.TestCase):
    def test_basic_anagram(self):
        self.assertTrue(are_anagrams("dog", "god"))
    def test_case_sensitivity(self):
        self.assertTrue(are_anagrams("Cat","Tac"))
    def test_numeric(self):
        self.assertTrue(are_anagrams("cat1234","tac"))
    def test_error_a(self):
        self.assertRaises(TypeError,are_anagrams, ["cat"],"tac")
    def test_error_b(self):
        self.assertRaises(TypeError,are_anagrams, "cat",["tac"])
    def test_not_anagram(self):
        self.assertFalse(are_anagrams("dog", "doc"))
    def test_spacing(self):
        self.assertTrue(are_anagrams("The Meaning of Life.", "The fine game of nil!"))
    def test_not_isalpha(self):
        self.assertTrue(are_anagrams("cat_","tac????"))
    def test_empty(self):
        self.assertTrue(are_anagrams("", ""))
    def test_false_different_counts(self):
        self.assertFalse("xxxyy", "yyyxx")


