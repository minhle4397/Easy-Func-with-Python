"""
####  Apocalyptic Numbers  ####

In this challenge, you have to establish if a number is apocalyptic. A positive integer n greater than 0 is apocalyptic when 2 elevated to n contains one or more occurrences of 666 inside it.
Given an integer n, implement a function that returns:
___
*) "Safe" if n is not apocalyptic.
*) "Single" if inside 2^n there's a single occurrence of 666.
*) "Double" if inside 2^n there are two occurrences of 666.
*) "Triple" if inside 2^n there are three occurrences of 666.
___



[Examples]

___
is_apocalyptic(66) ➞ "Safe"
# 2^66 = 73786976294838206464

is_apocalyptic(157) ➞ "Single"
# 2^157 =
# 182687704|666|362864775460604089535377456991567872

is_apocalyptic(220) ➞ "Double"
# 2^220 =
# 168499|666|66969149871|666|8844293872691710232152640 ...

is_apocalyptic(931) ➞ "Triple"
# 2^931 =
# 181520618710|666|8777829|666|135436890332191479738353753001777065257954029122510259245050254290156440857653562895251700406555730694879815558725330603736697259064676478076718090|666| ...
_____



[Notes]

___
*) Any given n will be a positive integer in the range of 1 to 1000.
*) Occurrences have to be unique. You can't use digits that have already been matched again (see example #3, there are five adjacent 6s, but only one possible match).
___



[numbers] [strings] [validation] 
"""
def is_apocalyptic(n):
    a = len(str(pow(2,n)).split("666"))
    if a == 1:
        return "Safe"
    elif a == 2:
        return "Single"
    elif a == 3:
        return "Double"
    else:
        return "Triple" 
print(is_apocalyptic(66))