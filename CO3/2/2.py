from graphics import circle,rectangle
from graphics.threeD_Graphics.cuboid import *
from graphics.threeD_Graphics import sphere as s

print("--------Circle--------")
r=int(input("Enter the Radious : "))
print("Area of given circle =",circle.area(r))
print("Perimeter of given circle =",circle.perimeter(r))

print("--------Rectangle--------")
l=int(input("Enter the length : "))
b=int(input("Enter the bredth : "))
print("Area of rectangle =",rectangle.area(l,b))
print("Perimeter of rectangle =",rectangle.perimeter(l,b))

print("--------Cuboid--------")
l=int(input("Enter the length of cuboid : "))
b=int(input("Enter the bredth of cuboid : "))
h=int(input("Enter the height of cuboid : "))
print("Area of cuboid =",area(l,b,h))
print("Perimeter of cuboid =",perimeter(l,b,h))

print("--------Sphere--------")
r=int(input("Enter the radious of the sphere : "))
print("Area of the  sphere =",s.area(r))
print("Perimeter of the sphere =",s.perimeter(r))