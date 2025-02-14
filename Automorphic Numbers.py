"""
####  Automorphic Numbers  ####

A number n is automorphic if n^2 ends in n.
For example: n=5, n^2=25
Create a function that takes a number and returns True if the number is automorphic, False if it isn't.


[Examples]

___
is_automorphic(5) ➞ True

is_automorphic(8) ➞ False

is_automorphic(76) ➞ True
_____



[Notes]

N/A


[algebra] [numbers] [validation] 
"""
def is_automorphic(a):
    lst = [x for x in str(a**2)]
    a = str(a)
    lst = ''.join(lst[-len(a):])
    return a == lst
    
print(is_automorphic(8))