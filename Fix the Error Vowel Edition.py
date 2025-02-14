"""
####  Fix the Error: Vowel Edition  ####

Your friend is trying to write a function that removes all vowels from a string. They write:
___
def remove_vowels(string):
    vowels = "aeiou"
    for vowel in vowels[1]:
        string.replace(vowel, "", 1)
    return string
_____

However, it seems that it doesn't work? Fix your friend's code so that it actually does remove all vowels.


[Examples]

___
remove_vowels("ben") ➞ "bn"

remove_vowels("hello") ➞ "hllo"
# The "e" is removed, but the "o" is still there!

remove_vowels("apple") ➞ "appl"
# The "e" is removed, but the "a" is still there!
_____



[Notes]

All letters will be lowercase.


[bugs] [regex] [strings] 
"""
def remove_vowels(string):
    vowels = "aeiou"
    st = ''
    for x in string:
        if x not in vowels:
            st+=x
    return st
print(remove_vowels("ben"))