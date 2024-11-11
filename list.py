# A list of three numbers //
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

# 1. Using append method
my_numbers.append(32)
print("Afte Append:", my_numbers)

# Output
# Before Append: [21,34,54,12]
# After Append: [21,34,54,12,32]

prime_numbers = [2,3,4]
print("List1:", prime_numbers)

even_numbers = [4,6,8]
print("List2:", even_numbers)

# join two lists
prime_numbers.extend(even_numbers)
print("List after append:", prime_numbers)

# Output
# List1: [2,3,5]
# List2: [4,6,8]
# List after append: [2,3,5,4,6,8]

# Change List Items //
# changing the third item to C
languages[2] = 'C'
print(languages) # ['Python', 'Swift', 'C']


# / Remove an Item From a List //
my_languages = ['Python', 'Swift', 'C++', 'C', 'Java', 'Rust', 'R']

# Deleting the second item
del my_languages[1]
print(my_languages) # ['Python', 'C++', 'C', 'Java', 'Rust', 'R']

# Deleting the last item
del my_languages[-1]
print(my_languages) # ['Python', 'C++', 'C', 'Java', 'Rust']

# Delete first two items
del my_languages[0:2] # ['C', 'Java', 'Rust']
print(my_languages)

# 2. Using remove()
# Remove python fromthe list
languages.remove("Python")
print(languages)

# Iterating through a list
for language in languages:
    print(language)
    
# Output
# Python
# Swift
# C++

# Python List Comprehsion
numbers_compress = [number*number for number in range(1,6)]
print(numbers_compress)
# Output: [1,4,9,16,25]