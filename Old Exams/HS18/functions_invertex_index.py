def rev_idx(words):
    return_dic = {}
    for index,word in enumerate(words):
        if word.lower() not in return_dic.keys():
            return_dic[word.lower()] = [index]
        else:
            return_dic[word.lower()].append(index)

    return return_dic
assert rev_idx([]) == {}
assert rev_idx(["a","b"]) == {"a": [0], "b": [1]}
assert rev_idx(["a","B","A","aa"]) == {"a": [0, 2], "aa": [3], "b": [1]}
