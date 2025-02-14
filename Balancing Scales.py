"""
####  Balancing Scales  ####

Given a list with an odd number of elements, return whether the scale will tip "left" or "right" based on the sum of the numbers. The scale will tip on the direction of the largest total. If both sides are equal, return "balanced".


[Examples]

___
scale_tip([0, 0, "I", 1, 1]) ➞ "right"
# 0 < 2 so it will tip right

scale_tip([1, 2, 3, "I", 4, 0, 0]) ➞ "left"
# 6 > 4 so it will tip left

scale_tip([5, 5, 5, 0, "I", 10, 2, 2, 1]) ➞ "balanced"
# 15 = 15 so it will stay balanced
_____



[Notes]

___
*) The middle element will always be "I" so you can just ignore it.
*) Assume the numbers all represent the same unit.
*) Both sides will have the same number of elements.
*) There are no such things as negative weights in both real life and the tests!
___



[algorithms] [arrays] [conditions] 
"""
def scale_tip(lst):
    a = lst.index("I")
    if sum(lst[:a])>sum(lst[a+1:]):
        return "left"
    elif sum(lst[:a])<sum(lst[a+1:]):
        return "right"
    else:
        return "balanced"
print(scale_tip([0, 0, "I", 1, 1]))