"""
####  Calculating Damage  ####

Create a function that takes damage and speed (attacks per second) and returns the amount of damage after a given time.


[Examples]

___
damage(40, 5, "second") ➞ 200

damage(100, 1, "minute") ➞ 6000

damage(2, 100, "hour") ➞ 720000
_____



[Notes]

Return "invalid" if damage or speed is negative.


[conditions] [math] 
"""
def Damage_Qualities(dam,speed,unit):
    if unit == "second":
        print(dam*speed)
    elif unit == "minute":
        print(dam*speed*60)
    elif unit == "hour":
        print(dam*speed*60*60)
dam = int(input("Enter damge: "))
while True:
    if dam<0:
        print("Invalid input!")
        dam = int(input("Enter positive damge: "))
    else: break
speed = int(input("Enter speed: "))
while True:
    if speed<0:
        print("Invalid input!")
        speed = int(input("Enter positive speed: "))
    else : break

unit  = input("Enter unit: ")

while True:
    if unit!="second" and unit!="minute" and unit!="hour":
        print("Invalid input!")
        unit  = input("Unit must be second, minute or hour: ")
    else: break
Damage_Qualities(dam,speed,unit)