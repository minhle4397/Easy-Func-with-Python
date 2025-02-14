"""
####  Are Letters in the Second String Present in the First?  ####

Create a function that accepts a list of two strings and checks if all of the letters in the second string are present in the first string.


[Examples]

___
letter_check(["trances", "nectar"]) ➞ True

letter_check(["compadres", "DRAPES"]) ➞ True

letter_check(["parses", "parsecs"]) ➞ False
_____



[Notes]

___
*) Function should not be case sensitive (as indicated in the second example).
*) Both strings are presented as a single argument in the form of a list.
*) Bonus: Solve this without RegEx.
___



[regex] [strings] [validation] 
"""
def letter_check(lst):
    lst = list(map(lambda x: x.lower(),lst))
    for x in lst[1]:
        if x not in lst[0]:
            return False
    return True
            
print(letter_check(["parses", "parsecs"]))