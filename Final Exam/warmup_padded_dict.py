def padded_dict(keys, values, padding = None):

    res = {}


    for i in range(len(keys)):
        if len(keys) <= len(values):
            res[keys[i]] = values[i]
        else:
            res[keys[i]] = padding

    return res


print( padded_dict([1, "b", 3], [55, 66, 77] ) )
print( padded_dict([1, "b", 3], [55] ) )
print( padded_dict([1, "b"], [55, 66, 77] ) )

