def scale_up(factor, image):
    image_lst = image.split("\n")
    scaled_up = []
    for i in image_lst:
        temp_list = []
        for j in i:
            for k in range(factor):
                temp_list.append(j)
        for m in range(factor):
            scaled_up.append(temp_list)
    res = ""
    for i in range(len(scaled_up)):
        for k in scaled_up[i]:
            res+= k
        if i < len(scaled_up)-1:
            res += "\n"
    return res



def scale_down(factor, image):
    image_lst = image.split("\n")
    scaled_down = []
    for i,j in enumerate(image_lst):
        if i%factor == 0:
            temp = ""
            for k,ele in enumerate(j):
                if k%factor == 0:
                    temp += ele
            scaled_down.append(temp)
    res = ""
    for j,i in enumerate(scaled_down):
        res += i
        if j < len(scaled_down) - 1:
            res += "\n"
    return res



# DO NOT SUBMIT THE LINES BELOW!
img1 = ("xxx\n"
        "x x\n"
        "xxx")

img2 = ("xxxxxx\n"
        "xxxxxx\n"
        "xx  xx\n"
        "xx  xx\n"
        "xxxxxx\n"
        "xxxxxx")

assert scale_up(2, img1) == img2
assert scale_down(2, img2) == img1
#
img3 = ("123\n"
        "345")

img4 = ("111222333\n"
        "111222333\n"
        "111222333\n"
        "333444555\n"
        "333444555\n"
        "333444555")

assert scale_up(3, img3) == img4
assert scale_down(3, img4) == img3

img5 = ("12345\n"
        "abcde\n"
        "ABCDE")

img6 = ("14")

assert scale_down(3, img5) == img6