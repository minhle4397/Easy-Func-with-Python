"""
####  Purge and Organize  ####

Given a list of numbers, write a function that returns a list that...



[Examples]

___
unique_sort([1, 2, 4, 3]) ➞ [1, 2, 3, 4]

unique_sort([1, 4, 4, 4, 4, 4, 3, 2, 1, 2]) ➞ [1, 2, 3, 4]

unique_sort([6, 7, 3, 2, 1]) ➞ [1, 2, 3, 6, 7]
_____



[Notes]

N/A


[arrays] [data_structures] [loops] [numbers] [sorting] 
"""
def unique_sort(lst):
    lst = list(set(lst))
    lst.sort()
    return lst
print(unique_sort([6, 7, 3, 2, 1]))