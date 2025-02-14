"""
####  Finding Nemo  ####

You're given a string of words. You need to find the word "Nemo", and return a string like this: "I found Nemo at [the order of the word you find Nemo]!".
If you can't find Nemo, return "I can't find Nemo :(".


[Examples]

___
find_nemo("I am finding Nemo !") ➞ "I found Nemo at 4!"

find_nemo("Nemo is me") ➞ "I found Nemo at 1!"

find_nemo("I Nemo am") ➞ "I found Nemo at 2!"
_____



[Notes]

___
*) ! , ? . are always separated from the last word.
*) Nemo will always look like Nemo, and not NeMo or other capital variations.
*) Nemo's, or anything that says Nemo with something behind it, doesn't count as Finding Nemo.
*) If there are multiple Nemo's in the sentence, only return the first one.
___



[arrays] [formatting] [strings] 
"""
def find_nemo(st):
    st = st.split()
    return f"I found Nemo at {st.index('Nemo')+1}!"
print(find_nemo("I Nemo am"))