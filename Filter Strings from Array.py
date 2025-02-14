"""
####  Filter Strings from Array  ####

Create a function that takes a list of strings and integers, and filters out the list so that it returns a list of integers only.


[Examples]

___
filter_list([1, 2, 3, "a", "b", 4]) ➞ [1, 2, 3, 4]

filter_list(["A", 0, "Edabit", 1729, "Python", "1729"]) ➞ [0, 1729]

filter_list(["Nothing", "here"]) ➞ []
_____



[Notes]

Don't overthink this one.


[arrays] [conditions] [loops] [strings] 
"""
def filter_list(lst):
    lst = [x for x in lst if isinstance(x,int)]
    return lst
print(filter_list(["Nothing", "here"]))