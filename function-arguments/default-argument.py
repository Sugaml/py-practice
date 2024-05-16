"""Default Arguments: """
"""You can specify default values for parameters."""
"""If the argument is not provided when calling the function, the default value is used."""

def greet(name, message="How are you?"):
    print(f"Hello, {name}! {message}")

greet("Anish")