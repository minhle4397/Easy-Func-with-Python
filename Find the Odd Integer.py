"""
####  Find the Odd Integer  ####

Create a function that takes a list and finds the integer which appears an odd number of times.


[Examples]

___
find_odd([1, 1, 2, -2, 5, 2, 4, 4, -1, -2, 5]) ➞ -1

find_odd([20, 1, 1, 2, 2, 3, 3, 5, 5, 4, 20, 4, 5]) ➞ 5

find_odd([10]) ➞ 10
_____



[Notes]

There will always only be one integer that appears an odd number of times.


[arrays] [bit_operations] [loops] [math] 
"""
def find_odd(lst):
    unique_lst = list(set(lst))
    for x in unique_lst:
        if lst.count(x)%2!=0:
            return x
print(find_odd([10]))    