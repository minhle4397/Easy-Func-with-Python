"""
####  Alphanumeric Restriction  ####

Create a function that returns True if the given string has any of the following:
___
*) Only letters and no numbers.
*) Only numbers and no letters.
___

If a string has both numbers and letters, or contains characters which don't fit into any category, return False


[Examples]

___
alphanumeric_restriction("Bold") ➞ True

alphanumeric_restriction("123454321") ➞ True

alphanumeric_restriction("H3LL0") ➞ False

alphanumeric_restriction("ed@bit") ➞ False
_____



[Notes]

Any string that contains spaces or is empty should return False.


[language_fundamentals] [regex] [strings] [validation] 

"""
def alphanumeric_restriction(st):
    st1 = [True for x in st if x.isdigit()]
    st2 = [True for x in st if x.isalpha()]
    return len(st1)==len(st) or len(st2)==len(st)
print(alphanumeric_restriction("ed@bit"))
