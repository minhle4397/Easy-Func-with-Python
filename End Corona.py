"""
####  End Corona!  ####

Create a function that takes the number of daily average recovered cases recovers, daily average new_cases, current active_cases, and returns the number of days it will take to reach zero cases.


[Examples]

___
end_corona(4000, 2000, 77000) ➞ 39

end_corona(3000, 2000, 50699) ➞ 51

end_corona(30000, 25000, 390205) ➞ 79
_____



[Notes]

___
*) The number of people who recover per day recovers will always be greater than daily new_cases.
*) Be conservative and round up the number of days needed.
___



[math] [numbers] 
"""
import math
def end_corona(recover,new_cases,active_cases):
    return math.ceil(active_cases/(recover-new_cases))
l = [0]*3
l[0] = int(input("Enter number of recover: "))
l[1] = int(input("Enter number of new cases: "))
l[2] = int(input("Enter number of active case: "))
print(end_corona(*l))