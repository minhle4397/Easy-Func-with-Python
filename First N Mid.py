"""
####  First N Mid  ####

Create a function that takes a string and returns the first character of every word if the length of the word is even and the middle character if the length of the word is odd.


[Examples]

___
stmid("Alexa have to paid") ➞ "ehtp"
# "e" is the middle character of "Alexa"
# "h" is the first character of "have"

stmid("Th3 0n3 4nd 0n1y") ➞ "hnn0"

stmid("who is the winner") ➞ "hihw"
_____



[Notes]

N/A


[math] [strings] 
"""
def stmid(st):
    st = st.split()
    s = ""
    for x in st:
        if len(x)%2==0:
            s+= x[0]
        else:
            s+= x[int(len(x)/2)]
    return s
print(stmid("who is the winner"))