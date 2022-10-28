#!/usr/bin/env python3

# You can freely adopt this number to print pyramids of different sizes
h = 2


# build a string 
def build_string_pyramid():

    # You need to change the functionality of this function to
    # create the correct 'encoded' string which will be returned
    # at the end of the function.
    s = ""
    height = h

    for i in range(height):     #first half of pyramid
        for j in range(i+1):
            if j+1 > 1 and j<height:
                s += "*"
            s+=str(j+1)
        s += "\n"

    for k in range(height-1,-1,-1):     #second half of pyramid
        for l in range(k):
            if l + 1 > 1 and l < height:
                s += "*"
            s += str(l + 1)
        if k>0:
            s += "\n"
    # You don't need to change the following line.
    # It simply returns the string created above.
    return s

# The following line calls the function and prints the return
# value to the Console. This way you can check what it does.
# See the console output and compare it to the image in the task description
print(build_string_pyramid())



