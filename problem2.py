#! python3

"""
Problem 2
Factors are positive integers that divide evenly into another integer.
The user will enter in two numbers. Determine if the smaller is a factor of the larger
(2 marks)

inputs:
an integer
an integer

outputs:
xx is a factor of yy
xx is not a factor of yy

examples:
Enter a number: 10
Enter another number: 2
2 is a factor of 10

Enter a number: 4
Enter another number: 25
4 is not a factor of 25
"""

integer1 = float(input("Enter a number: "))
integer2 = float(input("Enter another number: "))

o = [integer1, integer2]
a = max(o)
b = min(o)
x = a % b

if x == 0:
    print(str(int(b)) + " is a factor of " + str(int(a)))

else:
    print(str(int(b)) + " is not a factor of " + str(int(a)))
