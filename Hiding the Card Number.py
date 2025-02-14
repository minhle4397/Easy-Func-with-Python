"""
####  Hiding the Card Number  ####

Write a function that takes a credit card number and only displays the last four characters. The rest of the card number must be replaced by ************.


[Examples]

___
card_hide("1234123456785678") ➞ "************5678"

card_hide("8754456321113213") ➞ "************3213"

card_hide("35123413355523") ➞ "**********5523"
_____



[Examples]

___
*) Ensure you return a string.
*) The length of the string must remain the same as the input.
___



[formatting] [numbers] [strings] 
"""
def card_hide(st):
    new_st = ['*' for x in range(len(st)-4)]
    for x in st[-4:]:
        new_st.append(x)
    new_st = ''.join(new_st)
    return new_st
print(card_hide("1234123456785678"))