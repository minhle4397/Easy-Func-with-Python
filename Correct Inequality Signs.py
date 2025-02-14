"""
####  Correct Inequality Signs  ####

Create a function that returns True if a given inequality expression is correct and False otherwise.


[Examples]

___
correct_signs("3 < 7 < 11") ➞ True

correct_signs("13 > 44 > 33 > 1") ➞ False

correct_signs("1 < 2 < 6 < 9 > 3") ➞ True
_____



[Notes]

N/A


[regex] [strings] [validation] 
"""
def correct_signs(expr):
    return eval(expr)
print(correct_signs("1 < 2 < 6 < 9 > 3"))