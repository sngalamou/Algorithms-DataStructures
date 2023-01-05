import math
# Polygon class definition
class Polygon:
    # constructor to initialize variable
    def __init__(self,numberOfSides):
        self.numberOfSides
    # abstract method declaration
    def area(self):
        pass
    def perimeter(self):
        pass

# RightTriangle class definition
class RightTriangle(Polygon):
    # constructor to initialize variables
    def __init__(self,base,height):
        self.base=base
        self.height=height
    # method to calculate and return area
    def area(self):
        return self.base*self.height/2.0
    # method to calculate and return perimeter
    def perimeter(self):
        return self.base+self.height+math.sqrt(self.base*self.base+self.height*self.height)

# Square class definition
class Square(Polygon):
    # constructor to initialize variable
    def __init__(self,side):
        self.side=side
    # method to calculate and return area
    def area(self):
        return self.side*self.side
    # method to calculate and return perimeter
    def perimeter(self):
        return 4*self.side

# Rectangle class definition
class Rectangle(Polygon):
    # constructor to initialize variables
    def __init__(self,length,width):
        self.length=length
        self.width=width
    # method to calculate and return area
    def area(self):
        return self.length*self.width
    # method to calculate and return perimeter
    def perimeter(self):
        return 2*(self.length+self.width)

#main method to test classes
def main():
    # create instances of RightTriangle,Square and Rectangle
    rt=RightTriangle(6,5)
    s=Square(8)
    r=Rectangle(10,9)
    # display area and perimeter of each object by calling area() and perimeter methods
    print("Area of Triangle object:",rt.area())
    print("Perimeter of Triangle object:",rt.perimeter())
    print("Area of Square object:",s.area())
    print("Perimeter of Square object:",s.perimeter())
    print("Area of Rectangle object:",r.area())
    print("Perimeter of Rectangle object:",r.perimeter())
# call main() function
main()
