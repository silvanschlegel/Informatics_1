def compute_stats(lst):
    import statistics
    # write your implementation below
    list = sorted(lst)
    second_highest = list[len(list)-2]
    average = sum(list)/len(list)
    median = 0
    if len(list)%2 != 0:
        median = statistics.median(list)
    else:
        median = statistics.median(list)

    return (second_highest,average,median)

stats = compute_stats([1,12,4,5,8])
assert stats[0] == 8 and stats[1] == 6 and stats[2] == 5