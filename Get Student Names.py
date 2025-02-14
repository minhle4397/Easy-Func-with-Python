"""
####  Get Student Names  ####

Create a function that takes a dictionary of student names and returns a list of student names in alphabetical order.


[Examples]

___
get_student_names({
  "Student 1" : "Steve",
  "Student 2" : "Becky",
  "Student 3" : "John"
}) ➞ ["Becky", "John", "Steve"]
_____



[Notes]

___
*) Don't forget to return your result.
*) If you get stuck on a challenge, find help in the Resources tab.
*) If you're really stuck, unlock solutions in the Solutions tab.
___



[arrays] [data_structures] [loops] [objects] 
"""
def get_student_names(d):
    l = [x for x in d.values()]
    l.sort()
    return l
print(get_student_names({
  "Student 1" : "Steve",
  "Student 2" : "Becky",
  "Student 3" : "John"
}))