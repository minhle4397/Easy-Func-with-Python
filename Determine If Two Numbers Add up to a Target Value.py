"""
####  Determine If Two Numbers Add up to a Target Value  ####

Given two unique integer lists a and b, and an integer target value v, create a function to determine whether there is a pair of numbers that add up to the target value v, where one number comes from one list a and the other comes from the second list b.
Return True if there is a pair that adds up to the target value and False otherwise.


[Examples]

___
sum_of_two([1, 2], [4, 5, 6], 5) ➞ True

sum_of_two([1, 2], [4, 5, 6], 8) ➞ True

sum_of_two([1, 2], [4, 5, 6], 3) ➞ False

sum_of_two([1, 2], [4, 5, 6], 9) ➞ False
_____



[Notes]

N/A


[arrays] [numbers] [validation] 
"""
def sum_of_two(lst1,lst2,a):
    lst = [True if x+y==a else False for x in lst1 for y in lst2]
    return any(lst)
print(sum_of_two([1, 2], [4, 5, 6], 9))