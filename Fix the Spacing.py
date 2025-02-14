"""
####  Fix the Spacing  ####

Additional spaces have been added to a sentence. Return the correct sentence by removing them. All words should be separated by one space, and there should be no spaces at the beginning or end of the sentence.


[Examples]

___
correct_spacing("The film   starts       at      midnight. ")
➞ "The film starts at midnight."

correct_spacing("The     waves were crashing  on the     shore.   ")
➞ "The waves were crashing on the shore."

correct_spacing(" Always look on    the bright   side of  life.")
➞ "Always look on the bright side of life."
_____



[Notes]

N/A


[formatting] [strings] 
"""
def correct_spacing(st):
    st = st.split()
    return ' '.join(st)
print(correct_spacing("The film   starts       at      midnight. "))