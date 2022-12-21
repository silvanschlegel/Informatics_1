lst = [1,1,1,1,1,1,1,1,1,1]
def sum_lst(lst):
    if len(lst) == 1:
        return lst[0]
    return lst[0]+sum_lst(lst[1:])



print(sum_lst(lst))

