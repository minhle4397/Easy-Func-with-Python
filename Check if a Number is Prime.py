"""
####  Check if a Number is Prime  ####

Create a function that returns True if a number is prime, and False otherwise. A prime number is any positive integer that is evenly divisible by only two divisors: 1 and itself.
The first ten prime numbers are:
___
2, 3, 5, 7, 11, 13, 17, 19, 23, 29
_____



[Examples]

___
is_prime(31) ➞ True

is_prime(18) ➞ False

is_prime(11) ➞ True
_____



[Notes]

___
*) A prime number has no other factors except 1 and itself.
*) If a number is odd it is not divisible by an even number.
*) 1 is not considered a prime number.
___



[math] [validation] 
"""
import math
def is_prime(n):
    if n<=1:
        return False
    elif n == 2 or n == 3:
        return True
    else:
        for x in range(2,int(math.sqrt(n))+1):
            if n%x==0:
                return False
    return True
print(is_prime(29))