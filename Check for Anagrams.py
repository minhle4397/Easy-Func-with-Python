"""
####  Check for Anagrams  ####

Create a function that takes two strings and returns either True or False depending on whether they're anagrams or not.


[Examples]

___
is_anagram("cristian", "Cristina") ➞ True

is_anagram("Dave Barry", "Ray Adverb") ➞ True

is_anagram("Nope", "Note") ➞ False
_____



[Notes]

___
*) Should be case insensitive.
*) The two given strings can be of different lengths.
___



[interview] [math] [strings] [validation] 
"""
def is_anagram(st1,st2):
    st1 = st1.lower()
    st2 = st2.lower()
    st1 = [x for x in st1]
    st2 = [x for x in st2]
    st1.sort()
    st2.sort()

    return st1 == st2
print(is_anagram("Dave Barry", "Ray Adverb"))