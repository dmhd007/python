square = lambda a : a * a
rectangle = lambda l,b : l * b
triangle = lambda b,h : 0.5 * b * h

square_side=int(input("Enter the side of square : "))
print("The area of Square is : ",square(square_side))

rectangle_length=int(input("Enter the length of rectangle : "))
rectangle_bredth=int(input("Enter the bredth of rectangle : "))
print("The area of Rectangle is : ",rectangle(rectangle_length,rectangle_bredth))

triangle_length=int(input("Enter the breadth of triangle : "))
triangle_height=int(input("Enter the height of triangle : "))
print("The area of Triangle is : ",triangle(triangle_length,triangle_height))