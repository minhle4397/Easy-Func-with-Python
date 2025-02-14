"""
####  Solving Exponential Equations With Logarithms  ####

Create a function that takes a number a and finds the missing exponent x so that a when raised to the power of x is equal to b.


[Examples]

___
solve_for_exp(4, 1024) ➞ 5

solve_for_exp(2, 1024) ➞ 10

solve_for_exp(9, 3486784401) ➞ 10
_____



[Notes]

a is raised to the power of what in order to equal b?


[algorithms] [math] [numbers] 
"""
import math
def solve_for_exp(a,b):
    return math.log(b,a)
a = int(input())
b = int(input())
print(solve_for_exp(a,b))    