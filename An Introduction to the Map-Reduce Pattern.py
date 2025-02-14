"""
####  An Introduction to the Map-Reduce Pattern  ####

You will be implementing a basic case of the map-reduce pattern in programming. Given a vector stored as a list of integers, find the magnitude of the vector. Use the standard distance formula for n-dimensional Cartesian coordinates.


[Examples]

___
magnitude([3, 4]) ➞ 5

magnitude([0, 0, -10]) ➞ 10

magnitude([]) ➞ 0

magnitude([2, 3, 6, 1, 8] ) ➞ 10.677078252031311
_____



[Notes]

___
*) The list can have any length.
*) The input list will contain integers (except for empty list [] ➞ 0).
___



[arrays] [functional_programming] [higher_order_functions] [math] 
"""
import math
import numpy as np
def magnitude(lst):
    x = np.array(lst)
    return np.linalg.norm(x)
    #return math.sqrt(sum(math.pow(x,2) for x in lst))
print(magnitude([2, 3, 6, 1, 8])) 