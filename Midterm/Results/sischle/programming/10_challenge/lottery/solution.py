#!/usr/bin/env

import random
# this line of code makes it so that calls to random always produce the same
# successive values so that the examples below always produce the same results
random.seed(7)

def lottery(limit, guess, prize):
    match = 0
    numbers = []
    while len(numbers) < len(guess):
        n = random.randint(1, limit)
        if n not in numbers:
            numbers.append(n)
    for number in guess:
        if number in numbers:
            match += 1
    payout = prize
    for n in range(len(numbers) - match):
        payout /= 2
    if match == 0:
        payout = 0
    numbers.sort()
    return numbers, match, payout

    # or if you already know Python:
    #numbers = sorted(random.sample(range(1, limit+1), k=len(guess)))
    #match = len(set(numbers) & set(guess))
    #payout = 0 if not match else prize*(1/2**(len(guess)-match))
    #return numbers, match, payout

# examples
print( lottery(52, [4, 8, 15, 16, 23, 42], 1000000) ) # 2 matching
print( lottery(3, [1, 2, 3], 1000000) )               # inevitable perfect match
print( lottery(10000, [1, 2, 3], 1000000) )           # zero matching

