"""
####  Find the Mean of All Digits  ####

Create a function that returns the mean of all digits.


[Examples]

___
mean(42) ➞ 3

mean(12345) ➞ 3

mean(666) ➞ 6
_____



[Notes]

___
*) The mean of all digits is the sum of digits / how many digits there are (e.g. mean of digits in 512 is (5+1+2)/3(number of digits) = 8/3=2).
*) The mean will always be an integer.
___



[algorithms] [logic] [loops] [math] 

"""
import numpy as np
def mean(a):
    lst = [int(x) for x in str(a)]
    return np.mean(lst)
print(mean(12345))