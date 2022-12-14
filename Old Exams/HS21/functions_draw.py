def draw(size, instructions):
    board = []
    for i in range(size):
        board.append([" " for i in range(size)])

    for tuple in instructions:
        if tuple[0] < 0 or tuple[0] > size-1 or tuple[1] < 0 or tuple[1] > size-1:
            raise IndexError
        if len(tuple[2]) != 1:
            raise ValueError

        board[tuple[1]][tuple[0]] = tuple[2]
    res = ""
    for i in range(size):
        for j in range(size):
            res += board[i][j]
        if i < size-1:
            res += "\n"

    return res

print(draw(5, [
  (0, 0, "a"),
  (1, 2, "a"),
  (4, 4, "b"),
  (0, 4, "a"),
  (1, 1, "a"),
  (0, 3, "a")]))

#print(draw(10, (3,3,1)))
# DO NOT SUBMIT THE LINES BELOW!
assert draw(1, [(0, 0, "a")]) == "a"
assert draw(2, [(0, 0, "a"), (1, 1, "b")]) == (
     "a \n"
     " b"
)
assert draw(3, [(1, 0, "a"), (0, 1, "b")]) == (
     " a \n"
     "b  \n"
     "   "
)

assert draw(5, [
  (0, 0, "a"),
  (1, 2, "a"),
  (4, 4, "b"),
  (0, 4, "a"),
  (1, 1, "a"),
  (0, 3, "a")]) == (
    "a    \n"
    " a   \n"
    " a   \n"
    "a    \n"
    "a   b"
)
