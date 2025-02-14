"""
####  Format V: Alignment  ####

For each challenge of this series you do not need to submit a function. Instead, you need to submit a template string that can be formatted in order to get a certain outcome.
Write three template strings according to the following example. All final strings must have a length of 30 characters. Notice the period . at the end of the strings:


[Example]

___
name = "John"

left_align = "yourtemplatestringhere"
center_align = "yourtemplatestringhere"
right_align = "yourtemplatestringhere"

left_align.format(name) ➞ "My name is John              ."
center_align.format(name) ➞ "My name is        John       ."
right_align.format(name) ➞ "My name is               John."
_____



[Tips]

The placeholders {:<x}, {:^x}, {:>x} are used to align left, center and right respectively within a width x.
For example:
___
"Credits: {:>7}".format(128) ➞ "Credits:     128"
_____



[Notes]

___
*) Submit a string, not a function.
*) Do not change the name of the variables left_align, center_align, right_align.
*) You can find all the exercises in this series over here.
___



[formatting] [language_fundamentals] [strings] 
"""
name = "John"

left_align = "My name is {0} {1:<15}."
center_align = "My name is {0:^20s}."
right_align = "My name is {0:>20s}."

formatted_left = left_align.format(name, "")
formatted_center = center_align.format(name)
formatted_right = right_align.format(name)

print(formatted_left)
print(formatted_center)
print(formatted_right)





