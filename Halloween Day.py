"""
####  Halloween Day  ####

Create a function that takes date in the format yyyy/mm/dd as an input and returns "Bonfire toffee" if the date is October 31, else return "toffee".


[Examples]

___
halloween("2013/10/31") ➞ "Bonfire toffee"

halloween("2012/07/31") ➞ "toffee"

halloween("2011/10/12") ➞ "toffee"
_____



[Notes]

N/A


[numbers] [strings] 
"""
def halloween(st):
    lst = st.split('/')
    if lst[-1]=='31' and lst[-2]=='10':
        return 'Bonfire toffee'
    else:
        return 'toffee'
print(halloween("2012/07/31"))