#!/usr/bin/env python3

from unittest import TestCase
from cube import Cube
from cone import Cone
from cylinder import Cylinder


class CubeTest(TestCase):

    # Test if the getter for color works properly
    def test_cube_get_color(self):
        cube = Cube(10, "red", True)
        actual = cube.get_color()
        self.assertEqual(actual, "red")

    def test_cone_get_color(self):
        cone = Cone(10, 5, 6.4, "yellow", False)
        actual = cone.get_color()
        self.assertEqual(actual, "yellow")

    def test_cylinder_get_color(self):
        cylinder = Cylinder(3.5, 6.3, "blue", True)
        actual = cylinder.get_color()
        self.assertEqual(actual, "blue")

    #test roundedness of area and volume
    def test_cone_rounded(self):
        cone = Cone(10,5,6.4,"black", True)
        actual = cone.get_area()
        expected = 514.96
        self.assertEqual(actual,expected)

    def test_cone_rounded_1(self):
        cone = Cone(10,5,6.4,"black", True)
        actual = cone.get_volume()
        expected = 523.33
        self.assertEqual(actual,expected)

    def test_cylinder_rounded(self):
        cylinder = Cylinder(10,5,"black", True)
        actual = cylinder.get_area()
        expected = 942
        self.assertEqual(actual,expected)

    def test_cylinder_rounded_1(self):
        cylinder = Cylinder(10,5,"black", True)
        actual = cylinder.get_volume()
        expected = 1570
        self.assertEqual(actual,expected)

    def test_cube_rounded(self):
        cube = Cube(10,"black", True)
        actual = cube.get_area()
        expected = 600
        self.assertEqual(actual,expected)

    def test_cube_rounded_1(self):
        cube = Cube(10,"black", True)
        actual = cube.get_volume()
        expected = 1000
        self.assertEqual(actual,expected)





    # This current test suite only contains very basic test cases. By now,
    # you have some experience in writing test cases. We strongly encourage
    # you to implement further test cases. The additional tests can be run via
    # 'Test&Run' in ACCESS. These tests won't affect the grading of your solution
    # directly, but they can help you with identifying relevant corner cases
    # that you have to consider in your implementation.
