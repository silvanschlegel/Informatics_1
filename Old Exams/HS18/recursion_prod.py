def prod(x, y):
    if x == 0 or y == 0:
        return 0
    while y>0:
        return x+prod(x,y-1)


assert prod(2, 0) == 0
assert prod(5, 2) == 10
assert prod(37,10) == 370