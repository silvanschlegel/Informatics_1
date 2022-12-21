# -- THIS LINE SHOULD BE THE FIRST LINE OF YOUR SUBMISSION! --#

def censor(text, censored_words):
    words = text.split()
    res = []
    # complete the function implementation here
    for i in words:
        j = ''.join([i for i in i if i.isalpha()])
        if j.lower() in censored_words:
            a = ""
            for k in i:
                if k.isalpha():
                    a += "#"
                else:
                    a += k
            res.append(a)
        else:
            res.append(i)


    return " ".join(res)


# -- THIS LINE SHOULD BE THE LAST LINE OF YOUR SUBMISSION! ---#

### DO NOT SUBMIT THE FOLLOWING LINES!!! THESE ARE FOR LOCAL TESTING ONLY!
assert (censor("Hello, World!", ["hello"])
        == "#####, World!")
assert (censor("Everything is going to be fine!", ["everything", "fine"])
        == "########## is going to be ####!")
assert (censor("", ["does", "not", "matter"])
        == "")
assert (censor("Everything is going to be fine!", [])
        == "Everything is going to be fine!")