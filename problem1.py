"""
Problem 1
Ask the user to enter a number.
The number is considered "frue" if it is
divisible by 6, but not divisible by 8.
State whether the number is "frue" 
(2 marks)

Inputs:
a number

Outputs:
xx is frue
xx is not frue

example:
Enter a number: 48
48 is not frue
"""

#! python3

number = int(input("Enter a number: "))

x = number % 6 
y = number % 8

if x == 0 and y > 0:
    print(str(number) + " is frue")

elif (x > 0 and y ==0) or (x == 0 and y ==0):
    print(str(number) + " is not frue")