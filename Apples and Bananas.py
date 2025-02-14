"""
####  Apples and Bananas  ####

Write a function that replaces all vowels in a string with a specified vowel.


[Examples]

___
vow_replace("apples and bananas", "u") ➞ "upplus und bununus"

vow_replace("cheese casserole", "o") ➞ "chooso cossorolo"

vow_replace("stuffed jalapeno poppers", "e") ➞ "steffed jelepene peppers"
_____



[Notes]

___
*) All words will be lowercase.
*) "Y" is not considered a vowel.
___



[language_fundamentals] [strings] 
"""
def vow_replace(st,r):
    st = [r if x in 'aeoui'else x for x in st ]
    return ''.join(st)
print(vow_replace("cheese casserole", "o"))