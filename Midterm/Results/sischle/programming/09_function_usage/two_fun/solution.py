#!/usr/bin/env

def apply(f1, f2, value):
    return f2(f1(value))

# examples
print( apply(min, chr, [101, 97, 99]) )
print( apply(max, lambda x: x*2, [2, 50, 3]) )
print( apply(sorted, lambda s: s[0].upper(), "what") )
