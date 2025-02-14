"""
####  Bitwise Operations  ####

A decimal number can be represented as a sequence of bits. To illustrate:
___
6 = 00000110
23 = 00010111
_____

From the bitwise representation of numbers, we can calculate the bitwise AND, bitwise OR and bitwise XOR. Using the example above:
___
bitwise_and(6, 23) ➞ 00000110

bitwise_or(6, 23) ➞ 00010111

bitwise_xor(6, 23) ➞ 00010001
_____

Write three functions to calculate the bitwise AND, bitwise OR and bitwise XOR of two numbers.


[Examples]

___
bitwise_and(7, 12) ➞ 4

bitwise_or(7, 12) ➞ 15

bitwise_xor(7, 12) ➞ 11
_____



[Notes]

N/A


[bit_operations] [language_fundamentals] [logic] 
"""
def bitwise_and(a,b):
    return a & b
def bitwise_or(a,b):
    return a | b
def bitwise_xor(a,b):
    return a ^ b
print(bitwise_xor(7,12))