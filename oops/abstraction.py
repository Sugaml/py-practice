from abc import ABC, abstractclassmethod

class Shape(ABC):
    @abstractclassmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self,width,height):
        self.width=width
        self.height=height


    def area(self):
        return self.width*self.height
    

r=Rectangle(10,8)
print(r.area())