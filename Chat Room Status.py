"""
####  Chat Room Status  ####

Write a function that returns the number of users in a chatroom based on the following rules:

For example, if there are 5 users, return:
___
"user1, user2 and 3 more online"
_____



[Examples]

___
chatroom_status([]) ➞ "no one online"

chatroom_status(["paRIE_to"]) ➞ "paRIE_to online"

chatroom_status(["s234f", "mailbox2"]) ➞ "s234f and mailbox2 online"

chatroom_status(["pap_ier44", "townieBOY", "panda321", "motor_bike5", "sandwichmaker833", "violinist91"])
➞ "pap_ier44, townieBOY and 4 more online"
_____



[Notes]

N/A


[arrays] [control_flow] 
"""
def chatroom_status(lst):
    if lst == []:
        return "no one online"
    elif len(lst)==1:
        return f"{lst[0]} online"
    elif len(lst)==2:
        return f"{lst[0]} and {lst[1]} online"
    else :
        return f"{lst[0]}, {lst[1]} and {len(lst)-2} more online"
print(chatroom_status(["pap_ier44", "townieBOY", "panda321", "motor_bike5", "sandwichmaker833", "violinist91"]))