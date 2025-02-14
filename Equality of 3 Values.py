"""
####  Equality of 3 Values  ####

Create a function that takes three integer arguments (a, b, c) and returns the amount of integers which are of equal value.


[Examples]

___
equal(3, 4, 3) ➞ 2

equal(1, 1, 1) ➞ 3

equal(3, 4, 1) ➞ 0 
_____



[Notes]

Your function must return 0, 2 or 3.


[algorithms] [conditions] [numbers] 
"""
def equal(a,b,c):
    if a==b==c:
        return 3
    elif a==b or a==c or b==c:
        return 2
    else : return 0
print(equal(3,4,1))