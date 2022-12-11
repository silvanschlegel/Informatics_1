#!/usr/bin/python3

from data import words

def words_with_length(length):
    '''this one just serves as an example'''
    return [word for word in words if len(word) == length]

def words_containing_string(s):
    return [word for word in words if s in word]

def words_starting_with_character(c):
    return [word for word in words if word.startswith(c)]

def alphabet():
    '''you don't have to solve this one using a comprehension.'''
    import string
    return string.ascii_lowercase

def dictionary():
    return {k: words_starting_with_character(k) for k in alphabet()}

def censored_words(s):
    return [ "x"*len(word) if s in word else word for word in words ]

print(alphabet())
print(dictionary()["y"])
print(censored_words("abc"))