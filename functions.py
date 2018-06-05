# Take two numbers from user input and return the maximum number

# By convention, functions are defined first in the file.
def findMaximum(firstNumber, secondNumber):
    if firstNumber > secondNumber:
        return firstNumber
    elif firstNumber is secondNumber:
        return "Your numbers are the same! Try again."
    else:
        return secondNumber

print("Enter the first number: ")
firstNumber = int(input())

print("Enter the second number: ")
secondNumber = int(input())

maximumNumber = findMaximum(firstNumber, secondNumber)
print(f'Maximum number = {maximumNumber}')
