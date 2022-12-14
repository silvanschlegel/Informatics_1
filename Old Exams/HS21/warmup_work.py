def work(hours, days, teen = False):
    import math
    work_per_day = round(hours/days,2)
    vac_days = 0
    if teen:
        a = 25/42
        vac_days = math.ceil(a*hours)
    else:
        a = 20/42
        vac_days = math.ceil(a*hours)

    return {"per_day": work_per_day, "vacation_days": vac_days}



# DO NOT SUBMIT THE LINES BELOW!
assert work(42, 5) == {"per_day": 8.4, "vacation_days": 20}
assert work(42, 5, True) == {"per_day": 8.4, "vacation_days": 25}
assert work(34, 5) == {"per_day": 6.8, "vacation_days": 17}
assert work(16.55, 4, True) == {"per_day": 4.14, "vacation_days": 10}