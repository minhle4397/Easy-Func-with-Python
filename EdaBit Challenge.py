"""
####  "EdaBit" Challenge  ####

Create a function that returns the list of numbers from a given range. But for multiples of three, return “Eda” instead of the number and for the multiples of five, return “Bit”. For numbers which are multiples of both three and five, return “EdaBit”.


[Examples]

___
eda_bit(0, 10) ➞ ["EdaBit", 1, 2, "Eda", 4, "Bit", "Eda", 7, 8, "Eda", "Bit" ]

eda_bit(14, 20) ➞ [14,  "EdaBit", 16, 17,  "Eda", 19, "Bit" ]

eda_bit(99, 106) ➞ ["Eda", "Bit", 101, "Eda", 103, 104, "EdaBit", 106 ]
_____



[Notes]

In case the number 0 happens to be in the range, return "EdaBit" as well.


[algorithms] [math] 
"""
def eda_bit(s,e):
    l = []
    for x in range(s,e+1):
        if x==0 or (x%3==0 and x%5==0):
            l.append("EdaBit")
        elif x%3==0:
            l.append("Eda")
        elif x%5==0:
            l.append("Bit")
        else:
            l.append(x)
    return l
print(eda_bit(99,106)) 