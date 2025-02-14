"""
####  Card Counting (BlackJack)  ####

In BlackJack, cards are counted with -1, 0, 1 values:
___
*) 2, 3, 4, 5, 6 are counted as +1
*) 7, 8, 9 are counted as 0
*) 10, J, Q, K, A are counted as -1
___

Create a function that counts the number and returns it from the list of cards provided.


[Examples]

___
count([5, 9, 10, 3, "J", "A", 4, 8, 5]) ➞ 1

count(["A", "A", "K", "Q", "Q", "J"]) ➞ -6

count(["A", 5, 5, 2, 6, 2, 3, 8, 9, 7]) ➞ 5
_____



[Notes]

___
*) String inputs will always be upper case.
*) You do not need to consider case sensitivity.
*) If the argument is empty, return 0.
*) No input other than: 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A".
___



[algebra] [conditions] [games] [loops] 
"""
def count(lst):
    s1 = list(range(2,7))
    s2 = list(range(7,10))
    
    count = 0
    for x in lst:
        if x in s1:
            count+=1
        elif x in s2:
            continue
        else:
            count-=1
    return count
print(count(["A", 5, 5, 2, 6, 2, 3, 8, 9, 7]))