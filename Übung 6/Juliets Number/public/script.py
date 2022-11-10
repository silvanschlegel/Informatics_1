#!/usr/bin/env python3

# use this list of presumably known Whatsapp numbers to check
# whether a trial nr from the function below exists in Whatsapp.
# Note that the grading framework might use different numbers here.
wa_nrs = ["0781111119", "0792653913", "0797763139", "0792793193", "0781139022", "0764320165"]


# This signature is required for the automated grading to work. 
# Do not rename the function or change its list of parameters.
def get_possible_nrs(n):
    # This function accepts a string n for juliets number where one digit is missing.
    # and should return a list of all whatsapp numbers that might belong to juliet 
    possible_nrs_for_juliet = []
    nr_string = str(n)
    all_nrs = set()
    for i in range(2,9,1):
        for j in range(10):
            if i == 8:
                poss_nr = nr_string + str(j)
            else:
                poss_nr = nr_string[:i] + str(j) + nr_string[i:]

            all_nrs.add(poss_nr)

    list(all_nrs)
    for k in wa_nrs:
        for l in all_nrs:
            if l == k:
                possible_nrs_for_juliet.append(l)

    return possible_nrs_for_juliet

# For this particular number, the function should find the
# last element in wa_nrs
print(get_possible_nrs("076432165"))