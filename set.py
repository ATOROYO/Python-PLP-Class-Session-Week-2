# Create a set of interger type
student_id = {112, 114, 116, 118, 115}
print("Student ID: ", student_id)

# Create a set of string type
vowel_letters = {'a', 'e', 'i', 'o', 'u'}
print("Vowels Letters: ", vowel_letters)

# Create a set of mixed data type
mixed_set = {'Hello', 101, -2, 'Bye'}
print("Set of mixed data types: ", mixed_set)

# / Create an empty Set in Python
# Empty set
empty_set = set()

# Empty dictionary
empty_dictionary = {}

print("Data type of empty _set: ", empty_set)
print("Data type of empty_dictionary", empty_dictionary)

# Add and Update in Python
numbers = {21, 34, 54, 12}
print("Initial Set: ", numbers)
# using add() method
print("Update set: ", numbers)

# Update Python Set
companies = {'Lacoste', 'Ralph Lauren'}
tech_companies = ['apple', 'google', 'apple']
companies.update(tech_companies) # Output: {'google', 'apple', 'Lacoste', 'Ralph Lauren'}

# / Remove an element from a list
languages = {'Swift', 'Java', 'Python'}
print("Initial Set: ", languages)
# remove 'Java' from a set
print("Set after remove(): ", languages)

# / Built in function with set
# Iterate Over a Set in Python
fruits = {"Apple", "Peach", "Mango"}
# for Loop to access each fruits
for fruit in fruits:
    print(fruit)
    
# Find Number of Set Elements
even_numbers = {2,4,6,8}
print("Set:", even_numbers)
# find number of elements
print("Total Elements: ", len(even_numbers))
# Output
# Set: {8,2,4,6}
# Total Elements: 4

# / Python Set Operation
# union of two sets
A = {1, 3, 5}
B = {0, 2, 4}
# perform union operation using |
print("Union using |: ", A | B)
# perform union operation using union()
print("Union usning union(): ", A.union(B))

# set intersection
# perform intersection operation using &
print("Intersection using &: ", A & B)
# perform intersection operation using intersection()
print("Intersection using intersection(): " A.intersection(B))

# difference between Two Sets
# perform defference operation using -
print("Difference using -: ", A - B)
# perform defference operation using difference()
print("Difference using difference(): ", A.difference(B))

# set symmetric difference
# perform defference operation using ^
print("using ^: ", A ^ B)
# perform defference operation using symmetric_difference()
print("using symmetric_difference(): ", A.symmetric_difference(B))

# check if two sets are equal
# perform difference operation using ==
if A == B:
    print("Set A and B are equal")
else:
    print("Set A and B are not equal")
