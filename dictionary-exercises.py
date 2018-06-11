#  Use dictionary comprehension to solve the exercises

# Given a list [("name", "Elie"), ("job", "Instructor")], create a dictionary
# that looks like this {'job': 'Instructor', 'name': 'Elie'} (the order does not matter).
{k:v for k, v in [("name", "Elie"), ("job", "Instructor")]}

# Given two lists ["CA", "NJ", "RI"] and ["California", "New Jersey", "Rhode Island"]
# return a dictionary that looks like this
# {'CA': 'California', 'NJ': 'New Jersey', 'RI': 'Rhode Island'}.
# You can research the zip method (https://docs.python.org/3.3/library/functions.html#zip)to help you.
{k:v for k, v in zip(["CA", "NJ", "RI"], ["California", "New Jersey", "Rhode Island"])}

# Create a dictionary with the key as a vowel in the alphabet and the value as 0.
# Your dictionary should look like this {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}.
# (Do not use the fromkeys method).
{k:0 for k in ['a', 'e', 'i', 'o', 'u']}

# Create a dictionary starting with the key of the position of the letter and
# the value as the letter in the alphabet. You should return something like this
# (Hint - use chr(65) to get the first letter):
{(count-64):chr(count) for count in range(65, 91)}

{1: 'A',
 2: 'B',
 3: 'C', ...}
