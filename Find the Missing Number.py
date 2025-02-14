"""
####  Find the Missing Number  ####

Create a function that takes a list of numbers between 1 and 10 (excluding one number) and returns the missing number.


[Examples]

___
missing_num([1, 2, 3, 4, 6, 7, 8, 9, 10]) ➞ 5

missing_num([7, 2, 3, 6, 5, 9, 1, 4, 8]) ➞ 10

missing_num([10, 5, 1, 2, 4, 6, 8, 3, 9]) ➞ 7
_____



[Notes]

___
*) The list of numbers will be unsorted (not in order).
*) Only one number will be missing.
___



[algorithms] [interview] [math] [numbers] [sorting] 
"""
def missing_number(lst):
    """lst.sort()
    lst1 = [x for x in range(11) if x!=0]
    for x in lst1:
        if x not in lst:
            return x
        """
    a = sum(lst)
    b = sum(range(11))
    return b-a
print(missing_number([10, 5, 1, 2, 4, 6, 8, 3, 9]))