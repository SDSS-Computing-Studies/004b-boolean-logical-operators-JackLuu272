#! python3
"""
Problem 3
Pythagorean triples are sets of 3 integers such that the squares of the 2 smaller numbers is equal to the square of the third.
Ask the user to enter in 3 numbers, in any order.  Order the numbers from smallest to largest.
Determine if they form a Pythagorean triple. 
(2 marks)

Inputs:
an integer
an integer
an integer

Outpus:
xx,yy,zz form a Pythagorean Triple
xx,yy,zz do not form a Pythagorean Triple

Examples:
Enter an integer=>3
Enter an integer=>5
Enter an integer=>4
3,4,5 form a Pythagorean triple

Enter an integer=>5
Enter an integer=>4
Enter an integer=>2
2,4,5 do not form a Pythagorean triple
"""
side1 = float(input(""))
side2 = float(input(""))
side3 = float(input(""))

if side2 > side1 > side3:
    a = side2
    b = side1
    c = side3

elif side3 > side1 > side2:
    a = side3
    b = side1
    c = side2

elif side1 > side2 > side3:
    a = side1
    b = side2
    c = side3

elif side2 > side3 > side1:
    a = side2
    b = side3
    c = side1

elif side3 > side2 > side1:
    a = side3 
    b = side2
    c = side1

else:
    a = side1
    b = side3
    c = side2

if b**2 + c**2 == a**2:
    print(str(c) + "," + str(b) + "," + str(a) + " from a Pythagorean triple")
else:
    print(str(c) + "," + str(b) + "," +str(a) + " do not from a Pythagorean triple")

    