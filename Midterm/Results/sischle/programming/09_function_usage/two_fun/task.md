Implement a function `apply` which takes three parameters: a function `f1`, a function `f2`, and a value `value`. These parameters will always be chosen such that the function `f1` takes one parameter of the same type as `value` and `f2` will take one parameter of whatever type the return value of `f1` will be.

The function `apply` should do the following:

 * Call `f1` with `value` as the parameter, which will result in some return value
 * Call `f2` with the return value of the previous call as the parameter, which will result in another value
 * Return the resulting value

For example, calling `apply(min, chr, [101, 97, 99])` should first call `min` with `[101, 97, 99]` as the parameter, which will result in `97`. Then, `chr` should be called with `97` as the parameter, resulting in `a`, which shall be returned.

You may assume that your function will only be called with parameters that match the given description.
