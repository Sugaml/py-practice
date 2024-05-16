"""Variable Length Keyword Arguments (**kwargs): """
"""This allows a function to accept any number of keyword arguments as a dictionary."""


def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alish", age=30, city="Kathmandu")