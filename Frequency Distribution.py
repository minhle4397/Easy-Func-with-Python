"""
####  Frequency Distribution  ####

Create a function that returns the frequency distribution of a list. This function should return an object, where the keys are the unique elements and the values are the frequency in which those elements occur.


[Examples]

___
get_frequencies(["A", "B", "A", "A", "A"]) ➞ { "A" : 4, "B" : 1 }

get_frequencies([1, 2, 3, 3, 2]) ➞ { 1: 1, 2: 2, 3: 2 }

get_frequencies([True, False, True, False, False]) ➞ { True: 2, False: 3 }

get_frequencies([]) ➞ {}
_____



[Notes]

___
*) If given an empty list, return an empty object (see example #4).
*) The object should be in the same order as in the input list.
___



[language_fundamentals] [loops] [objects] 
"""
def get_frequencies(lst):
    if lst == []:
        return []
    else:
        a = list(set(lst))
        d = {x:lst.count(x) for x in a}
        return d
print(get_frequencies([]))