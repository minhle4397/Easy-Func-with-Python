"""
####  Fix the Error: Filtering out Empty Arrays  ####

I am trying to filter out empty arrays from an array. In other words, I want to transform something that looks like this: ["a", "b", [], [], [1, 2, 3]] to look like ["a", "b", [1, 2, 3]]. My code looks like this:
___
def remove_empty_arrays(arr):
    return [x for x in arr if len(x) != 0]
_____

However, it seems that I've run into a problem, with an error message of object of type 'int' has no len(). Fix my code so that all tests pass.


[Examples]

___
# What I want:
remove_empty_arrays([1, 2, [], 4]) ➞ [1, 2, 4]

# What I am getting:
ERROR: Traceback:
   in <module>
   in remove_empty_arrays
   in <listcomp>
TypeError: object of type 'int' has no len()
_____



[Notes]

N/A


[arrays] [bugs] 
"""
def remove_empty_arrays(arr):
    return [x for x in arr if x != []]
print(remove_empty_arrays(["a", "b", [], [], [1, 2, 3]]))