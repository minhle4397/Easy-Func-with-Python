"""
####  Find the Discount  ####

Create a function that takes two arguments: the original price and the discount percentage as integers and returns the final price after the discount.

[Examples]

___
dis(1500, 50) ➞ 750

dis(89, 20) ➞ 71.2

dis(100, 75) ➞ 25
_____

[Notes]

Your answer should be rounded to two decimal places.


[math] [numbers] 
"""
def discount(price,dis):
    price -= price*(dis/100)
    return round(price,2)
a = int(input("Enter price: "))
b = int(input("Enter discount percent: "))
print(discount(a,b))