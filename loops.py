#  Check if a book exists in the collection

books = ["Holy Bible", "How to Bake", "Sacred Marriage"]
print("Enter the name of the book: ")
userInput = input().title() # Title Case Method

for book in books:
    if userInput == book: # case sensitive
        print(f"'{userInput}' is available.")
        break
else:
    print(f"'{userInput}' isn't available currently")
