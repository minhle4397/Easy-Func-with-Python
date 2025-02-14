"""
####  Folding a Piece of Paper  ####

Create a function that returns the thickness (in meters) of a piece of paper after folding it n number of times. The paper starts off with a thickness of 0.5mm.


[Examples]

___
num_layers(1) ➞ "0.001m"
# Paper folded once is 1mm (equal to 0.001m)

num_layers(4) ➞ "0.008m"
# Paper folded 4 times is 8mm (equal to 0.008m)

num_layers(21) ➞ "1048.576m"
# Paper folded 21 times is 1048576mm (equal to 1048.576m)
_____



[Notes]

___
*) There are 1000mm in a single meter.
*) Don't round answers.
___



[algebra] [formatting] [math] [numbers] 
"""
def num_layers(n):
    return pow(2,n)*0.5*pow(10,-3)
print(f"{num_layers(21)}m")