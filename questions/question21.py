# Write a program to display only consonants of a given string in Python.

def display_consonants(input_string):
    vowels = "aeiouAEIOU"
    consonants = ""

    for char in input_string:
        if char.isalpha() and char not in vowels:
            consonants += char

    return consonants

input_string = "Welcome to MBA IT in SOMTU Kirtipur, 23 Kathmandu!"
consonants = display_consonants(input_string)
print("Consonants:", consonants)


# Alternatives without function/method
input_string = "Welcome to MBA IT in SOMTU Kirtipur, 23 Kathmandu!"
vowels = "aeiouAEIOU"
consonants = ""

for char in input_string:
    if char.isalpha() and char not in vowels:
        consonants += char

print("Consonants:", consonants)
