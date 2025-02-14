"""
####  Find the Other Two Side Lengths  ####

Given the shortest side of a 30° by 60° by 90° triangle, find out the other two sides. Return the longest side and medium-length side in that order.


[Examples]

___
returnsides(1) ➞ (2, 1.73)

returnsides(2) ➞ (4, 3.46)

returnsides(3) ➞ (6, 5.2)
_____



[Notes]

___
*) 30 60 90 triangles always follow this rule: let's say the shortest side length is x units, the hypotenuse would be 2x units and the other side would be x * square root of 3.
*) In the Tests, the decimal is rounded to 2 places.
*) Return the values as a tuple.
___



[geometry] [math] 
"""
import math
def returnsides(n):
    x = round(math.tan(math.pi/3)*n,2) 
    y = round(math.sqrt(pow(x,2)+pow(n,2)),2)
    return (y,x)
print(returnsides(1))