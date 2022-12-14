def words_by_len(sentence):
    if not isinstance(sentence,str):
        raise AssertionError
    return_dic = {}
    sentence = sentence.split()
    for i in sentence:
        if len(i) not in return_dic.keys():
            return_dic[len(i)] = {i}
        else:
            return_dic[len(i)].add(i)

    return return_dic

# DO NOT SUBMIT THE LINES BELOW!
assert words_by_len("how are ya?") == {3: {"how", "are", "ya?"}}
assert words_by_len(" I'm      so so ") == {2: {"so"}, 3: {"I'm"}}
assert words_by_len("Get well soon !!") == {2: {"!!"}, 3: {"Get"}, 4: {"well", "soon"}}
assert words_by_len("") == {}