"""
####  Count Ones in Binary Representation of Integer  ####

Count the amount of ones in the binary representation of an integer. For example, since 12 is 1100 in binary, the return value should be 2.


[Examples]

___
count_ones(0) ➞ 0

count_ones(100) ➞ 3

count_ones(999) ➞ 8
_____



[Notes]

The input will always be a valid integer (number).


[formatting] [numbers] 

"""
def count_ones(a):
    binary = bin(a)[2:]
    binary_lst = [int(x) for x in binary if x == '1']
    return sum(binary_lst)
print(count_ones(13))