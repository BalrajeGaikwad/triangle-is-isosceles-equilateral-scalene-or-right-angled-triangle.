"""
If the three sides of a triangle are entered through the keyboard, 
write a program to check whether the triangle is isosceles, equilateral, scalene or right angled triangle.

"""

side1=int(input("Enter the side of traingle"))
side2=int(input("Enter the side of traingle"))
side3=int(input("Enter the side of traingle"))


largest=max(side1, side2, side3)

sum_of_two_sides=side1+side2+side3-largest

if(side1==side2 or side2== side3 or side3==side1):
    print("Triangle is isosceles")
elif(side1==side2==side3):
    print("Triangle is equilateral")
elif(side1**2 + side2**2 == side3**2 or side2**2 + side3**2 == side1**2 or side1**2 + side3**2 == side2**2):
    print("right angle ")
else:
    print(" This is not  a traingle")
