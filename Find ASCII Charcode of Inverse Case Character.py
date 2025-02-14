"""
####  Find ASCII Charcode of Inverse Case Character  ####

Create a function that takes a single character as an argument and returns the char code of its lowercased / uppercased counterpart.


[Examples]

___
Given that:
  - "A" char code is: 65
  - "a" char code is: 97

counterpartCharCode("A") ➞ 97

counterpartCharCode("a") ➞ 65
_____



[Notes]

___
*) The argument will always be a single character.
*) Not all inputs will have a counterpart (e.g. numbers), in which case return the input's char code.
___



[formatting] [strings] 
"""
def counterpartCharCode(st):
    return ord(st.swapcase())
print(counterpartCharCode("a"))