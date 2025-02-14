"""
####  Emotify the Sentence  ####

Create a function that changes specific words into emoticons. Given a sentence as a string, replace the words smile, grin, sad and mad with their corresponding emoticons.



[Examples]

___
emotify("Make me smile") ➞ "Make me :D"

emotify("Make me grin") ➞ "Make me :)"

emotify("Make me sad") ➞ "Make me :("
_____



[Notes]

___
*) The sentence always starts with "Make me".
*) Try to solve this without using conditional statements like if/else.
___



[conditions] [formatting] [language_fundamentals] [strings] 
"""
def emotify(st):
    st = st.split()
    if st[-1] == "sad":
        st[-1] = ":("
    elif st[-1] == "smile":
        st[-1] = ":D"
    elif st[-1] == "grin":
        st[-1] = ":)"
    else:
        st[-1] = ">:("
    return ' '.join(st)
print(emotify("Make me grin")) 