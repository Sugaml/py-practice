"""
Question 5. 
Create a class Distance with instance variables feet and inches. 
The class also contains the instance method add and compare() to add and compare two distance object respectively.
Use this class to create two different distance object and add and compare these two distance objects.
"""

class Distance:
    def __init__(self, feet=0, inches=0):
        self.feet = feet
        self.inches = inches
        self.normalize()
    
    def normalize(self):
        if self.inches >= 12:
            extra_feet = int(self.inches / 12) 
            self.feet += extra_feet
            self.inches = self.inches % 12
    
    def add(self, other):
        new_feet = self.feet + other.feet
        new_inches = self.inches + other.inches
        return Distance(new_feet, new_inches)
    
    def compare(self, other):
        total_inches_self = self.feet * 12 + self.inches
        total_inches_other = other.feet * 12 + other.inches
        
        if total_inches_self > total_inches_other:
            return "Greater"
        elif total_inches_self < total_inches_other:
            return "Lesser"
        else:
            return "Equal"

dist1 = Distance(5, 10)
dist2 = Distance(4, 14)

result = dist1.add(dist2)
print(f"Sum of distances: {result.feet} feet {result.inches} inches")

comparison = dist1.compare(dist2)
print(f"Comparison of distances: dist1 is {comparison} than dist2")
