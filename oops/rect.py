class Rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth

    def area(self):
        print(self.length*self.breadth)

    def perimeter(self):
        print(2*(self.length+self.breadth))

r1=Rectangle(5,5)
r1.area()


r2=Rectangle(5,4)
r2.area()
r2.perimeter()