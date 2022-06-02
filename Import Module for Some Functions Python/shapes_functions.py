def triangle_area():
    base = int(input("Base= "))
    height = int(input("Height= "))
    area = 0.5 * base * height
    print("The Area of Triangle is: ", area)


def triangle_perimeter():
    side1 = int(input("First Side = "))
    side2 = int(input("Second Side = "))
    side3 = int(input("Third Side = "))
    perimeter = side1+side2+side3
    print("The Perimeter of Triangle is: ", perimeter)
    

def square_area():
    side = int(input("Side = "))
    area = side**2
    print("The Area of The Square is: ",area)
    
 
def square_perimeter():
    side = int(input("Side = "))
    perimeter = side*4
    print("The Perimter of The Square is: ",perimeter)
    

def circle_area():
    radius = int(input("Radius = "))
    area = (22/7) * radius**2
    print("The Area of The Circle is: ", area)
    
    
    
def circle_perimeter():
    radius = int(input("Radius = "))
    perimeter = (22/7) * radius * 2
    print("The Perimeter of The Circle is: ", perimeter)