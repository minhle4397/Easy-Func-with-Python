"""
####  Four Passengers and a Driver  ####

A typical car can hold four passengers and one driver, allowing five people to travel around. Given n number of people, return how many cars are needed to seat everyone comfortably.


[Examples]

___
cars_needed(5) ➞ 1

cars_needed(11) ➞ 3

cars_needed(0) ➞ 0
_____



[Notes]

It's likely there will be a few people left over and some cars won't be filled to max capacity.


[algorithms] [math] [numbers] 
"""
import math
def cars_needed(a):
    return math.ceil(a/5)
print(cars_needed(5)) 