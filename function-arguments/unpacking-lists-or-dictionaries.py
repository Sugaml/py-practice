"""Unpacking Lists or Dictionaries:"""
"""You can pass elements of a list or dictionary as individual arguments to a function using the * and ** operators, respectively."""

def greet(name, message):
    print(f"Hello, {name}! {message}")

info = {"name": "Anish", "message": "Nice to meet you!"}
greet(**info)
