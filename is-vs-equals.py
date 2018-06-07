name = "Andrew"
print(id(name))

userInput = input("What's your name? ")
print(id(userInput))

# Even if user input is "Andrew", it's assigned a different ID in memory.
if userInput is name:
    print("They have the same ID in memory, so True.")
else:
    print("IDs are different in memory, so False.")

if userInput == name:
    print("They have the same value in memory, so True.")
else:
    print("Values are different in memory, so False.")
