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
7. _ _variable_name_ _ (double underscore or 'dunder') private or are builtins to the language



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
  3. access similar to list, e.g. `tuple_name[0]` returns `object1`
  4. `del(tuple_name)` deletes the variable from memory
5. Dictionary {object}
  1. key:value pairs
  2. **NOTE** strings must be in quotes, including the key.
  3. literal notation: `dict = {"name": "Andrew", "car": "BMW"}`
  4. dictionary function `dict_function = dict(key = "value", key2 = "value2")`
    1. **NOTE** key can't be an integer when using dict()
    2. **NOTE** key will automatically receive quotes in the output
    3. **NOTE** dictionaries do not guarantee any kind of order
6. Sets
  1. DO NOT have duplicate values
    1. `s = set({1,1,4,4,5})` returns `{1,4,5}`
    2. `s = {1,4,2,5}`
  2. Elements ARE NOT ordered, i.e., cannot access an element by index


### Operators

Your usual suspects of: `+`, `-`, `*`, `/`, `%`, `<`, `<=`, `>`, `>=`, `==` (NO `===`), `!=`

Python-specific:
`and`, `or`, `not()` (not `&&`, `||`), `is` (in addition to `==`)

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
# prints 1...7 & All the numbers printed w/o breaking the loop.
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

Default argument values are used to provide default values when defining a function.

```py
# Default argument value example
def add(a=10, b=15):
  return a + b

add() # 25

# New argument values can be passed:
add(5, 3) # 8
add(5) # 20
add(b=8) #18
```

Keyword arguments are used when calling a function. The benefit is passing in the
arguments in any order.

```py
# Keyword argument value example
def add(a, b):
  return a + b

add(b=10, a=4) # 14
```
Variable number of function arguments using `*`. There are two ways to use it:
1. `*` in the function definition allows any number of arguments to be passed.

```py
def example(*args):
  print(args)

example(1,2,3) # (1,2,3)
example([1,2,3]) # ([1,2,3])

# Result is a tuple with the arguments passed in.
```
2. (2.) `*` used in calling (invoking) a function. `*` takes an iterable and splits it into individual arguments.

```py
def add_three_nums(n1, n2, n3):
  return n1 + n2 + n3

add_three_nums(*[4,5,6]) #same as add_three_nums(4,5,6)
```

Unpacking an argument is used to convert a collection to comma separated values.
```py
def add_and_mult_nums(a, b, c):
  return a + b * c

nums = [1,2,3]
nums2 = (2,3,4)

add_and_mult_nums(nums) # TypeError: missing 2 required positional arguments: 'b' and 'c'
add_and_mult_nums(*nums) # 7 (order of operations is automatic)

add_and_mult_nums(nums2) # TypeError: missing 2 required positional arguments: 'b' and 'c'
add_and_mult_nums(*nums2) # 14
```
Variable number of keyword arguments is to pass an unknown number of keyword arguments with `**`.

```py
def print_kwargs(a, b, **kwargs):
    print(a, b, kwargs)

print_kwargs(1, 2, awesome='sauce', test='yup') # 1 2 {'awesome': 'sauce', 'test': 'yup'}
```

Unpacking a dictionary into keyword arguments with `**`.

```py
def add_and_mult_nums(a, b, c):
  return a + b * c

data = dict(a=1, b=2, c=3)

add_and_mult_nums(data) # TypeError missing 2 required positional arguments: 'b' and 'c'
add_and_mult_nums(**data) # 7
```

Default argument types define what data type a variable is supposed to be passed.

```py
# Specifies that a and b are integers and the return value is also an integer.
def add(a: int, b: int) -> int:
    """This function returns the sum of two numbers""" # This is a docstring
    return a + b   

#  Specifies default parameter values as well as data types
def add_again(a: int = 5 ,b: int = 5) -> int:
    """This function returns the sum of two numbers with default values of 5 for a and 5 for b"""
    return a + b

add.__doc__ # 'This function returns the sum of two numbers'

help(add_again) # prints more details...
# Help on function add_again in module __main__:
#
# add_again(a:int=5, b:int=5) -> int
#     This function returns the sum of two numbers with default values of 5 for a and 5 for b
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

### Dictionary Iteration and Comprehension

- `for in` loops iterate through the keys

```py
a = dict(name = "Andrew", job = "Intern")

for key in a:
  print(key)

# name
# job
```
- To access both keys and value, call `items()` on the dictionary

```py
a = dict(name = "Andrew", job = "Intern")

for key, value in a.items():
  print(key, value)

# name Andrew
# job Intern
```
- Dictionary Comprehension
**NOTE** I can create a dictionary using other data types through dictionary comprehensions.

```py
str1 = "ABC"
str2 = "123"
{str1[i]: str2[i] for i in range(0, len(str1))} # length of str1 is most important b/c that is the key
# {'A': '1', 'B': '2', 'C': '3'}
```

```py
num_list = [1,2,3,4]
{ num:("even" if num % 2 == 0 else "odd") for num in num_list }
# {1:"odd", 2:"even", 3:"odd", 4:"even"}
```
