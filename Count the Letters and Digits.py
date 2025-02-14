"""
####  Count the Letters and Digits  ####

Write a function that takes a string and calculates the number of letters and digits within it. Return the result in a dictionary.


[Examples]

___
count_all("Hello World") ➞ { "LETTERS":  10, "DIGITS": 0 }

count_all("H3ll0 Wor1d") ➞ { "LETTERS":  7, "DIGITS": 3 }

count_all("149990") ➞ { "LETTERS": 0, "DIGITS": 6 }
_____



[Notes]

___
*) Tests contain only alphanumeric characters.
*) Spaces are not letters.
*) All tests contain valid strings.
___



[conditions] [data_structures] [objects] [regex] 
"""
def count_all(st):
    count_letter = 0
    count_digit = 0
    for x in st:
        if x.isalpha():
            count_letter+=1
        elif x!=' ' and x.isdigit():
            
            count_digit+=1
        
    d = {"LETTERS": count_letter,"DIGITS":count_digit}
    return d
print(count_all("149990"))