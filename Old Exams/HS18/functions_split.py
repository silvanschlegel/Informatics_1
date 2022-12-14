def split(text):
    
    return text.split()

assert split("") == []
assert split("aaa") == ["aaa"]
assert split("a bbb cc") == ["a", "bbb", "cc"]