"""
####  Compare by ASCII Codes  ####

Create a function that compares two words based on the sum of their ASCII codes and returns the word with the smaller ASCII sum.


[Examples]

___
ascii_sort(["hey", "man"]) ➞ "man"
# ["h", "e", "y"] ➞ sum([104, 101, 121]) ➞ 326
# ["m", "a", "n"] ➞ sum([109, 97, 110]) ➞ 316

ascii_sort(["majorly", "then"]) ➞ "then"

ascii_sort(["victory", "careless"]) ➞ "victory"
_____



[Notes]

Both words will have strictly different ASCII sums.


[loops] [strings] 
"""
def ascii_sort(lst):
    if sum(ord(x) for x in lst[0]) > sum(ord(x) for x in lst[1]):
        return lst[1]
    else:
        return lst[0]
print(ascii_sort(["victory", "careless"]))