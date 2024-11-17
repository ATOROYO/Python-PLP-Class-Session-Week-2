# QUESTION 1
# Accept user input to create a list of integers
numbers = input("Enter a list of integers, separated by spaces: ")

# Split the input string into a list of strings, then convert each to an integer
numbers_list = [int(num) for num in numbers.split()]

# Calculate the sum of the integers in the list
total_sum = sum(numbers_list)

# Output the result
print("The sum of the integers in the list is:", total_sum)

# QUESTION 2
# Create a tuple with five favorite book names
favorite_books = ("The Great Gatsby", "1984", "To Kill a Mockingbird", "Pride and Prejudice", "Moby-Dick")

# Use a for loop to print each book name on a separate line
for book in favorite_books:
    print(book)

# QUESTION 3
# Create an empty dictionary to store the person's information
person_info = {}

# Ask the user for their name, age, and favorite color
person_info["name"] = input("What is your name? ")
person_info["age"] = input("How old are you? ")
person_info["favorite_color"] = input("What is your favorite color? ")

# Print the dictionary containing the person's information
print("\nPerson's Information:")
print(person_info)

