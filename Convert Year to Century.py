"""
####  Convert Year to Century  ####

Write a function that takes a year and returns its corresponding century.


[Examples]

___
century_from_year(2005) ➞ 21

century_from_year(1950) ➞ 20

century_from_year(1900) ➞ 19
_____



[Notes]

For guidance on the year boundaries for each century:
___
*) The 19th century are the years from 1801 to 1900.
*) The 20th century are the years from 1901 to 2000.
___



[algorithms] [dates] [math] 
"""
import math
def century_from_year(a):
    return math.ceil(a/100)
print(century_from_year(1997))