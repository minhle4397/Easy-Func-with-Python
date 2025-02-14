"""
####  Flip the Boolean  ####

Create a function that reverses a boolean value and returns the string "boolean expected" if another variable type is given.


[Examples]

___
reverse(True) ➞ False

reverse(False) ➞ True

reverse(0) ➞ "boolean expected"

reverse(None) ➞ "boolean expected"
_____



[Notes]

___
*) Don't forget to return the result.
*) If you get stuck on a challenge, find help in the Resources tab.
*) If you're really stuck, unlock solutions in the Solutions tab.
___



[conditions] [language_fundamentals] [logic] 

"""
def reverse(a):
    if isinstance(a,bool):
        return not a
    else :
        return "boolean expected"

print(reverse(0))