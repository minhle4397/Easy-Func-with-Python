"""
####  Alternating Ones and Zeroes  ####

Write a function that returns True if the binary string can be rearranged to form a string of alternating 0s and 1s.


[Examples]

___
can_alternate("0001111") ➞ True
# Can make: "1010101"

can_alternate("01001") ➞ True
# Can make: "01010"

can_alternate("010001") ➞ False

can_alternate("1111") ➞ False
_____



[Notes]

___
*) No substring of the output may contain more than one consecutive repeating character (e.g. 00 or 11 are not allowed).
*) Return False if a string only contains 0s or only contains 1s.
___



[logic] [strings] [validation] 
"""
def can_alternate(st):
    st = [x for x in st]
    if abs(st.count('1')-st.count('0'))==1:
        return True
    else:
        return False
print(can_alternate("1111"))