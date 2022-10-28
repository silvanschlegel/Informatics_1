#!/usr/bin/env python3
import re
# This signature is required for the automated grading to work. 
# Do not rename the function or change its list of parameters.
def analyze(posts):
    hashtags = {}
    for i in posts:
        words = re.split(r'[`!@$%^&*()_+\-=\[\]{};\':"\\|,.<>\/?~ ]', i)
        for j in words:
            while j.startswith("#"):
                if j.startswith("#"):
                    j = j[1:]
                    if not len(j) == 0:
                        if not j[0].isdigit():
                            if j.isalnum():
                                if j in hashtags.keys():
                                    hashtags[j] += 1
                                else:
                                    hashtags[j] = 1

    return hashtags


# The following line calls the function and prints the return
# value to the Console. This way you can check what it does.
# However, we encourage you to write tests, because then you
# can easily test many different values on every "Test & Run"!
posts = [
    "hi #weekend",
    "good morning #zurich #limmat .#c. ...:#dasistok.dasnichtmehr",
    "spend my #weekend in #zurich",
    "#zurich <3 #1hallo #hallo ##aa #a#a"]
print(analyze(posts))
