'''
Small program to calculate the area and perimeters of small set of shapes
 depending on the right choice of the three shapes and what to calculate
'''
import shapes_functions 


shape = input("Enter the Shape (Triangle, Square, Circle) :")

calc = input("What to calculate (Area, Perimeter) :")


if (shape == "Triangle" and calc=="Area"):
    shapes_functions.triangle_area()
elif (shape == "Triangle" and calc=="Perimeter"):
    shapes_functions.triangle_perimeter()
elif (shape == "Square" and calc=="Perimeter"):
    shapes_functions.square_perimeter()
elif (shape == "Square" and calc=="Area"):
    shapes_functions.square_area()()
elif (shape == "Circle" and calc=="Perimeter"):
    shapes_functions.circle_perimeter()
elif (shape == "Circle" and calc=="Area"):
    shapes_functions.circle_area()
else:
    print("Enter right Choices")    



