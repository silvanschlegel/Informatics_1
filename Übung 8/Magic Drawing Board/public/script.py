#!/usr/bin/env python3

class MagicDrawingBoard:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
        if self.__x > 0 and self.__y > 0:
            if isinstance(self.__x, int) and isinstance(self.__y, int):
                self.__board = [["0" for i in range(self.__x)] for j in range(self.__y)]
            else:
                raise Warning("x and y must be Integers")
        else:
            raise Warning("Board size invalid. x and y coordinates must be bigger than 0")

    def pixel(self, coordinate):
        if not isinstance(coordinate[0], int) or not isinstance(coordinate[1], int):
            raise Warning
        if coordinate[0] in range(self.__x) and coordinate[1] in range(self.__y):
            self.__board[coordinate[1]][coordinate[0]] = "1"
        else:
            raise Warning("At least one input value is either too big or too small.")

    def rect(self, first_coordinate, second_coordinate):
        if not isinstance(first_coordinate[0], int) or not isinstance(first_coordinate[1], int) or not isinstance(
                second_coordinate[0], int) or not isinstance(second_coordinate[1], int):
            raise Warning("coordinates have to be given as an integer")
        if first_coordinate[0] in range(self.__x + 1) and first_coordinate[1] in range(self.__y + 1):
            if second_coordinate[0] in range(self.__x + 1) and second_coordinate[1] in range(self.__y + 1) and \
                    second_coordinate[0] > first_coordinate[0] and second_coordinate[1] > first_coordinate[1]:
                for i in range(first_coordinate[1], second_coordinate[1], 1):
                    for j in range(first_coordinate[0], second_coordinate[0], 1):
                        self.__board[i][j] = "1"
            else:
                raise Warning("Second coordinates are unauthorized")
        else:
            raise Warning("First Coordinates are not in playing field.")

    def reset(self):
        self.__board = [["0"] * self.__x] * self.__y

    def img(self):
        image = ""
        for k, i in enumerate(self.__board):
            for j in i:
                image += j
            if k < len(self.__board)-1:
                image += "\n"

        return image


# You can play around with your implementation in the body of the following 'if'.
# The contained statements will be ignored while evaluating your solution.
if __name__ == '__main__':
    db = MagicDrawingBoard(6, 4)


    db.rect((2, 2), (5,4))
    db.pixel((6,1))
    img = db.img()
    print(img)



