"""
####  Circle or Square  ####

Given the radius of a circle and the area of a square, return True if the circumference of the circle is greater than the square's perimeter and False if the square's perimeter is greater than the circumference of the circle.


[Examples]

___
circle_or_square(16, 625) ➞ True

circle_or_square(5, 100) ➞ False

circle_or_square(8, 144) ➞ True
_____



[Notes]

___
*) You can use Pi to 2 decimal places (3.14).
*) Circumference of a circle equals 2 * Pi * radius.
*) To find the perimeter of a square using its area, find the square root of area (to get side length) and multiply that by 4.
___



[geometry] [validation] 
"""
import math
def Circle_or_Square(radius,area):
    cir = radius*3.14*2
    per = 4*math.sqrt(area)
    return True if cir>per else False
ra = int(input("Enter radius of circle: "))
ar = int(input("Enter area of square: "))
print(Circle_or_Square(ra,ar)) 
