"""
####  Count the Towers  ####

Create a function that counts the number of towers.


[Examples]

___
count_towers([
  ["     ##         "],
  ["##   ##        ##"],
  ["##   ##   ##   ##"],
  ["##   ##   ##   ##"]
]) ➞ 4

count_towers([
  ["                         ##"],
  ["##             ##   ##   ##"],
  ["##        ##   ##   ##   ##"],
  ["##   ##   ##   ##   ##   ##"]
]) ➞ 6

count_towers([
  ["##"],
  ["##"]
]) ➞ 1
_____



[Notes]

___
*) You are given a 2D matrix.
*) Towers are two characters in length.
*) Towers are made only of the character #.
*) Some tests have no towers, return 0.
___



[arrays] [strings] 
"""
def count_towers(lst):
    if lst[-1] == []:
        return 0
    return lst[-1][0].split().count("##")
print(count_towers([
  [],
  [],
  [],
  []
]))