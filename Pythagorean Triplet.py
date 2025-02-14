"""
####  Pythagorean Triplet  ####

Create a function that validates whether three given integers form a Pythagorean triplet. The sum of the squares of the two smallest integers must equal the square of the largest number to be validated.


[Examples]

___
is_triplet(3, 4, 5) ➞ True
# 3² + 4² = 25
# 5² = 25

is_triplet(13, 5, 12) ➞ True
# 5² + 12² = 169
# 13² = 169

is_triplet(1, 2, 3) ➞ False
# 1² + 2² = 5
# 3² = 9
_____



[Notes]

Numbers may not be given in a sorted order.


[geometry] [math] [numbers] [validation] 
"""
def Pythago_Trip(a,b,c):
    if a**2==(b**2+c**2) or b**2==(a**2+c**2) or c**2==(a**2+b**2):
        return True
    else:
        return False
print(Pythago_Trip(13, 5, 12))