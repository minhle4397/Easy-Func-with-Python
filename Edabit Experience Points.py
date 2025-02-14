"""
####  Edabit Experience Points  ####

As you complete questions on Edabit, you gain experience points depending on the difficulty of the question. The points for each difficulty are as follows:

Given a dictionary of how many questions a person has completed of each difficulty, return how many experience points they'll have.


[Examples]

___
get_xp({
  "Very Easy" : 89,
  "Easy" : 77,
  "Medium" : 30,
  "Hard" : 4,
  "Very Hard" : 1
}) ➞ "2055XP"


get_xp({
  "Very Easy" : 254,
  "Easy" : 32,
  "Medium" : 65,
  "Hard" : 51,
  "Very Hard" : 34
}) ➞ "7650XP"


get_xp({
  "Very Easy" : 11,
  "Easy" : 0,
  "Medium" : 2,
  "Hard" : 0,
  "Very Hard" : 27
}) ➞ "2255XP"
_____



[Notes]

Return values as a string and make sure to add "XP" to the end.


[arrays] [numbers] [strings] 
"""
def get_xp(d):
    c=0
    for x,y in d.items():
        if x=="Very Easy":
            c+=(y*5)
        elif x=="Easy":
            c+=(y*10)
        elif x=="Medium":
            c+=(y*20)
        elif x=="Hard":
            c+=(y*40)
        else:
            c+=(y*80)
    return f"{c}XP"
print(get_xp({
  "Very Easy" : 254,
  "Easy" : 32,
  "Medium" : 65,
  "Hard" : 51,
  "Very Hard" : 34
}))