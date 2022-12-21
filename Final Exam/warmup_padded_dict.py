def padded_dict(keys, values, padding = None):

    res = {}


    for i in range(len(keys)):
        if len(keys) <= len(values):
            res[keys[i]] = values[i]
        else:
            res[keys[i]] = padding

    return res

