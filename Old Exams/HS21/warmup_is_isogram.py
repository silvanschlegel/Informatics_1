def is_isogram(sentence):
    if not isinstance(sentence,str):
        raise TypeError
    if sentence == "":
        raise ValueError
    counter = 0
    for i in sentence:
        if i.isalpha():
            counter += 1
    if counter == 0:
        raise ValueError

    sentence = sentence.lower()
    dic = {}
    for i in sentence:
        if i.isalpha():
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1

    test_val = list(dic.values())[0]
    for i in dic:
        if dic[i] != test_val:
            return False
    return True




# DO NOT SUBMIT THE LINES BELOW!
assert is_isogram("uncopyrightable")
assert is_isogram("The big dwarf only jumps.")
assert is_isogram("Apple-ale")
assert (not is_isogram("bass"))
assert (not is_isogram("Tart"))