def apply(f1, f2, value):
    f1(value)
    return f2(f1(value))