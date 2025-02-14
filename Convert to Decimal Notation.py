"""
####  Convert to Decimal Notation  ####

Create a function to convert a list of percentages to their decimal equivalents.


[Examples]

___
convert_to_decimal(["1%", "2%", "3%"]) ➞ [0.01, 0.02, 0.03]

convert_to_decimal(["45%", "32%", "97%", "33%"]) ➞ [0.45, 0.32, 0.97, 0.33]

convert_to_decimal(["33%", "98.1%", "56.44%", "100%"]) ➞ [0.33, 0.981, 0.5644, 1]
_____



[Notes]

N/A


[numbers] [strings] 
"""
def convert_to_decimal(lst):
    lst = list(map(lambda x: x/100,[float(x[:-1]) for x in lst]))
    return lst
print(convert_to_decimal(["33%", "98.1%", "56.44%", "100%"]))