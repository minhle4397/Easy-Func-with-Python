"""
####  Even Number Generator  ####

Using list comprehensions, create a function that finds all even numbers from 1 to the given number.


[Examples]

___
find_even_nums(8) ➞ [2, 4, 6, 8]

find_even_nums(4) ➞ [2, 4]

find_even_nums(2) ➞ [2]
_____

Try to use list comprehensions in your solution. Here's an example:
___
vals = [expression 
  for value in collection 
    if condition]
_____

This is equivalent to:
___
vals = []
for value in collection:
  if condition:
    vals.append(expression)
_____



[Notes]

___
*) Try to use list comprehensions instead of logic.
*) If there are no even numbers, return an empty list.
___



[arrays] [conditions] [numbers] 
"""
def find_even_nums(a):
    lst = [x for x in range(a+1) if x%2==0 and x!=0]
    return lst
print(find_even_nums(8))