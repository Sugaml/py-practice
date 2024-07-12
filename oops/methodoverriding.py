class Employee():
    def __init__(self,name,sal):
        self.name=name
        self.sal=sal

    def get_sal(self):
        return self.sal
    

class SalesEmployee(Employee):
    def __init__(self,name,sal,inctive):
        super().__init__(name,sal)
        self.inctive=inctive

    def get_sal(self):
        return self.sal+self.inctive

hari=SalesEmployee("Hari",12000,1200)
print(hari.get_sal())