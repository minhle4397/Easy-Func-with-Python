"""
####  Convert Key, Values in a Dictionary to List  ####

Write a function that converts a dictionary into a list of keys-values tuples.


[Examples]

___
dict_to_list({
  "D": 1,
  "B": 2,
  "C": 3
}) ➞ [("B", 2), ("C", 3), ("D", 1)]

dict_to_list({
  "likes": 2,
  "dislikes": 3,
  "followers": 10
}) ➞ [("dislikes", 3), ("followers", 10), ("likes", 2)]
_____



[Notes]

Return the elements in the list in alphabetical order.


[arrays] [objects] 
"""
def dict_to_list(d):
    lst = list(d.keys())
    lst.sort()
    return [(x,d[x]) for x in lst]
print(dict_to_list({
  "likes": 2,
  "dislikes": 3,
  "followers": 10
}))