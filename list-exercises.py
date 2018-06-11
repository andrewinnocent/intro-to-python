# Complete using list comprehension.

# Given a list [1,2,3,4], print out all the values in the list.
[print(value) for value in [1,2,3,4]]

# Given a list [1,2,3,4], print out all the values in the list multiplied by 20.
[print(value*20) for value in [1,2,3,4]]

# Given a list ["Elie", "Tim", "Matt"], return a new list with only the first letter (["E", "T", "M"]).
[name[0] for name in ["Elie", "Tim", "Matt"]]

# Given a list [1,2,3,4,5,6] return a new list of all the even values ([2,4,6]).
[num for num in [1,2,3,4,5,6]
if num % 2 == 0]

# Given two lists [1,2,3,4] and [3,4,5,6], return a new list that is the
# intersection of the two ([3,4]).
*[num for num in [1,2,3,4] and [3,4,5,6]
if num == 3 or num == 4] # the output is correct, but I'm not sure if it's right.

[val for val in [1,2,3,4] if val in [3,4,5,6]]

# Given a list of words ["Elie", "Tim", "Matt"] return a new list with each word
# reversed and in lower case (['eile', 'mit', 'ttam']).
[name[::-1].lower() for name in ["Elie", "Tim", "Matt"]]

reversed = [] # long way

for el in ["Elie", "Tim", "Matt"]:
    reversed.append(el[::-1].lower())

# Given two strings "first" and "third", return a new string with all the letters
# present in both words (["i", "r", "t"]).
[el for el in "first" and "third"
if el in ["i", "r", "t"]]

# For all the numbers between 1 and 100, return a list with all the numbers that
# are divisible by 12 ([12, 24, 36, 48, 60, 72, 84, 96]).
[num for num in range(1,100) if num % 12 == 0]

# Given the string "amazing", return a list with all the vowels removed
# (['m', 'z', 'n', 'g']).
[el for el in "amazing"
if el not in ['a', 'e', 'i', 'o', 'u']]

# Generate a list with the value [[0, 1, 2], [0, 1, 2], [0, 1, 2]].
# for each i there will be a num array
[[num for num in range(0,3)] for i in range(0,3)]

# Generate a list with the value:
[[num for num in range(0,10)] for i in range(0,10)]
