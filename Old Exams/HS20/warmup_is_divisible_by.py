#-- THIS LINE SHOULD BE THE FIRST LINE OF YOUR SUBMISSION! --#

def is_divisible_by(n, numbers):
    if numbers == "":
        raise ValueError
    for i in numbers:
        if i == 0:
            raise ValueError
        if n%i != 0:
            return False

    return True


#-- THIS LINE SHOULD BE THE LAST LINE OF YOUR SUBMISSION! ---#

### DO NOT SUBMIT THE FOLLOWING LINES!!! THESE ARE FOR LOCAL TESTING ONLY!
assert(is_divisible_by(30, [3, 6, 15]))
assert(not is_divisible_by(30, [3, 6, 29]))
try:
    is_divisible_by(30, [0, 6, 29])
    assert(False) # expected an exception!
except ValueError:
    pass # the correct exception was thrown