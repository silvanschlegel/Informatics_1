import random
# this line of code makes it so that calls to random always produce the same
# successive values so that the examples below always produce the same results
random.seed(7)
def lottery(limit, guess, prize):
    n = len(guess)
    corr = 0
    l = guess
    preis = 0
    drawnnrs = []
    for i in range(n):
        j = random.randint(1,limit)
        drawnnrs.append(j)

        if j in l:
            l.remove(j)
            corr +=1
    drawnnrs.sort()
    if corr == n:
        preis = prize

    elif corr+1 == n:
        preis = 0.5*prize

    elif corr +2 ==n:
        preis = 0.25*prize

    return drawnnrs, corr, preis



print( lottery(52, [4, 8, 15, 16, 23, 42], 1000000) ) # 2 matching
print( lottery(3, [1, 2, 3], 1000000) )               # inevitable perfect match
print( lottery(10000, [1, 2, 3], 1000000) )           # zero matching
