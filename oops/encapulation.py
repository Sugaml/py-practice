class Person:
    def __init__(self,name,age):
        self.__name=name
        self.__age=age

    def get_name(self):
        return self.__name
    
    def set_name(self,name):
        self.__name=name

    
p=Person("Hari",40)
print(p.get_name())

p.set_name("Ram")
print(f"{p.get_name()}")