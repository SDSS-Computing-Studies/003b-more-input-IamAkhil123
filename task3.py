#!python3
##### Task 3
a = input("enter the first price")
b = input("enter the second price")
c = input("enter the third price")
d = input("enter the fourth price")
e = input("enter the fifth price")
f = float(a) + float(b) + float(c) + float(d) + float(e)
g = float(f) * 0.12
h = float(g) + float(f)
i = round(g, 2)
j = round(h, 2)
print('Your subtotal is ${}'.format(float(f)),'and your taxes total ${}'.format(float(i)), 'for a total of ${}'.format(float(j)))

"""
When shopping, we pay 12% combined GST and PST on many items.  
Write a program that asks the user to enter in the prices of 4 items that they are buying.  
Find the total price, the amount of tax and the overall price.  Taxes are rounded appropriately
example:
Enter the first price: 11.99
Enter the second price: 14.76
Enter the third price: 12.99
Enter the fourth price: 15.98
Enter the fifth price: 7.99
Your subtotal is $63.71 and your taxes total $7.65 for a total of $71.36
"""