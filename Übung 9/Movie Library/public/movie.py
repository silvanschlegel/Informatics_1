#!/usr/bin/env python3

# Implement this class. Stick to the naming that is introduced in the
# UML diagram. Do not change the class name or the method signatures
# or the automated grading won't work.

class Movie:

    def __init__(self, title, actors, duration):
        if title == "" or actors == [] or duration < 1:
            raise Warning("Title, Actors can't be empty, and duration can't be less than a minute.")
        else:
            self.__title = title
            self.__actors = actors
            self.__duration = duration

    def __repr__(self):
        from json import dumps
        return f'Movie(\"{self.__title}\", {dumps(self.__actors)}, {self.__duration})'

    def __eq__(self, other):
        if not isinstance(other, Movie):
            raise Warning
        if self.__title == other.__title:
            if self.__actors == other.__actors:
                if self.__duration == other.__duration:
                    return True
                return False
            return False
        return False

    def __hash__(self):
        return hash((self.__title, self.__actors, self.__duration))

    def get_title(self):
        return self.__title

    def get_actors(self):
        return self.__actors[:]

    def get_duration(self):
        return self.__duration

    # also implement the required special functions
