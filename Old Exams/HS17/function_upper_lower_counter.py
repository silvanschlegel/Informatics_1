
def count_letters(s):
    # write your implementation here
    dic = {"lower": 0,"upper":0}
    for i in s:
        if i.islower():
            dic["lower"] += 1
        if i.isupper():
            dic["upper"] += 1

    return dic
d = count_letters("Abc Defg HiJ!")
assert d["upper"] == 4 and d["lower"] == 6
