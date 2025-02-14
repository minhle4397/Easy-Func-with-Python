"""
####  Functioninator 8000  ####

Create a function that takes a single word string and does the following:

The examples should make this clear.


[Examples]

___
inator_inator("Shrink") ➞ "Shrinkinator 6000"

inator_inator("Doom") ➞ "Doominator 4000"

inator_inator("EvilClone") ➞ "EvilClone-inator 9000"
_____



[Notes]

For the purposes of this challenge, vowels will be a, e, i, o and u only.


[formatting] [strings] 
"""
def inator_inator(st):
    if st[-1] not in "aeiou":
        return st+'inator '+f'{len(st)}000'
    else:
        return st+'-inator '+f'{len(st)}000'
print(inator_inator("Shrink"))