def intersperse(s, l):
    res = ""
    for j, i in enumerate(s):
        res += s[j]
        if j == len(s)-1:
            continue
        res += l[j % len(l)]
    return res


# DO NOT SUBMIT THE LINES BELOW!
assert intersperse("H", [',']) == "H"
assert intersperse("Hello", [',']) == "H,e,l,l,o"
assert intersperse("Hello", [',', '.']) == "H,e.l,l.o"
assert intersperse("Hello", ['', '.']) == "He.ll.o"
assert intersperse("Hello", ['-o-', '_o_']) == "H-o-e_o_l-o-l_o_o"
assert intersperse("Hello", [',', '.', '-']) == "H,e.l-l,o"
