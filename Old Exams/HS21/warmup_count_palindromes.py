def count_palindromes(sentence):
    import re
    counter = 0

    sentence = sentence.split()
    for word in sentence:
        if len(word) >= 3:
            word = ''.join(e for e in word if e.isalpha())
            if word.lower() == word[::-1].lower():
                counter += 1


    return counter



# DO NOT SUBMIT THE LINES BELOW!
assert count_palindromes("Having fun!") == 0
assert count_palindromes("Bob and otto") == 2
assert count_palindromes("Where's Dad?") == 1
assert count_palindromes("Otto is my dad.") == 2
assert count_palindromes("I don't like pop music") == 1