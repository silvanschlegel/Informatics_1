def count(l):

    if len(l) == 0:
        return 0
    if type(l[0]) == list:
        return count(l[0])+count(l[1:])
    return 1+count(l[1:])





# DO NOT SUBMIT THE LINES BELOW!
assert count([]) == 0
assert count([[],[]]) == 0
assert count([1, "", [{}], [[True], 4]]) == 5