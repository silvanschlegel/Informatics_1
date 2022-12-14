def calc(expression):
    a = expression.split()

    if a[0] == "+":
        return float(a[1])+float(a[2])
    if a[0] == "-":
        return float(a[1])-float(a[2])
    if a[0] == "*":
        return float(a[1])*float(a[2])
    if a[0] == "/":
        if a[2] == 0:
            raise ValueError
        return float(a[1])/float(a[2])


# DO NOT SUBMIT THE LINES BELOW!
assert calc("+ 1 2") == 3
assert calc("- 1 2") == -1
assert calc("* 1 2") == 2
assert calc("/ 1 2") == 0.5
assert calc("* 1 -2") == -2
assert calc("* 10.5 2") == 21
assert calc("* -10.5 -2") == 21
