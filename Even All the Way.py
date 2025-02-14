"""
####  Even All the Way  ####

Given a list of numbers, return a list which contains all the even numbers in the original list, which also have even indices.


[Examples]

___
get_only_evens([1, 3, 2, 6, 4, 8]) ➞ [2, 4]

get_only_evens([0, 1, 2, 3, 4]) ➞ [0, 2, 4]

get_only_evens([1, 2, 3, 4, 5]) ➞ []
_____



[Notes]

Lists start at index 0.


[arrays] [language_fundamentals] [numbers] 
"""
def get_only_evens(lst):
    return [y for x,y in enumerate(lst) if x%2==0 and y%2==0]
print(get_only_evens([0, 1, 2, 3, 4]))