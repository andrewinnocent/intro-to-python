## Python Notes

I have the privilege of interning with the platform analytics software engineering team at Cengage Learning. Python is the main programming language used, so I completed a Udemy course: ["Programming with Python: Hands-On Introduction for Beginners."](https://www.udemy.com/python-programming-beginners/)

These are my notes from the course. Included in this repo are practice problems I worked through.

Additional resource from [Rithm School](https://www.rithmschool.com/courses/python-fundamentals-part-1).

### Run a Program

Command line: `python3 filePath`

### Variables

Defining a variable is simple: variable_name = value
  - Like JavaScript, the value is assigned to the variable_name

**Four General Rules to Define a Variable**

1. Start with an alphabet or `_`
  1. variable_name or _variable_name
2. Case sensitive
  1. variable_name != variable_Name
3. Reserved words (e.g., `print`) cannot be used
4. Only `_` special character is allowed
5. CAPITAL_SNAKE_CASE usually refers to constants
6. UpperCamelCase usually refers to a class
7. __variable_name__ private or are builtins to the language



### Data Types
* To check the data type: print(type(variable))

1. Number
  1. Integer = whole number like `10`
  2. Float = decimal like `3.5`
2. String (Unicode is default encoding)
  1. [String interpolation examples](https://www.programiz.com/python-programming/string-interpolation)
  2. Iterable like a list
  3. Immutable
3. List [array]
4. ** *Tuple* **
  1. Once defined cannot change values - immutable
  2. tupleName = (object1, object2, object3)
  3. access similar to list, e.g. `tupleName[0]` returns `object1`
  4. `del(tupleName)` deletes the variable from memory
5. Dictionary {object}
  1. key:value pairs
  2. **NOTE** strings must be in quotes, including the key.

### Operators

Your usual suspects of: `+`, `-`, `*`, `/`, `%`, `<`, `<=`, `>`, `>=`, `==` (NO `===`), `!=`

Python-specific:
`and`, `or`, `not()` (not `&&`, `||`), `is` (instead of `==`)

**Cool Stuff**

Division:
`6 / 2` returns `3.0`
`6 // 2` returns `3`
`5 / 2` returns `2.5`
`5 // 2` returns `2`

### Falsey Values

```py
# False
bool(False)

# 0
bool(0)

# None
bool(None)

# Empty string
bool("")

# Empty list
bool([])

# Empty tuple
bool(())

# Empty dictionary
bool({})

# Empty set
bool(set())
```

### Conditionals

Indentations are mandatory and important in defining where the condition belongs. `:` informs that a block of code is next.

`if condition`

**NOTE!**
```py
`if x is y`
# `is` is used to compare if object id's match (everything is Python is an object with an id). `==` is used to compare if objects have the same `value`.

# `is` is "the same" as `==` ONLY with integers for a True result.
number = 3 # id(number) => 4305328608 (in memory)
integer = 3 # id(integer) => 4305328608 (in memory)
if integer is 3: # same IDs in memory => True
  print("They're equal.")

# same as:
if integer == 3: # same values => True
  print("They're equal.")

# with strings, use `==`
name = "Andrew"
userInput = input("What's your name? ")

if userInput is name:
  print("They're equal.")
  # This WON'T print!

if userInput == name:
  print("They're equal.")
  # this WILL print
```

```py
# you can string inequalities together without using the `and` keyword
if 1 < 2 and 2 < 3:
    print("this is ok")

if 1 < 2 < 3:
    print("this is better!")
```
```py
gradeScore = 92

if gradeScore >= 90:
  print("You got an 'A'")

# if false, there's no output
```
```py
gradeScore = 92
attendanceScore = 93

if gradeScore >= 90 and attendanceScore >= 90:
  print("You are a very disciplined student!")
```
```py
gradeScore = 92
attendanceScore = 73

if gradeScore >= 90 or attendanceScore >= 90:
  print("You are a very disciplined student!")
```
```py
gradeScore = 92

if gradeScore is 92:
  print(f"You scored a {gradeScore}.")
```

`if-else condition`
```py
gradeScore = 92

if gradeScore >= 90:
  print("You got an 'A'")
else:
  print("Study smarter, not harder")
```

`if-elif condition`
```py
gradeScore = 60

if gradeScore >= 90:
  print("You got an 'A'")
elif gradeScore >= 40:
  print("Congrats! You passed.")
else:
  print("You have failed :(")
```

`nested if condition`
```py
gradeScore = 100

if gradeScore >= 90:
  print("You got an 'A'")
  if gradeScore == 100:
    print("You got a perfect score!")
```
**Looping Statements**
1. `for in` loop
Syntax:
```py
for element in list:
  code to execute
```

```py
letters = ['a', 'b', 'c', 'd']

for letter in letters:
  print(letter)

# To print the element index and element, use the enumerate() function. The for takes two variables representing index & element.
for index, letter in enumerate(letters):
  print(index, letter)
```
**Range()**
Ranges take up less memory than lists.

Syntax: `range(stop)`

stop: Number of integers (whole numbers) to generate, starting from zero. eg. `range(3) == [0, 1, 2]`.

Syntax: `range([start], stop[, step])`

start: Starting number of the sequence.

stop: Generate numbers up to, but not including this number.

step: Difference between each number in the sequence.
```py
# The range is exclusive of the top number
for number in range(1, 10):
  print(number)
  # prints 1...9
```

```py
# The range is exclusive of the top number
for number in range(2, -7, -2):
  print(number)
  # prints 2, 0, -2, -4, -6
```
2. while loop
```py
number = 25
while number >= 12 and number <= 27:
  print(f"{number} falls into the correct range.")
  number = number - 1
```
3. break
```py
for number in range(1, 8):
  if number == 5:
    break
  else:
    print(number)
# prints 1...4
```
4. continue
```py
for number in range(1, 8):
  if number == 5:
    continue
  else:
    print(number)
# prints 1...4, 6...8
```
5. else
```py
for number in range(1, 8):
  if number == 10:
    break
  else:
    print(number)
else:
  print("All the numbers printed w/o breaking the loop.")
# prints 1...8 & All the numbers printed w/o breaking the loop.
```

## Functions

Syntax:
```py
# define a function
def functionName():
  blockOfCode
  return variable_name

# call/invoke a function
functionName()

# the return is accessible when assigned to a variable
returned = functionName()
```

### Exception Handling

The purpose is for a user to understand why something doesn't work, e.g. division by 0.

```py
try:
	length = 10
	width = 0
	length / width
except Exception: # `Exception` is a generic class name
	print("Division by zero is invalid!")

# When the code is executed, the exception will print.
```

```py
del(width) # Continuing from the previous snippet, the variable `width` is deleted from memory.

width # return this error:
# Traceback (most recent call last):
#   File "<pyshell#9>", line 1, in <module>
#     width
# NameError: name 'width' is not defined
try:
	length / width
except Exception:
	print("Division by zero is invalid!")

# When the code is executed, the exception will print, HOWEVER `width` doesn't exist!
# Use the specified exception name from the error, ie. NameError

try:
	length / width
except NameError:
	print("Variable is used before defining it.")
# Returns an appropriate exception message to the user.

# Multiple exceptions can be used at once:
try:
	length / width
except NameError:
	print("Variable used before defining it.")
except ZeroDivisionError:
	print("Division by zero is invalid!")
```
### Slicing Lists

Slices return portions of a list or string.

The standard syntax for a slice is `list[start:end]`, or `list[start:end:step]`. We can also do list[:] to make a copy of a list, or even `list[::-1]` to make a copy of a reversed list.

```py
first_list = [1,2,3,4,5,6]
first_list[0:1] # [1]

# if a value for end isn't provided, you'll slice to the end of the list
first_list[1:] # [2, 3, 4, 5, 6]

# if a value for start isn't provided, you'll slice from the start of the list
first_list[:3] # [1,2,3]

# get the last element in the list
first_list[-1] # 6

# start from the second to last element in the list
first_list[-2:] # [5, 6]

# There is always more than one way of doing something...
first_list[4:] == first_list[-2:] # True

# step in the opposite direction
first_list[::-1] # [6, 5, 4, 3, 2, 1]

# step in the opposite direction by two elements
first_list[::-2] # [6, 4, 2]
```
### List Comprehension

List comprehensions are an alternative to loops.

One use is to transform a set of values from a range or another list into a new set of values.

```py
# return a list of squares
[num**2 for num in range(10)] # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# chr() function takes in a number and returns the ascii character for the number
[chr(num) for num in range(65,91)]
# ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
```
With `if` statements:
```py
[
letter
for letter in 'awesome'
if letter in ['a','e','i','o','u']
]
# ['a', 'e', 'o', 'e']
```
