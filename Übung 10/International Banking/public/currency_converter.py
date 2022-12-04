#!/usr/bin/env python3
# add imports, if necessary
from exchange_rates import EXCHANGE_RATES

def convert(amount, from_currency, to_currency):
    if not isinstance(amount, int) and not isinstance(amount,float):
        raise Warning("Amount must be number")
    if not isinstance(from_currency, str) or not isinstance(to_currency, str):
        raise Warning("currencies have at least one invalid input!")
    if from_currency not in EXCHANGE_RATES.keys() or from_currency == "":
        raise Warning("Source currency is not in Exchange rates dict!")
    if to_currency not in EXCHANGE_RATES.keys():
        raise Warning("Destination currency not in Exchange rates dict!")
    if from_currency in EXCHANGE_RATES.keys() and to_currency in EXCHANGE_RATES[from_currency]:
        return amount * EXCHANGE_RATES[from_currency][to_currency]
    if to_currency in EXCHANGE_RATES.keys() and from_currency in EXCHANGE_RATES[to_currency]:
        return amount * 1/EXCHANGE_RATES[to_currency][from_currency]
