#!/usr/bin/env python3

def evolve(world, steps):

    # check if steps are ok
    if not isinstance(steps, int):
        raise Warning(f"Steps must be positive and of type Integer. You chose: {steps} ")

    if steps <= 0:
        raise Warning(f"Steps must be positive and of type Integer. You chose: {steps} ")

    # check if world is of correct type
    if not isinstance(world, tuple):
        raise Warning("World must be in the form of a tuple. ")

    if len(world) == 0:
        raise Warning("World can't be empty")

    for i in world:
        # check types of objects in tuple
        if not isinstance(i, str):
            raise Warning(
                f"Your tuple world doesn't contain only strings as values. At least one line is of type: {type(i)}")

    # check for invalid characters again
    valid_chars = ['#', '-', '|', ' ']
    for i in world:
        for j in i:
            if not j in valid_chars:
                raise Warning("Fails because world has false character in it")

    # check height and width
    height = len(world)
    width = len(world[0])
    if height <= 2:
        raise Warning("World's height is too small")
    if width <= 2:
        raise Warning("World's width is too small")

    # check if lines have the same length
    for j, i in enumerate(world):
        if len(i) != width:
            raise Warning(
                f"Lines of world don't have the same width. The width of the first line is {width} and the width of the {j}th line is {len(i)}.")

    # check if characters are right and if layout is correct
    # 1. check first and last line
    if not world[0] == width * "-" or not world[height - 1] == width * "-":
        raise Warning("Fails because frame is not right.")
    # 2. check middle lines
    for i in range(1, height - 2):
        if not world[i][0] == "|" or not world[i][width - 1] == "|":
            raise Warning("Fails because frame is not right.")

        for l in range(1, width - 2):
            if not world[i][l] == " " and not world[i][l] == "#":
                raise Warning(f"Fails because world has false character in it: {world[i][l]} ")

    # implement the game
    world = list(world)
    temp_world = world[:]

    for i in range(steps):

        for j in range(1, height - 2):
            for k in range(1, width - 2):
                if check(world[j][k], world, j, k) == 1:
                    a = list(temp_world[j])
                    a[k] = "#"
                    temp_world[j] = listToString(a)

                else:
                    a = list(temp_world[j])
                    a[k] = " "
                    temp_world[j] = listToString(a)

        world = temp_world[:]
    final_world = tuple(world)

    counter = 0
    for i in world:
        for j in i:
            if j == "#":
                counter += 1

    return final_world, counter


def check(i, world, reihe, index):
    counter = 0
    for m, n in enumerate(world):
        world[m] = list(world[m])
    # check how many # there are
    if world[reihe][index - 1] == "#":
        counter += 1
    if world[reihe][index + 1] == "#":
        counter += 1
    if world[reihe + 1][index] == "#":
        counter += 1
    if world[reihe - 1][index] == "#":
        counter += 1
    if world[reihe + 1][index + 1] == "#":
        counter += 1
    if world[reihe + 1][index - 1] == "#":
        counter += 1
    if world[reihe - 1][index + 1] == "#":
        counter += 1
    if world[reihe - 1][index - 1] == "#":
        counter += 1

    if i == "#" and (counter <= 1 or counter >= 4):
        return 0

    if i == "#" and counter >= 2 and counter <= 3:
        return 1

    if i == " " and counter == 3:
        return 1

    return 0


def listToString(s):
    # initialize an empty string
    str1 = ""

    # traverse in the string
    for ele in s:
        str1 += ele

    # return string
    return str1


field = (
    "--------------",
    "|            |",
    "|   ###      |",
    "|   #        |",
    "|    #       |",
    "|            |",
    "--------------"
)
steps = 4

result, alive_cells = evolve(field, steps)

print(f"Game of Life after {steps} moves:")
for row in result:
    print(row)
print(f"{alive_cells} are alive.")
