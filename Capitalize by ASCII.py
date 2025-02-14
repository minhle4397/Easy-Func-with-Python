"""
####  Capitalize by ASCII  ####

Create a function that takes a string as input and capitalizes a letter if its ASCII code is even and returns its lower case version if its ASCII code is odd.


[Examples]

___
ascii_capitalize("to be or not to be!") ➞ "To Be oR NoT To Be!"

ascii_capitalize("THE LITTLE MERMAID") ➞ "THe LiTTLe meRmaiD"

ascii_capitalize("Oh what a beautiful morning.") ➞ "oH wHaT a BeauTiFuL moRNiNg."
_____



[Notes]

N/A


[higher_order_functions] [strings] 
"""
def ascii_capitalize(st):
    st = ''.join([x.upper() if ord(x)%2==0 else x.lower() for x in st])
    return st
print(ascii_capitalize("Oh what a beautiful morning."))