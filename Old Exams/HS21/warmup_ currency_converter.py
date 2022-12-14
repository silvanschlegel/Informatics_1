def currency_converter(src, dst, rate):
    return lambda n: f'{n} {src} is {round(n*rate,2)} {dst}'

    '''def converter(amount):
        a = round(amount*rate,2)

        return f'{amount} {src} is {a} {dst}'
    return converter
'''


# DO NOT SUBMIT THE LINES BELOW!
assert currency_converter("EUR", "CHF", 1.1)(5) == "5 EUR is 5.5 CHF"
chf_to_jpy = currency_converter("CHF", "JPY", 123)
assert chf_to_jpy(1) == "1 CHF is 123 JPY"
assert chf_to_jpy(2) == "2 CHF is 246 JPY"
assert currency_converter("Peanuts", "Pinecones", 0.2)(50) == "50 Peanuts is 10.0 Pinecones"
assert currency_converter("Blemflarcks", "Coins", 0.0021)(333.3) == "333.3 Blemflarcks is 0.7 Coins"
