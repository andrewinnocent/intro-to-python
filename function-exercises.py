# difference: this function takes in two parameters and returns the difference between the two
def difference(a, b):
    return a - b

# product: this function takes in two parameters and returns the product of the two
def product(a, b):
    return a * b

# print_day: this function takes in one parameter (a number from 1-7) and returns the day of the week (1 is Sunday, 2 is Monday, 3 is Tuesday etc.). If the number is less than 1 or greater than 7, the function should return None
* def print_day(arg):
    days = {1:'Sunday', 2:'Monday', 3:'Tuesday', 4:'Wednesday', 5:'Thursday', 6:'Friday', 7:'Saturday'}
    if arg >= 1 or arg <= 7:
        return days[arg]
    else:
        return None  # Returns KeyError not None

# alternative
def print_day(arg):
    days = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
    if arg >= 1 or arg <= 7:
        return days[arg-1]  # Minus 1 to account for 0-based indexing
    else:
        return None  # Returns IndexError

# Tutorial's solution
def print_day(arg):
    try:
        return ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday'][arg-1]  # I can index directly on the array; no variable needed
    except IndexError:  # Takes care of the error message and returns None
        return None

# last_element: this function takes in one parameter (a list) and returns the last value in the list. It should return None if the list is empty.
def last_element(list):
    try:
        return lst[-1]
    except IndexError:
        return None

# number_compare: this function takes in two parameters (both numbers). If the first is greater than the second, this function returns "First is greater." If the second number is greater than the first, the function returns "Second is greater." Otherwise the function returns "Numbers are equal."
def number_compare(a: int, b: int):
    if a > b:
        return "First is greater."
    elif a < b:
        return "Second is greater."
    else:
        return "Numbers are equal."

# single_letter_count: this function takes in two parameters (two strings). The first parameter should be a word and the second should be a letter. The function returns the number of times that letter appears in the word. The function should be case insensitive (does not matter if the input is lowercase or uppercase). If the letter is not found in the word, the function should return 0.
def single_letter_count(a: str, b: str) -> int:
    return a.lower().count(b.lower())  # Letter cases matter for equality

# multiple_letter_count: this function takes in one parameter (a string) and returns a dictionary with the keys being the letters and the values being the count of the letter.
def multiple_letter_count(string: str):
    return {string[i]: string.count(string[i]) for i in range(0, len(string))}

# alternative
def multiple_letter_count(string):
    return {letter: string.count(letter) for letter in string}

# list_manipulation this function should take in three parameters (a list, command, location and value). If the command is "remove" and the location is "end", the function should remove the last value in the list and return the value removed. If the command is "remove" and the location is "beginning", the function should remove the first value in the list and return the value removed. If the command is "add" and the location is "beginning", the function should add the value (fourth parameter) to the beginning of the list and return the list. If the command is "add" and the location is "end", the function should add the value (fourth parameter) to the end of the list and return the list.
def list_manipulation(a_list, command, location, value=None):  # value=None so that argument doesn't have to be written when not using command `add`
    if command == "remove" and location == "end":
        return a_list.pop()
    elif command == "remove" and location == "beginning":
        return a_list.pop(0)
    elif command == "add" and location == "beginning":
        a_list.insert(0, value)
        return a_list
    elif command == "add" and location == "end":
         a_list.append(value)
         return a_list
    else:
        return "Make sure you have the correct arguments!"

# is_palindrome: A Palindrome is a word, phrase, number, or other sequence of characters which reads the same backward or forward. This function should take in one parameter and returns True or False depending on whether it is a palindrome. As a bonus, allow your function to ignore whitespace and capitalization so that is_palindrome('a man a plan a canal Panama') returns True.
def is_palindrome(word_or_phrase):
    lowered = word_or_phrase.lower()
    split = lowered.split()
    string = ''.join(split)
    return string == string[::-1]

# alternative
def is_palindrome(word_or_phrase):
    string = word_or_phrase.lower().replace(' ','')
    return string == string[::-1]

# frequency: This function accepts a list and a search_term (this will always be a primitive value) and returns the number of times the search_term appears in the list.
def frequency(a_list, search_term):
    return a_list.count(search_term)

# flip_case: This function accepts a string and a letter and reverses the case of all occurances of the letter in the string.
def flip_case(string, letter):
    if letter in string:
        new_string = string.replace(letter, letter.swapcase())
    return new_string

# multiply_even_numbers: This function accepts a list of numbers and returns the product of all even numbers in the list.
def multiply_even_numbers(list_of_numbers):
    evens = []
    total = 1
    for num in list_of_numbers:
        if num % 2 == 0:
            evens.append(num)
    for e in evens:
        total *= e
    return total

# mode: This function accepts a list of numbers and returns the most frequent number in the list of numbers. You can assume that the mode will be unique.
** def mode(arg):
    pass

# capitalize: This function accepts a string and returns the same string with the first letter capitalized.
def capitalize(string: str):
    return string.capitalize()

# compact: This function accepts a list and returns a list of values that are truthy values.
def compact(list):
    truthy = []
    for el in list:
        if bool(el):
            truthy.append(el)
    return truthy

# partition: This function accepts a list and a callback function (which you can assume returns True or False). The function should iterate over each element in the list and invoke the callback function at each iteration. If the result of the callback function is True, the element should go into one list if it's False, the element should go into another list. When it's finished, partition should return both lists inside of one larger list.
def is_even(num):  # callback function
    return num % 2 == 0

def partition(list, is_even):
    arr = []
    truthy = []
    falsey = []
    for el in list:
        if is_even(el):
            truthy.append(el)
        else:
            falsey.append(el)
    arr.append(truthy)
    arr.append(falsey)
    return arr

# intersection: This function should accept a two dimensional list and return a list with the values that are the same in each list.
def intersection(list1, list2):
    arr = []
    for el in list1:
        if el in list2:
            arr.append(el)
    return arr

# once: This function accepts a function and returns a new function that can only be invoked once. If the function is invoked more than once, it should return None. Hint you will need to define a new function inside of your once function and return that function. You can add properties to your inner function to see if it has run already.
** def add(a,b):
    return a + b

def once(add):
    def one_addition(add):
        if add
