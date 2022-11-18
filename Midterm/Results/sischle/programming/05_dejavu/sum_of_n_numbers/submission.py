def sum_divisibles(limit, divisor):
    sum = 0
    for i in range(limit+1):
        if i%divisor == 0:
            sum += i

    return sum