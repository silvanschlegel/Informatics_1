#!/usr/bin/env python3

# Implement this function
#
# This signature is required for the automated grading to work.
# You must not rename the function or change its list of parameters.
def convert_roman_to_int(roman):
    roman_single_digits = {
        # simple cases
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    roman_double_digits = {
        # compound cases
        "IV": 4,
        "IX": 9,
        "XL": 40,
        "XC": 90,
        "CD": 400,
        "CM": 900,
    }
    roman_allowed_tuples = {
        # allowed combinations between numbers
        "XI": 11,
        "VI": 6,
        "II": 2,
        "XV": 15,
        "XX": 20,
        "LI": 51,
        "LV": 55,
        "LX": 60,
        "CI": 101,
        "CV": 105,
        "CX": 110,
        "CL": 150,
        "CC": 200,
        "DI": 501,
        "DV": 505,
        "DX": 510,
        "DL": 550,
        "DC": 600,
        "MI": 1001,
        "MV": 1005,
        "MX": 1010,
        "ML": 1050,
        "MC": 1100,
        "MD": 1500,
        "MM": 2000
    }
    roman_unallowed = ["IIMX", "IVII", "IVIV", "IXIX", "VIIII", "VV", "DD", "LL", "LLX", "VIV", "XXXX", "IIII", "DCCCC",
                       "IVI", "IXI", "ILI", "ICI", "IDI", "IMI", "XLX", "XCX", "XDX", "XMX", "LDL", "LML", "CDC", "CMC",
                       "IL", "IC", "ID", "IM", "VX", "VL", "VC", "VD", "VM", "LC", "LD", "LM", "DM", "IVX", "IVL",
                       "IVC", "IVD", "IVM", "IXL", "IXL", "IXC", "IXD", "IXM", "XLC", "XLD", "XLM", "CDM"]
    num = 0
    for k in roman_unallowed:
        if k in roman:
            raise Warning("Invalid Input")
    i = 0
    temp = 0
    if i + 1 <= (len(roman) - 1):
        if roman[i] + roman[i + 1] in roman_double_digits.keys():
            temp = roman_double_digits[roman[i]+roman[i+1]]+1
        else:
            temp = roman_single_digits[roman[i]]+1
    else:
        temp = roman_single_digits[roman[i]]+1

    while i< len(roman):
        if i+1 <= (len(roman)-1):
            if roman[i]+roman[i+1] in roman_double_digits.keys() and roman_double_digits[roman[i]+roman[i+1]] < temp:
                num += roman_double_digits[roman[i]+roman[i+1]]
                temp = roman_double_digits[roman[i]+roman[i+1]]
                if i+1 < (len(roman)-1):
                    if roman[i+1]+roman[i+2] in roman_allowed_tuples.keys():
                        i += 2
                    else:
                        raise Warning("Invalid Input")
                else:
                    i+=2

            elif roman[i] in roman_single_digits.keys() and roman_single_digits[roman[i]] <= temp:
                num += roman_single_digits[roman[i]]
                temp = roman_single_digits[roman[i]]
                if i < len(roman)-1:
                    if roman[i] + roman[i+1] in roman_allowed_tuples.keys():
                        i += 1
                    else:
                        raise Warning("Invalid Input")

            else:
                raise Warning("Invalid Input")

        else:
            if roman[i] in roman_single_digits.keys() and roman_single_digits[roman[i]] <= temp:
                num += roman_single_digits[roman[i]]
                temp = roman_single_digits[roman[i]]
                if i < len(roman):
                    i += 1
            else:
                raise Warning("Invalid Input")

    return num



# The following lines calls the function and prints the return
# value to the Console.
i = convert_roman_to_int("XX")
print(i)
