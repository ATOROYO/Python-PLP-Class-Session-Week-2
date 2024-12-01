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

# QUESTION 4
# Accept user input to create the first set
set1_input = input("Enter the integers for the first set, separated by spaces: ")
set1 = set(map(int, set1_input.split()))

# Accept user input to create the second set
set2_input = input("Enter the integers for the second set, separated by spaces: ")
set2 = set(map(int, set2_input.split()))

# Create a new set containing the common elements
common_elements = set1 & set2

# Print the result
print("The common elements between both sets are:", common_elements)

# QUESTION 5
# Store a list of words
words = ["apple", "banana", "cherry", "date", "kiwi", "orange", "melon"]

# Use list comprehension to create a new list with words that have an odd number of characters
odd_length_words = [word for word in words if len(word) % 2 != 0]

# Print the result
print("Words with an odd number of characters:", odd_length_words)


