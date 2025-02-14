"""
####  Amplify the Multiples of Four  ####

Create a function that takes an integer and returns a list from 1 to the given number, where:



[Examples]

___
amplify(4) ➞ [1, 2, 3, 40]

amplify(3) ➞ [1, 2, 3]

amplify(25) ➞ [1, 2, 3, 40, 5, 6, 7, 80, 9, 10, 11, 120, 13, 14, 15, 160, 17, 18, 19, 200, 21, 22, 23, 240, 25]
_____



[Notes]

___
*) The given integer will always be equal to or greater than 1.
*) Include the number (see example above).
*) To perform this problem with its intended purpose, try doing it with list comprehensions. If that's too difficult, just solve the challenge any way you can.
___



[algebra] [arrays] [loops] [math] 
"""
def amplify(a):
    lst = [x*10 if x%4==0 else x for x in range(1,a+1)]
    return lst
print(amplify(25))