def remove_every(l, n):
    li = l
    for i in range(len(l)):
        if i%n == 0:
            del l[i]

    return l
print(remove_every([1, 2, 3, 4, 5], 2))
