"""
####  Even or Odd Number of Factors  ####

Create a function that returns "even" if a number has an even number of factors and "odd" if a number has an odd number of factors.


[Examples]

___
factor_group(33) ➞ "even"

factor_group(36) ➞ "odd"

factor_group(7) ➞ "even"
_____



[Notes]

___
*) You don't need to actually calculate the factors to solve this problem.
*) Think about why a number would have an odd number of factors.
___



[logic] [math] [validation] 
"""
import math
def factor_group(n):
    s = math.isqrt(n)
    if s*s == n:
        return "odd"
    else:
        return "even"
print(factor_group(12))