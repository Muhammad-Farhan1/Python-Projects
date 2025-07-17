length = input("Enter the length of rectangle : ")
width = input("Enter the width of rectangle : ")

area = float(length) * float(width)
#print(f"The area of rectangle is : {area}")



#calculation of circumference of circle (2*3.14*r)
import math
radius = input("Enter the radius of circle :")
pie_value = math.pi
area = 2 * pie_value * float(radius)
#print(f"The value of area of circumference of circle is {round(area ,3)}")


#area of circle (2*3.14*r*r)
import math
radius = float(input("Enter the area of circle :"))
area = 2 * math.pi * radius * radius
#print(f"The area of circle is : {round(area , 2)}")



#Hypotenuse of triangle
import math
side_a = float(input("Enter the value of side A:"))
side_b = float(input("Enter the value of side B:"))

c = (math.sqrt(pow(side_a , 2) + pow(side_b , 2)))
d = round(c , 2)
#print(f"The value of third side of a triangle is : {d}")