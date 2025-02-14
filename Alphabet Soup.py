"""
####  Alphabet Soup  ####

Create a function that takes a string and returns a string with its letters in alphabetical order.


[Examples]

___
alphabet_soup("hello") ➞ "ehllo"

alphabet_soup("edabit") ➞ "abdeit"

alphabet_soup("hacker") ➞ "acehkr"

alphabet_soup("geek") ➞ "eegk"

alphabet_soup("javascript") ➞ "aacijprstv"
_____



[Notes]

You can assume numbers and punctuation symbols won't be included in test cases. You'll only have to deal with single word, alphabetic characters.


[formatting] [sorting] [strings] 
"""
def alphabet_soup(st):
    lst = [x for x in st]
    lst.sort()
    st = ''.join(lst)
    return st
print(alphabet_soup("hacker"))