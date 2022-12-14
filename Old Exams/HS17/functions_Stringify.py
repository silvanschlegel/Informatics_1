def stringify(n):
    # write your implementation here
    if n%2 == 0:
        return f'{n} is even'
    else:
        return f'{n} is odd'
assert stringify(10) == "10 is even"
assert stringify(5) == "5 is odd"