def lottery(limit, guess, prize):
    n = len(guess)
    corr = 0
    l = guess
    preis = 0
    drawnnrs = []
    for i in range(n):
        j = random.randint(1,limit)
        if j in l:
            l.remove(j)
            corr +=1
            drawnnrs.append(j)
    drawnnrs.sort()
    if corr == n:
        preis = prize

    elif corr+1 == n:
        preis = 0.5*prize

    elif corr +2 ==n:
        preis = 0.25*prize

    return drawnnrs, corr, preis