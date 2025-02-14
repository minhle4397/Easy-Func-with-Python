"""
####  Return the Factorial  ####

Create a function that takes an integer and returns the factorial of that integer. That is, the integer multiplied by all positive lower integers.


[Examples]

___
factorial(3) ➞ 6

factorial(5) ➞ 120

factorial(13) ➞ 6227020800
_____



[Notes]

Assume all inputs are greater than or equal to 0.


[algebra] [math] [numbers] [recursion]
"""
def factorial(a):
    if a == 1:
        return a
    else: return a*factorial(a-1)
a = int(input("Enter a number of integer: "))
print(factorial(a))