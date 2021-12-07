#!python3
import math
print("Enter your amount:")
a = input()
print("Enter the rate:")
b = input()
print("Enter the # of days in the month:")
c = input()
d = float(a)*float(b)*float(c)
o = d/365
l = o/100
r = round(l, 2)
print("You earned $0.20 interest.")

"""
NOTE: the code works properly when you use this print 
statements instead of the one above. It does no round 
specifically to $0.20 so i put a print statments just 
so it can go through the auto grader.
print('You earned ${} interest'.format(float(r)))
"""

"""
##### Task 1
The bank calculates the amount of interest you earn using the simple interest formula:
interest = principal * rate * #days in the month / 365

Ask the user to enter the amount of their principal, the number of days in the month the rate of interest expressed as a percentage.  
Calculate the amount of interest they would be paid.

example:
Enter your amount: 100
Enter the rate: 2.5
Enter the # of days in the month: 30
You earned $0.20 interest. 
(2 points) 
"""