"""
####  Find the Area of a (Regular) Hexagon  ####

Given the side length x find the area of a hexagon.



[Examples]

___
area_of_hexagon(1) ➞ 2.6

area_of_hexagon(2) ➞ 10.4

area_of_hexagon(3) ➞ 23.4
_____



[Notes]

___
*) Return None if the side length given is not a positive integer.
*) Round to the nearest tenth.
___



[algorithms] [geometry] [math] 
"""
import math
def area_of_hexagon(n):
    return round(1.5*pow(n,2)*math.sqrt(3),1)
print(area_of_hexagon(3))