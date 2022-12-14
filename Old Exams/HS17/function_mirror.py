def mirror(s):
    # write your implementation here
    mirrored = s
    for i in range(len(s)-2,-1,-1):
        mirrored +=s[i]

    return mirrored
assert mirror("") == ""
assert mirror("a") == "a"
assert mirror("abc") == "abcba"