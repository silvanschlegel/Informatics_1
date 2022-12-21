#-- THIS LINE SHOULD BE THE FIRST LINE OF YOUR SUBMISSION! --#

def are_anagrams(a, b):
    first = []
    second = []
    for i in a:
        if i.isalnum():
            first.append(i.lower())
    for j in b:
        if j.isalnum():
            second.append(j.lower())
    if len(first) != len(second):
        return False
    for i in first:
        try:
            second.remove(i)
        except:
            return False
    if len(second) == 0:
        return True


#-- THIS LINE SHOULD BE THE LAST LINE OF YOUR SUBMISSION! ---#

### DO NOT SUBMIT THE FOLLOWING LINES!!! THESE ARE FOR LOCAL TESTING ONLY!
assert(are_anagrams('Dog', 'ddd'))
assert(are_anagrams("The Meaning of Life.", "The fine game of nil!"))
assert(not are_anagrams("The Meaning of Life", "Work"))