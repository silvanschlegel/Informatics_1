#!/usr/bin/env python3

# Implement this class. Stick to the naming that is introduced in the
# UML diagram. Do not change the class name or the method signatures
# or the automated grading won't work.

from movie import Movie


class MovieBox(Movie):

    def __init__(self, title, movies):
        if title == "" or movies == []:
            raise Warning

        for i in movies:
            if not isinstance(i, Movie):
                raise Warning

        self.__title = title
        movies = sorted(movies, key=lambda x: x.get_title())
        for i in range(len(movies)-1):
            for j in range(1,len(movies)):
                if movies[i].__eq__(movies[j]):
                    movies.remove(movies[j])
        self.__movies = movies

    def __repr__(self):
        return f'MovieBox(\"{self.__title}\", {self.__movies})'

    def __eq__(self, other):
        return self.__title == other.__title and self.__movies == other.__movies

    def __hash__(self):
        return hash((self.__title, self.__movies))

    def get_title(self):
        return self.__title

    def get_actors(self):
        actors = []
        for i in self.__movies:
            actors.append(i.get_actors())
        return actors

    def get_duration(self):
        duration = 0
        for i in self.__movies:
            duration += i.get_duration()
        return duration

    def get_movies(self):
        return self.__movies[:]


    # also implement the required special functions
