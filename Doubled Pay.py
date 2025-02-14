"""
####  Doubled Pay  ####

An employee working at a very bizarre company earns one penny on their first day. However, for every day that passes, their base amount doubles, so they earn two pennies on the second day and four pennies on the third day (totalling 7 pennies). Given a number of days, return how many pennies the employee accumulates.


[Examples]

___
doubled_pay(1) ➞ 1

doubled_pay(2) ➞ 3

doubled_pay(3) ➞ 7
_____



[Notes]

You will only get tests for valid positive integers.


[loops] [math] [numbers] 
"""
def doubled_pay(n):
    return sum((x-1)*2 if x!=1 else x for x in range(1,n+1))
print(doubled_pay(4))