
def reverse(l):
    if len(l) == 0: return []
    return [l[-1]] + reverse(l[:-1])
assert reverse([]) == []
assert reverse([2]) == [2]
assert reverse([2, 6, 5]) == [5, 6, 2]