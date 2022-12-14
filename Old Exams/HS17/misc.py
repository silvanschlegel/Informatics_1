

def e():
    for i in {"a":1, "b":2, "c":3 }:
        return i


print(e())
print(type(e()))
f = ((1), (2,3))
a = f[0]
print(type(a))
print(a)

class g(object): x = 1.2
def __init__(self): self.x = 3
print(type(g.x))
print(g.x)