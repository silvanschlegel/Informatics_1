#!/usr/bin/env python3

# The signatures of this class and its public methods are required for the automated grading to work. 
# You must not change the names or the list of parameters.
# You may introduce private/protected utility methods though.
class Publication:

    def __init__(self, authors, title, year):
        self.__authors = authors
        self.__title = title
        self.__year = year

    # To implement the required functionality, you will also have to implement several
    # of the special functions that typically include a double underscore.
    # implement get_authors
    def get_authors(self):
        temp = self.__authors[:]
        return temp

    # implement get_title
    def get_title(self):
        return self.__title

    # implement get_year
    def get_year(self):
        return self.__year

    # implement __repr__
    def __repr__(self):
        from json import dumps
        return f"Publication({dumps(self.__authors)}, \"{self.__title}\", {self.__year})"

    # implement __str__
    def __str__(self):
        from json import dumps
        return f"Publication({dumps(self.__authors)}, \"{self.__title}\", {self.__year})"

    # implement __eq__
    def __eq__(self, other):
        if isinstance(other, Publication):
            if self.__authors == other.__authors:
                if self.__title == other.__title:
                    if self.__year == other.__year:
                        return True
                    return False
                return False
            return False
        return NotImplemented

    # implement __hash__
    def __hash__(self):
        return hash((tuple(self.__authors), self.__title, self.__year))

    # implement __lt__
    def __lt__(self, other):
        if not isinstance(other, Publication):
            return NotImplemented
        # check names
        if len(self.__authors) < len(other.__authors):
            return True
        if len(self.__authors) > len(other.__authors):
            return False
        #gleich viele namen
        for i, j in enumerate(self.__authors):
            if self.__authors[i] < other.__authors[i]:
                return True

        # check title
        if self.__title < other.__title:
            return True

        # check year
        if self.__year < other.__year:
            return True

        return False

    # implement __le__
    def __le__(self, other):
        if not isinstance(other, Publication):
            return NotImplemented
        # check names
        if not len(self.__authors) <= len(other.__authors):
            return False

        for i, j in enumerate(self.__authors):
            if not self.__authors[i] <= other.__authors[i]:
                return False
        # check title
        if not self.__title <= other.__title:
            return False

        # check year
        if not self.__year <= other.__year:
            return False

        return True

    # implement __gt__
    def __gt__(self, other):
        if not isinstance(other, Publication):
            return NotImplemented
        # check names
        if len(self.__authors) > len(other.__authors):
            return True
        if len(self.__authors) < len(other.__authors):
            return False
        for i, j in enumerate(other.__authors):
            if self.__authors[i] > other.__authors[i]:
                return True

        # check title
        if self.__title > other.__title:
            return True

        # check year
        if self.__year > other.__year:
            return True

        return False

    # implement __ge__
    def __ge__(self, other):
        if not isinstance(other, Publication):
            return NotImplemented
        # check names
        if not len(self.__authors) >= len(other.__authors):
            return False
        for i, j in enumerate(other.__authors):
            if not self.__authors[i] >= other.__authors[i]:
                return False
        # check title
        if not self.__title >= other.__title:
            return False

        # check year
        if not self.__year >= other.__year:
            return False

        return True

    def __ne__(self, other):
        if not isinstance(other, Publication):
            return NotImplemented
        if self.__authors == other.__authors:
            if self.__title == other.__title:
                if self.__year == other.__year:
                    return False
                return True
            return True
        return True


# You can play around with your implementation in the body of the following 'if'.
# The contained statements will be ignored while evaluating your solution.
if __name__ == '__main__':
    references = [
        Publication(["Gamma", "Helm", "Johnson", "Vlissides"], "Design Patterns", 1994),
        Publication(["Cockburn"], "Writing Effective Use Cases", 2000),
        Publication(["Duvall", "Matyas", "Glover"], "Continuous Integration", 2007)
    ]

    p = Publication(["Duvall", "Matyas", "Glover"], "Continuous Integration", 2007)
    s = "Publication([\"Duvall\", \"Matyas\", \"Glover\"], \"Continuous Integration\", 2007)"
    print(p)
    print(str(p) == s)

    p1 = Publication(["Schlegel", "Waltenspuel"], "Wurmhoehle 17", 2022)
    p2 = Publication(["Schlegel"], "Wurmhoehle 17", 2022)
    p3 = Publication(["B"], "C", 2345)
    print(p1 >= p2)  # True
    #print(p2 == p3)  # False
    #print(p1 < p2)
    print(p.get_authors())

    sales = {
        p1: 273,
        p3: 398,
    }

    for values in sales.values():
        print(values)
    for key in sales.keys():
        print(key)

    a = [1,2,3,4]
    b = a[:]
    b[1] = "mutable"
    print(a)
    print(b)
    print("aaaaa">"aaaaa")
