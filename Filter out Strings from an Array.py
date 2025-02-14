"""
####  Filter out Strings from an Array  ####

Create a function that takes a list of non-negative integers and strings and return a new list without the strings.


[Examples]

___
filter_list([1, 2, "a", "b"]) ➞ [1, 2]

filter_list([1, "a", "b", 0, 15]) ➞ [1, 0, 15]

filter_list([1, 2, "aasf", "1", "123", 123]) ➞ [1, 2, 123]
_____



[Notes]

___
*) Zero is a non-negative integer.
*) The given list only has integers and strings.
*) Numbers in the list should not repeat.
*) The original order must be maintained.
___



[arrays] [formatting] [loops] 
"""
def filter_list(st):
    lst = list()
    for x in st:
        if isinstance(x,int):
            lst.append(x)
    return lst
print(filter_list([1, "a", "b", 0, 15]))
