def check(speed, limit):
    if limit == 0:
        return True
    if speed > limit:
        return False
    else:
        return True


print( check(170, 0) )