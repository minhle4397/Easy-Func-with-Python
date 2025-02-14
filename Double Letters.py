"""
####  Double Letters  ####

Create a function that takes a word and returns True if the word has two consecutive identical letters.


[Examples]

___
double_letters("loop") ➞ True

double_letters("yummy") ➞ True

double_letters("orange") ➞ False

double_letters("munchkin") ➞ False
_____



[Notes]

N/A


[regex] [strings] [validation] 
"""
def double_letters(st):
    for x,y in enumerate(st):
        if x==len(st)-1:
            return False
        elif st[x]==st[x+1]:
            return True
print(double_letters(""))