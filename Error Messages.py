"""
####  Error Messages  ####

Create a function that takes a number as an argument and returns the appropriate error message. You should do this without using the switch or if statements.
The input error will be 1 to 5:
___
1 >> "Check the fan: e1"
2 >> "Emergency stop: e2"
3 >> "Pump Error: e3"
4 >> "c: e4"
5 >> "Temperature Sensor Error: e5"
_____

For any other value, return 101 (you can use an if statement here).


[Examples]

___
error(1) ➞ "Check the fan: e1"

error(2) ➞ "Emergency stop: e2"

error(3) ➞ "Pump Error: e3"
_____



[Notes]

Do this without using the switch or if statements.


[conditions] [strings] 
"""
def error(n):
    d = {1:"Check the fan: e1", 2:"Emergency stop: e2", 3:"Pump Error: e3", 4:"c: e4",
         5:"Temperature Sensor Error: e5"}
    if n not in d.keys():
        return "101"
    else:
        return d[n]
print(error(5))