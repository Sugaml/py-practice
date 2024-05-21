class Base:
    def base(self):
        print("I am from method")


class Derived(Base):

    def derived(self):
        print("I am from derived class")


obj=Derived()

obj.base()
obj.derived()