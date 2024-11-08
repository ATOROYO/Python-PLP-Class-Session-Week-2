# A list of three numbers
numbers = [1,2,3]
print(numbers)

# Empty list
my_list = []
print(my_list)

# List with mixed data types
my_list2 = [1, "hello", 3.4]
print(my_list2)

# Access Python List Elements
languages = ["Python", "Swift", "C++"]
print(languages[0])
print(languages[2])

# Slicing of a Python List
print(languages[-1])

# Listi slicing in python
my_lists = ['p','r','o','g','r','a','m','i']

# items from index 2 to index 4
print(my_lists[2:5]) #Output: ['o', 'g', 'r']

# items from index 5 to end
print(my_lists[5:]) # Output: ['a', 'm', 'i', 'z']

# items begining to end
print(my_lists[:]) # Output: ['p','r','o','g','r','a','m','i']

# Access item at index 2
print(languages[-3]) # Output: Python

# / Add Elements to a Python List //
my_numbers = [21, 34, 54, 12]
print("Before Append:", my_numbers)

# Using append method
my_numbers.append(32)
print("Afte Append:", my_numbers)

# Output
# Before Append: [21,34,54,12]
# After Append: [21,34,54,12,32]
