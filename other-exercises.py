# Have your program get a word or phrase from the user and two numbers. Use those two numbers to slice the string and print out that slice.
# user_phrase = input("Write a short phrase: ")
# user_number1 = int(input("Enter a number: "))
# user_number2 = int(input("Enter another number: "))
#
# output = user_phrase[user_number1:user_number2]
#
# print(output)

# Create one that will ask users for their hourly rate and the number of hours they've worked and calculate their weekly pay. If users have worked more than 40 hours, pay 1 1/2 times the regular hourly wage.

# rate = int(input("Enter hourly rate: "))
# hours_worked = int(input("Enter hours worked: "))
#
# if hours_worked > 0 and hours_worked <= 40:
#     print(f"You've earned ${hours_worked * rate}.")
# elif hours_worked > 40:
#     print(f"You've earned overtime. Your paycheck is ${((hours_worked - 40) * (rate * 1.5)) + (40 * rate)}")
# else:
#     print("Enter valid info.")

# Prompt user for wind speed and print the hurricane category
# speed = int(input("Enter wind speed: "))
#
# if speed >= 74 and speed <= 95:
#     print("Category 1")
# elif speed >= 96 and speed <= 110:
#     print("Category 2")
# elif speed >= 111 and speed <= 130:
#     print("Category 3")
# elif speed >= 131 and speed <= 155:
#     print("Category 4")
# elif speed >= 156:
#     print("Category 5")
# else:
#     print("It's a tropical storm, not a hurricane.")

# while loop using...
# number = 1
# answer = 'y'
# while answer == 'y':
#          print (number)
#          number = number + 1
#          answer = input("Do you want the next number? ").lower()

# get some numbers from our user and compute the average
# times = int(input("How many numbers would you like to average? "))
# sum = 0
# for count in range(times):  # 0...times
#     val = float(input("Pick a number: "))  # float() to allow decimals.
#     sum += val
# print(f"The average is {sum/times}.")

# phrase = input("Enter a phrase: ")
# letter = input("Enter a letter: ")
# length = len(phrase)
#
# for index in range(0, length):
#     if phrase [index] == letter:
#         break
# else:
#     print ("Your letter wasn't found")

# Write a program that reads in a list of numbers from the users and displays the sum and average of this list. Your program should allow the users to enter as many numbers as they wish. When the users are finished entering numbers, they'll enter the value -1. Be sure not to include the -1 in your calculations for the sum and average.
# times = int(input("How many numbers would you like to sum and average? "))
# sum = 0
# for count in range(times):  # 0...times
#     if count < times:
#         val = float(input("Pick a number: "))  # float() to allow decimals.
#         sum += val
# else:
#     int(input("Type -1: "))
#     print(f"The sum is {sum} and the average is {sum/times}.")

# Sample solution
count = 0
sum = 0.0
# average = 0.0
value = eval(input("Please enter a number (-1 quits): "))  # eval() allows for both floats and integers

while (value != -1):
    sum += value
    count += 1

    value = eval(input("Please enter a number (-1 quits): "))

# This is necessary, in case the user doesn't enter any values before quitting
if (count != 0):
    average = sum / count

print ("The sum of these numbers is", sum)
print ("The average of these numbers is", average)
