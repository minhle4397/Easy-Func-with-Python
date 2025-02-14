"""
####  Cumulative List Sum  ####

Create a function that takes a list of numbers and returns a list where each number is the sum of itself + all previous numbers in the list.


[Examples]

___
cumulative_sum([1, 2, 3]) ➞ [1, 3, 6]

cumulative_sum([1, -2, 3]) ➞ [1, -1, 2]

cumulative_sum([3, 3, -2, 408, 3, 3]) ➞ [3, 6, 4, 412, 415, 418]
_____



[Notes]

Return an empty list if the input is an empty list.


[arrays] [loops] [math] [numbers] 
"""
def cumulative_sum(lst):
    return [sum(lst[:x])+y if x!=0 else y for x,y in enumerate(lst)]
print(cumulative_sum([3, 3, -2, 408, 3, 3]))