#!/usr/bin/env

def check(speed, limit):
    if limit == 0:
        return True
    if speed > limit:
        return False
    return True

# examples
print( check(130, 90) )
print( check(170, 0) )
