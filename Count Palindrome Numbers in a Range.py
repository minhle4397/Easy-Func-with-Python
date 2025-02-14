"""
####  Count Palindrome Numbers in a Range  ####

Create a function that returns the number of palindrome numbers in a specified range (inclusive).
For example, between 8 and 34, there are 5 palindromes: 8, 9, 11, 22 and 33. Between 1550 and 1552 there is exactly one palindrome: 1551.


[Examples]

___
count_palindromes(1, 10) ➞ 9

count_palindromes(555, 556) ➞ 1

count_palindromes(878, 898) ➞ 3
_____



[Notes]

___
*) A palindrome number is a number which remains the same when its digits are reversed. For example, 2552 reversed is still 2552. The reflectional symmetry of this number makes it a palindromic number.
*) Single-digit numbers are trivially palindrome numbers.
___



[control_flow] [numbers] [strings] 
"""
def count_palindromes(s,e):
    lst = [x for x in range(s,e+1) if str(x)==str(x)[::-1]]
    return len(lst)
print(count_palindromes(555,556))