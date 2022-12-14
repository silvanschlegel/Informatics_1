

#Validate for all values of up to 100$ that the change amount is correct.
assert change(2) == 0
assert change(1) == 0
assert change(0) == 0
assert change(100) == 100
assert change(38) == 38
assert change(5) == 5
assert change(7) == 7

#Test meaningful corner cases to make sure that the selection of coins is correct.
assert change(10) == amount((1))
assert change(100) == amount((10))
assert change(38) == amount((3,1,1,1))
assert change(5) == amount((0,1))
assert change(2) == amount((0,0,1,0))