"""
####  Burglary Series (10): Calculate Difference  ####

The insurance guy calls again and apologizes. They found another policy made by your spouse, but this one is limited to cover a particular maximum in losses (for example, 50,000€). You send a bill to your spouse for the difference you lost.
Given a dict of the stolen items and a limit, return the difference between the total value of those items and the limit of the policy.


[Examples]

___
calc_diff({ "baseball bat": 20 }, 5) ➞ 15

calc_diff({"skate": 10, "painting": 20 }, 19) ➞ 11

calc_diff({"skate": 200, "painting": 200, "shoes": 1 }, 400) ➞ 1
_____



[Notes]

___
*) The dict data always contains at least an item (no empty objects).
*) The sum of the items is always greater than the limit.
___



[arrays] [loops] [objects] 
"""
def calc_diff(d,l):
    return sum(x for x in d.values()) - l
print(calc_diff({"skate": 10, "painting": 20 }, 19))