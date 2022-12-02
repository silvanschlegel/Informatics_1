#!/usr/bin/env python3

# Implement this class. Stick to the naming that is introduced in the
# UML diagram. Do not change the class name or the method signatures
# or the automated grading won't work.

from movie import Movie
from moviebox import MovieBox


class Library:

    def __init__(self):
        self.__movies = []

    def add_movie(self, movie):
        if not isinstance(movie, Movie) and not isinstance(movie, MovieBox):
            raise Warning

        self.__movies.append(movie)

    def get_movies(self):
        movie_list = []
        for i in self.__movies:
            if isinstance(i, MovieBox):
                continue
            if i not in movie_list:
                movie_list.append(i)
        return sorted(movie_list, key=lambda x: x.get_title())


    def get_total_duration(self):
        total_duration = 0
        for i in self.__movies:
            total_duration += i.get_duration()
        return total_duration
