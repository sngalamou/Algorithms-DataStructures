class RightTriangle(Polygon):
    def __init__(self,base,height):
        self.base=base
        self.height=height
    def area(self):
        return self.base*self.height/2.0
    def perimeter(self):
        return self.base+self.height+math.sqrt(self.base*self.base+self.height*self.height)

class Square(Polygon):
    def __init__(self,side):
        self.side=side
    def area(self):
        return self.side*self.side
    def perimeter(self):
        return 4*self.side

class Rectangle(Polygon):
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def area(self):
        return self.length*self.width
    def perimeter(self):
        return 2*(self.length+self.width)
