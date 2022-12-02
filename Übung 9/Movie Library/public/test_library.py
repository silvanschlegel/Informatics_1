#!/usr/bin/env python3

from unittest import TestCase
from movie import Movie
from moviebox import MovieBox
from library import Library

class LibraryTest(TestCase):

    def setUp(self) -> None:
        self.__library = Library()



    def test_repr_movie(self):
        actual = repr(Movie("T", ["A", "B"], 123))
        expected = 'Movie("T", ["A", "B"], 123)'
        self.assertEqual(expected, actual)



    def test_repr_moviebox(self):
        actual = repr(MovieBox("T", [Movie("T2", ["A", "B"], 234)]))
        expected = 'MovieBox("T", [Movie("T2", ["A", "B"], 234)])'
        self.assertEqual(expected, actual)

    def test_library(self):
        a = Movie("The Shawshank Redemption", ["Robbins", "Freeman"], 142)
        b = Movie("The Godfather", ["Brando", "Pacino"], 175)
        c = Movie("12 Angry Men", ["Fonda", "Cobb"], 96)
        d = MovieBox("Top Movies", [b, c])
        l = Library()
        l.add_movie(a)
        l.add_movie(d)
        self.assertEqual(413, l.get_total_duration())

    def test_library_duplicates(self):
        a = Movie("The Shawshank Redemption", ["Robbins", "Freeman"], 142)
        b = Movie("The Godfather", ["Brando", "Pacino"], 175)
        c = Movie("12 Angry Men", ["Fonda", "Cobb"], 96)
        x = Movie("12 Angry Men", ["Fonda", "Cobb"], 96)
        d = MovieBox("Top Movies", [b, c])
        l = Library()
        l.add_movie(c)
        l.add_movie(x)
        actual = l.get_movies()
        expected = [Movie("12 Angry Men", ["Fonda", "Cobb"], 96)]
        self.assertEqual(actual, expected)

    def test_library_duration_1(self):
        a = Movie("The Shawshank Redemption", ["Robbins", "Freeman"], 142)
        b = Movie("The Godfather", ["Brando", "Pacino"], 175)
        c = Movie("12 Angry Men", ["Fonda", "Cobb"], 96)
        x = Movie("12 Angry Men", ["Fonda", "Cobb"], 96)
        d = MovieBox("Top Movies", [x])
        l = Library()
        l.add_movie(d)
        l.add_movie(x)
        actual = l.get_total_duration()
        expected = 192
        self.assertEqual(actual, expected)

    def test_library_duration_2(self):
        a = Movie("The Shawshank Redemption", ["Robbins", "Freeman"], 142)
        b = Movie("The Godfather", ["Brando", "Pacino"], 175)
        c = Movie("12 Angry Men", ["Fonda", "Cobb"], 96)
        x = Movie("12 Angry Men", ["Fonda", "Cobb"], 96)
        m = MovieBox("Top Movies", [c])
        d = MovieBox("Top Movies", [m])
        l = Library()
        l.add_movie(d)
        l.add_movie(x)
        actual = l.get_total_duration()
        expected = 192
        self.assertEqual(actual, expected)

    def test_movie_eq(self):
        a = Movie("The Shawshank Redemption", ["Robbins", "Freeman"], 142)
        b = Movie("The Godfather", ["Brando", "Pacino"], 175)
        self.assertEqual(False, a.__eq__(b))

    def test_moviebox_eq_1(self):
        a = Movie("The Shawshank Redemption", ["Robbins", "Freeman"], 142)
        b = Movie("The Godfather", ["Brando", "Pacino"], 175)
        d = MovieBox("Top Movies", [a])
        e = MovieBox("Top Movies", [b])
        self.assertEqual(False, d.__eq__(e))

    def test_moviebox_eq_2(self):
        a = Movie("The Shawshank Redemption", ["Robbins", "Freeman"], 142)
        b = Movie("The Godfather", ["Brando", "Pacino"], 175)
        d = MovieBox("Top Movies", [a])
        e = MovieBox("Top Movies", [a])
        self.assertEqual(True, d.__eq__(e))

    def test_MovieBox_duplicates(self):
        a = Movie("The Shawshank Redemption", ["Robbins", "Freeman"], 142)
        b = Movie("The Shawshank Redemption", ["Robbins", "Freeman"], 142)
        d = MovieBox("Top Movies", [a,b])
        actual = d.__repr__()
        expected = "MovieBox(\"Top Movies\", [Movie(\"The Shawshank Redemption\", [\"Robbins\", \"Freeman\"], 142)])"
        self.assertEqual(actual,expected)

    def test_library_get_movies_1(self):
        a = Movie("A", ["A"], 100)
        b = Movie("B", ["B"], 100)
        c = Movie("C", ["Fonda", "Cobb"], 96)
        d = MovieBox("Top Movies", [b, c])
        e = Movie("D", ["A"], 100)
        l = Library()
        l.add_movie(a)
        l.add_movie(d)
        l.add_movie(e)
        actual = l.get_movies()
        expected = [Movie("A", ["A"], 100), Movie("D", ["A"], 100)]
        self.assertEqual(actual, expected)

    def test_library_get_movies_2(self):
        a = Movie("A", ["A"], 100)
        b = Movie("B", ["B"], 100)
        c = Movie("C", ["Fonda", "Cobb"], 96)
        d = MovieBox("Top Movies", [b, c])
        e = Movie("D", ["A"], 100)
        l = Library()
        l.add_movie(e)
        l.add_movie(d)
        l.add_movie(a)
        actual = l.get_movies()
        expected = [Movie("A", ["A"], 100), Movie("D", ["A"], 100)]
        self.assertEqual(actual, expected)


    # This current test suite only contains very basic test cases. By now,
    # you have some experience in writing test cases. We strongly encourage
    # you to implement further test cases. The additional tests can be run via
    # 'Test&Run' in ACCESS. These tests won't affect the grading of your solution
    # directly, but they can help you with identifying relevant corner cases
    # that you have to consider in your implementation.
