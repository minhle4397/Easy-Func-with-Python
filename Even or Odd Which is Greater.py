"""
####  Even or Odd: Which is Greater?  ####

Create a function to determine if the sum of all the individual even digits are greater than the sum of all the individual odd digits in a string of numbers.
___
*) If the sum of odd numbers is greater than the sum of even numbers, return "Odd is greater than Even".
*) If the sum of even numbers is greater than the odd numbers, return "Even is greater than Odd".
*) If the sum of both even and odd numbers are equal, return "Even and Odd are the same".
___



[Examples]

___
even_or_odd("22471") ➞ "Even and Odd are the same"

even_or_odd("213613") ➞ "Even and Odd are the same"

even_or_odd("23456") ➞ "Even is greater than Odd"
_____



[Notes]

The input will be a string of numbers.


[algorithms] [arrays] [language_fundamentals] [numbers] [strings] 
"""
def even_or_odd(st):
    odd = sum([int(x) for x in st if int(x)%2!=0])
    even = sum([int(x) for x in st if int(x)%2==0])
    if odd>even:
        return "Odd is greater than Even"
    elif even > odd:
        return "Even is greater than Odd"
    else:
        return "Even and Odd are the same"
print(even_or_odd("23456"))
    