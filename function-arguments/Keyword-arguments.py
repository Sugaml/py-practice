"""Keyword Arguments:"""
"""When you pass arguments by specifying the parameter name along with the value,"""
"""it allows you to pass them in any order. This can improve code readability."""

def greet(name, message):
    print(f"Hello, {name}! {message}")

greet(message="How are you?", name="Anish")
