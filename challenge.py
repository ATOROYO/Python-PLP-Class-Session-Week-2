# Accept user input to create a list of integers
numbers = input("Enter a list of integers, separated by spaces: ")

# Split the input string into a list of strings, then convert each to an integer
numbers_list = [int(num) for num in numbers.split()]

# Calculate the sum of the integers in the list
total_sum = sum(numbers_list)

# Output the result
print("The sum of the integers in the list is:", total_sum)
