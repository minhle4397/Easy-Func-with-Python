"""
####  Grab the City  ####

Write a function to return the city from each of these vacation spots.


[Examples]

___
grab_city("[Last Day!] Beer Festival [Munich]") ➞ "Munich"

grab_city("Cheese Factory Tour [Portland]") ➞ "Portland"

grab_city("[50% Off!][Group Tours Included] 5-Day Trip to Onsen [Kyoto]") ➞ "Kyoto"
_____



[Notes]

There may be additional brackets, but the city will always be in the last bracket pair.


[regex] [strings] 
"""
def grab_city(st):
    st = st.split()
    return st[-1][1:-1]
print(grab_city("[Last Day!] Beer Festival [Munich]"))