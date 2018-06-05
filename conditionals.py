# Check if a number is a multiple of 3 and a multiple of 7. Print "I'm a multiple of 3 & 7!" if true.
#  Run the program in the command line: python3 conditionals.py

print("Enter a number: ")
# `input()` allows a user input in the command line! The value is a string, hence the need in this case for `int()` to transform it to an integer.

number = int(input())
if number % 3 is 0 and number % 7 is 0:
    print("I'm a multiple of 3 & 7!")
else:
    print('I\'m a multiple of neither 3 or 7!') # Example using the \ escape with single quotes

# Another way:
# if number % 3 is 0:
#     print("I'm a multiple of 3!")
#     if number % 7 is 0:
#         print("I'm a multiple of 7 too!")
#     else:
#         print('I\'m a multiple of 3 only!')
# else:
#     print("I'm neither a multiple of 3 or 7.")

# while loop
while number >= 12 and number <= 27:
  print(f"{number} falls into the correct range.")
  number = number - 1
