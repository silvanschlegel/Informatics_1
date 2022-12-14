def gregorian_to_ifc(day, month, leap=False):
    import math
    if day == 30 and month == 12 and leap:
        return "Year Day"
    if day == 31 and month == 12:
        return "Year Day"

    days_per_month_normal = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days_per_month_leap = [31, 28, 31, 30, 31, 20, 31, 31, 30, 31, 30, 31]
    if not leap:
        days_passed = sum(days_per_month_normal[:month-1])
        days_passed += day
        if days_passed > 28:
            #days_in_ifc = days_passed % 28
            month_in_ifc = math.ceil(days_passed/28)
            days_in_ifc =days_passed-(month_in_ifc-1)*28
            if days_in_ifc == 0:
                days_in_ifc = 1
            return days_in_ifc,month_in_ifc
        return day,1
    else:
        days_passed = sum(days_per_month_leap[:month - 1])
        days_passed += day
        if days_passed > 28:
            days_in_ifc = days_passed % 28
            month_in_ifc = int(((days_passed - days_in_ifc) / 28) + 1)
            return days_in_ifc, month_in_ifc
        return day, 1


# DO NOT SUBMIT THE LINES BELOW!
assert gregorian_to_ifc(1, 1) == (1, 1)
assert gregorian_to_ifc(28, 1) == (28, 1)
assert gregorian_to_ifc(29, 1) == (1, 2)         #29th Jan Gregorian is 1st Feb IFC
assert gregorian_to_ifc(1, 3) == (4, 3)          #1st  Mar Gregorian is 4rd Mar IFC
assert gregorian_to_ifc(29, 2, True) == (4, 3)   #leap year
assert gregorian_to_ifc(1, 8) == (17, 8)
assert gregorian_to_ifc(15, 11) == (11, 12)
assert gregorian_to_ifc(30, 12) == (28, 13)
assert gregorian_to_ifc(30, 12, True) == "Year Day"
assert gregorian_to_ifc(31, 12) == "Year Day"
