#!/usr/bin/env

def remove_every(l, n):
    res = []
    for i, item in enumerate(l):
        if (i+1) % n == 0:
            continue
        res.append(item)
    return res

# examples
print( remove_every([1, 2, 3, 4, 5], 2) )
print( remove_every([1, 2, 3, 4, 5, 4, 3, 2, 1], 3) )
