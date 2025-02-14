"""
####  Harshad Numbers  ####

A number n is a Harshad (also called Niven) number if it is divisible by the sum of its digits. For example, 666 is divisible by 6 + 6 + 6, so it is a Harshad number.
Write a function to determine whether the given number is a Harshad number.


[Examples]

___
is_harshad(209) ➞ True

is_harshad(41) ➞ False

is_harshad(12255) ➞ True
_____



[Notes]

N/A


[math] [numbers] [strings] [validation] 
"""
def is_harshad(n):
    st = [int(x) for x in str(n)]
    return n%sum(st)==0
print(is_harshad(12255))