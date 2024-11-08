#! python3
# Have the user enter in 3 numerical values, representing the side lengths of a triangle. 
# Determine if the values are close enough to make a right triangle. 
# Note: You will need to decide which length is the possibly hypotenuse as the numbers
# are being entered in a random order.
# It is close enough if the expected length of the hypotenuse and the actual length 
# has a percent difference less than 2%
# (2 marks)

# Inputs:
# - 3 numbers, in any order

# Outputs:
# - "that is a right triangle"
# - "that is an acute triangle"
# - "that is an obtuse triangle"
"""
Example:
Enter one side: 5
Enter a second side: 13
Enter third side: 12
that is a right triangle

Enter one side: 13.01
Enter a second side: 5
Enter third side: 12
that is a right triangle

Enter one side: 5
Enter a second side: 15
Enter third side: 12
that is an obtuse triangle


"""
import math


a = float(input("Enter one side: "))

b = float(input("Enter a second side: "))

c = float(input("Enter third side: "))


if a > b and c:
    h = a
    s1 = b
    s2 = c
elif b > a and c:
    h = b
    s1 = a
    s2 = c
elif c > a and b:
    h = c
    s1 = a
    s2 = b


hexpected = math.pow(s1,2) + math.pow(s2,2)

hactual = math.pow(h,2)
lower = hexpected - (hexpected*0.02)
upper = hexpected + (hexpected*0.02)


if hexpected == hactual:
    print("that is a right triangle")
elif lower < hactual < upper:
    print("that is a right triangle")
elif math.pow(s1,2) + math.pow(s2,2) > math.pow(h,2):
    print("that is a acute triangle")
elif math.pow(s1,2) + math.pow(s2,2) < math.pow(h,2):
    print("that is a obtuse triangle")


#done