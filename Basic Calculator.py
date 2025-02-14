"""
####  Basic Calculator  ####

Create a function that takes two numbers and a mathematical operator + - / * and will perform a calculation with the given numbers.


[Examples]

___
calculator(2, "+", 2) ➞ 4

calculator(2, "*", 2) ➞ 4

calculator(4, "/", 2) ➞ 2
_____



[Notes]

If the input tries to divide by 0, return: "Can't divide by 0!"


[algebra] [math] [numbers] 
"""
def calculator(a,operator,b):
    if operator == "+":
        print(a+b)
    elif operator == "-":
        print(a-b)
    elif operator == "*":
        print(a*b)
    elif operator == "/":
        if b == 0:
            print("Can't divide by 0!")
        else:
            print(a/b)
    elif operator == "%":
        print(a%b)
    elif operator == "**":
        print(a**b)
    elif operator == "//":
        print(a//b)
a = float(input("Enter number a: "))
b = float(input("Enter number b: "))
operator = input("Enter operator: ")
while True:
    if operator == "+" or operator == "-" or operator == "*" or operator == "/" or operator == "%" or operator == "**" or operator == "//":
            break
    else:
        print("It's not an operator")
        operator = input("You must enter an operator: ")
calculator(a,operator,b)        
             