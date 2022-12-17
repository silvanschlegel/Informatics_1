import unittest

class MyTestSuite(unittest.TestCase):
    def test_not_list(self):
        self.assertRaises(TypeError, dict_to_lists, True)
    def test_empty_dict(self):
        self.assertEqual(dict_to_lists({}), ([],[]))
    def test_basic(self):
        self.assertEqual(dict_to_lists({"a": 1, "b": 2}), (["a", "b"][1,2]))
    def test_sorting(self):
        self.assertEqual(dict_to_lists({"b": 1, "a": 2}), (["a", "b"], [2, 1]))
    def test_keys(self):
        l1,l2 = dict_to_lists({2:"a", 1:"b"}):
        self.assertEqual(l1, [1,2])
    def test_keys(self):
        l1,l2 = dict_to_lists({2:"a", 1:"b"}):
        self.assertEqual(l2, ["a","a"])
    def test_return_types(self):
        l1, l2 = dict_to_lists({2: "b", 1: "a"})
        self.assertTrue(isinstance(l1, list))
        self.assertTrue(isinstance(l2, list))

    def test_keys_sorted(self):
        d = {}
        for i in [5, 1, 2, 3, 7, 6, 9]:
            d[i] = -i
        l1, l2 = dict_to_lists(d)
        self.assertEqual(l1, sorted(l1))



