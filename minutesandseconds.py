"""
Question 5. 

Create a class Distance with instance variables min and sec. 
The class also contains the instance method add and compare() to add and compare two distance object respectively.
Use this class to create two different distance object and add and compare these two distance objects.
"""

class Time:
    def __init__(self, min=0, sec=0):
        self.min = min
        self.sec = sec
        self.normalize()
    
    def normalize(self):
        if self.sec >= 60:
            extra_min = int(self.sec / 60) 
            self.min += extra_min
            self.sec = self.sec % 60
    
    def add(self, other):
        new_min = self.min + other.min
        new_sec = self.sec + other.sec
        return Time(new_min, new_sec)
    
    def compare(self, other):
        total_sec_self = self.min * 60 + self.sec
        total_sec_other = other.min * 60 + other.sec
        
        if total_sec_self > total_sec_other:
            return "Faster"
        elif total_sec_self < total_sec_other:
            return "Slower"
        else:
            return "Equal"
    
    def __str__(self):
        return f"{self.min} min {self.sec} sec"

t1 = Time(5, 50)
t2 = Time(14, 14)

result = t1.add(t2)
print(f"Sum of Time: {result}")

comparison = t1.compare(t2)
print(f"Comparison of times : t1 is {comparison} than t2")
