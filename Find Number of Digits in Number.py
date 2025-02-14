"""
####  Find Number of Digits in Number  ####

Create a function that will return an integer number corresponding to the amount of digits in the given integer num.


[Examples]

___
num_of_digits(1000) ➞ 4

num_of_digits(12) ➞ 2

num_of_digits(1305981031) ➞ 10

num_of_digits(0) ➞ 1
_____



[Notes]

Try to solve this challenge without using strings!


[math] [numbers] 
"""
def num_of_digits(n):
    return len(str(n))
print(num_of_digits(12497))