def where_is_waldo(names):
    for i,j in enumerate(names):
        if j == "Waldo":
            return i
    return None

print( where_is_waldo(["Peter", "Waldo", "John"]) )
print( where_is_waldo(["Peter", "Willy", "John"]) )