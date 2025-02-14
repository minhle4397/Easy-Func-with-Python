"""
####  Find the First Non-Repeated Character  ####

Create a function that accepts a string as an argument and returns the first non-repeated character.


[Examples]

___
first_non_repeated_character("g") ➞ "g"

first_non_repeated_character("it was then the frothy word met the round night") ➞ "a"

first_non_repeated_character("the quick brown fox jumps then quickly blows air") ➞ "f"

first_non_repeated_character("hheelloo") ➞ False

first_non_repeated_character("") ➞ False
_____



[Notes]

___
*) An empty string should return False.
*) If every character repeats, return False.
*) Don't worry about case sensitivity or non-alphanumeric characters.
___



[interview] [language_fundamentals] [loops] [strings] 
"""
def first_non_repeated_character(st):
    for x in st:
        if st.count(x)==1:
            return x
    return False
print(first_non_repeated_character("the quick brown fox jumps then quickly blows air"))