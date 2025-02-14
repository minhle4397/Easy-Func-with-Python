"""
####  Clone a List  ####

The Code tab has code which attempts to add a clone of a list to itself. There is no error message, but the results are not as intended. Can you fix the code?


[Examples]

___
clone([1, 1]) ➞ [1, 1, [1, 1]]

clone([1, 2, 3]) ➞ [1, 2, 3, [1, 2, 3]]

clone(["x", "y"]) ➞ ["x", "y", ["x", "y"]]
_____



[Notes]

N/A


[arrays] [bugs] 

"""
def clone(lst):
    lst += [lst[:]]
    return lst
print(clone([1, 2, 3]))