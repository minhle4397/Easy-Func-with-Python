"""
####  Flatten the Curve  ####

Given a list of integers, replace every number with the mean of all numbers.


[Examples]

___
flatten_the_curve([1, 2, 3, 4, 5]) ➞ [3, 3, 3, 3, 3]

flatten_the_curve([0, 0, 0, 2, 7, 3]) ➞ [2, 2, 2, 2, 2, 2]

flatten_the_curve([4]) ➞ [4]

flatten_the_curve([]) ➞ []
_____



[Notes]

___
*) Round averages to 1 decimal point.
*) Return an empty list if given an empty list (see example #4).
___



[arrays] [language_fundamentals] [numbers] 
"""
import numpy as np
def flatten_the_curve(lst):
    return [np.mean(lst) for x in lst ]
print(flatten_the_curve([0, 0, 0, 2, 7, 3]))