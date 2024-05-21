class Animal:
    def __init__(self,name):
        self.name=name

    def speak(self):
        raise NotImplementedError("subclass must implement abstract method")
    
class Cat(Animal):
    def speak(self):
        return "Meow"
    
class Dog(Animal):
    def speak(self):
        return "Woof"
    
c=Cat("Kitty")
print(c.speak())
