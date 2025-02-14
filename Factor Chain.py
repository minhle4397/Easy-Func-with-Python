"""
####  Factor Chain  ####

A factor chain is a list where each previous element is a factor of the next consecutive element. The following is a factor chain:
___
[3, 6, 12, 36]

# 3 is a factor of 6
# 6 is a factor of 12
# 12 is a factor of 36
_____

Create a function that determines whether or not a list is a factor chain.


[Examples]

___
factor_chain([1, 2, 4, 8, 16, 32]) ➞ True

factor_chain([1, 1, 1, 1, 1, 1]) ➞ True

factor_chain([2, 4, 6, 7, 12]) ➞ False

factor_chain([10, 1]) ➞ False
_____



[Notes]

N/A


[arrays] [loops] [validation] 
"""
def factor_chain(lst):
    return all([lst[x+1]%lst[x]==0 for x,y in enumerate(lst) if x!=len(lst)-1 ])
print(factor_chain([2, 4, 6, 7, 12]))