## Python Notes

I have the privilege of interning with the platform analytics software engineering team at Cengage Learning. Python is the main programming language used, so I completed a Udemy course: ["Programming with Python: Hands-On Introduction for Beginners."](https://www.udemy.com/python-programming-beginners/)

These are my notes from the course. Included in this repo are practice problems I worked through.

### Run a Program

Command line: `python3 filePath`

### Variables

Defining a variable is simple: variableName = value
  - Like JavaScript, the value is assigned to the variableName

**Four General Rules to Define a Variable**

1. Start with an alphabet or `_`
  1. variableName or _variableName
2. Case sensitive
  1. variableName != VariableName
3. Reserved words (e.g., `print`) cannot be used
4. Only `_` special character is allowed


### Data Types
* To check the data type: print(type(variable))

1. Number
  1. Integer = whole number like `10`
  2. Float = decimal like `3.5`
2. String
  1. [String interpolation examples](https://www.programiz.com/python-programming/string-interpolation)
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


### Conditionals

Indentations are mandatory and important in defining where the condition belongs. `:` informs that a block of code is next.

`if condition`

**NOTE!**
```py
`if x is y`
# `is` is the same as `==` ONLY with integers.
number = 3
integer = 3
if integer is 3:
  print("They're equal.")

# same as:
if integer == 3:
  print("They're equal.")

# with strings, use `==`
name = "Andrew"
userInput = input()

if userInput is name:
  print("They're equal.")
  # This WON'T print!

if userInput == name:
  print("They're equal.")
  # this WILL print
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
1. for loop
```py
for variable in sequence:
  code
```

```py
letters = ['a', 'b', 'c', 'd']

for letter in letters:
  print(letter)
```
**Range()**

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
  return variableName

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
