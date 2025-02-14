"""
####  Hamming Distance  ####

Hamming distance is the number of characters that differ between two strings.
To illustrate:
___
String1: "abcbba"
String2: "abcbda"

Hamming Distance: 1 - "b" vs. "d" is the only difference.
_____

Create a function that computes the hamming distance between two strings.


[Examples]

___
hamming_distance("abcde", "bcdef") ➞ 5

hamming_distance("abcde", "abcde") ➞ 0

hamming_distance("strong", "strung") ➞ 1
_____



[Notes]

Both strings will have the same length.


[loops] [strings] 
"""
def hamming_distance(st1,st2):
    count = 0
    lst = list(zip(st1,st2))
    for x in lst:
        if len(set(x))>1:
            count+=1
    return count
print(hamming_distance("abcde", "abcde"))