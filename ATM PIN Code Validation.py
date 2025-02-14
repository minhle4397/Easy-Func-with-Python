"""
####  ATM PIN Code Validation  ####

ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain anything but exactly 4 digits or exactly 6 digits. Your task is to create a function that takes a string and returns True if the PIN is valid and False if it's not.


[Examples]

___
is_valid_PIN("1234") ➞ True

is_valid_PIN("12345") ➞ False

is_valid_PIN("a234") ➞ False

is_valid_PIN("") ➞ False
_____



[Notes]

___
*) Some test cases contain special characters.
*) Empty strings must return False.
___



[regex] [validation] 
"""
def is_valid_PIN(st):
    if not st.isdigit() or (len(st)!=4 and len(st)!=6):
        return False
    else: return True
print(is_valid_PIN(""))
    