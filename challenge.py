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

