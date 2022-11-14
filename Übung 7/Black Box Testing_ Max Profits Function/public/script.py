#!/usr/bin/env python3

# You can implement this function, but you do not have to.
# The grading will only depend on your test suite.
#
# This signature is required for the automated grading to work.
# You must not rename the function or change its list of parameters.
def max_profit(prices):
	if not isinstance(prices, list):
		return "Invalid Input Type"

	if len(prices) == 0:
		return "Empty Price List"

	for a in prices:
		if not isinstance(a,int):
			return "Invalid Data Type within List"

		if a < 0:
			return "Invalid Prices"


	values = set()
	max_diff = 0
	for j,i in enumerate(prices):

		values.add(i)

		for k in prices[j:]:
			if k-i > max_diff:
				max_diff = k-i

	if len(list(values)) == 1 or max_diff == 0:
		return 0

	return max_diff

print(max_profit([1,2,3,[4]]))





