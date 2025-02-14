"""
####  Default Mood  ####

Create a function that takes in a current mood and return a sentence in the following format: "Today, I am feeling {mood}". However, if no argument is passed, return "Today, I am feeling neutral".


[Examples]

___
mood_today("happy") ➞ "Today, I am feeling happy"

mood_today("sad") ➞ "Today, I am feeling sad"

mood_today() ➞ "Today, I am feeling neutral"
_____



[Notes]

Check the Resources tab for some helpful information.


[language_fundamentals] [strings] 
"""
def mood_today(mood='neutral'):
    return f"Today, I am feeling {mood}"
mood = input("Enter your mood: ")
print(mood_today(mood))