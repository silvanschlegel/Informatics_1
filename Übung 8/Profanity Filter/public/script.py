#!/usr/bin/env python3

# The signatures of this class and its public methods are required for the automated grading to work. 
# You must not change the names or the list of parameters. 
# You may introduce private/protected utility methods though.
class ProfanityFilter:

    def __init__(self, keywords, template):
        self.__keywords = keywords
        self.__template = template

    def filter(self, msg):
        if not isinstance(msg, str):
            raise Warning("Input must be string")

        if msg == "":
            return ""

        word_list = msg.split()
        for k, i in enumerate(word_list):
            for j in reversed(sorted(self.__keywords, key=len)):
                if j.lower() in i.lower():
                    word_list[k] = self.__clean(i.lower())
        return ' '.join(word_list)

    def __clean(self, word):
        cleaned = ""
        j = 0
        for i in reversed(sorted(self.__keywords, key=len)):
            if i.lower() in word:
                for j in range(len(i)):
                    cleaned += self.__template[j % (len(self.__template))]
                    j += 1
                word = word.replace(i.lower(), cleaned)
                cleaned = ""
        return word


# You can play around with your implementation in the body of the following 'if'.
# The contained statements will be ignored while evaluating your solution.
if __name__ == '__main__':
    f = ProfanityFilter(["duck", "shot", "batch", "mastard"], "?#$")
    offensive_msg = "abc defghi Mastardsilvanduck jklmno"
    clean_msg = f.filter(offensive_msg)
    print(clean_msg)  # abc defghi ?#$?#$? jklmno
