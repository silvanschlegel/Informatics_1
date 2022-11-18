You have been tasked with programming a simulator for number lotteries.

Implement a function `lottery` according to these implementation instructions:

 * `lottery` takes three parameters:
     * an integer `limit` specifying the largest number that can be drawn in this lottery
     * a list `guess` of *n* unique integer numbers between 1 and (including) `limit`; this is the guess provided by the player. *n* will always be larger than 0
     * a number `prize` indicating the maximum amount that can be won in the lottery

 * `lottery` shall then perform the following procedure:
     * draw *n* unique random numbers in the range from (and including) 1 to (and including) *limit*. *n* is implied by the length of the guess provided by the player.
     * check how many numbers in `guess` appear in the random draw
     * calculate the payout according to the following rule: For an exact match, the whole prize is paid out. If one number differs, half of the prize is paid out. If two numbers differ, a quarter of the prize is paid out, and so on. If none of the numbers match, the prize money is `0`.

 * In the end `lottery` should return three values: the randomly generated numbers in ascending order, the number of matches, and the payout.

**Note**: Make sure you return the correct number of return values. Partial points are awarded even if not all return values are correct, but only if all three values are present.

You may assume that your function will only be called with parameters that match the given description.
