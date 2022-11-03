#!/usr/bin/env python3

# This signature is required for the automated grading to work. 
# Do not rename the function or change its list of parameters.
def compress(data):
    keys_list = []
    ordered_values = []

    # if data is an empty list
    if len(data) == 0:
        return tuple(keys_list), ordered_values

    for i in data:
        # if dictionary in data is empty
        if len(i) == 0:
            return tuple(keys_list), [()]
        for j in i:
            # add keys to keys_list
            if j not in keys_list:
                keys_list.append(j)

                # sort keys
                keys_list.sort()

        # add values of dict to list of values
        tp = []
        for k in i:
            tp.append(i[k])

        # sort values according to sorting of keys
        for a,l in enumerate(tp):
            for key, value in i.items():
                if l == value:
                    found = key
            temp = tp[keys_list.index(found)]
            tp[keys_list.index(found)] = l
            tp[a] = temp
        tp_sorted = tuple(tp)

        ordered_values.append(tp_sorted)
    # create return tuple with keys_list and ordered_values
    return tuple(keys_list), ordered_values

# The following line calls the function and prints the return
# value to the Console. This way you can check what it does.
# However, we encourage you to write tests, because then you
# can easily test many different values on every "Test & Run"!
data = [
    {"a": 1, "b": 2, "c": 3},
    {"a": 4, "c": 6, "b": 5}
]
print(compress(data))
