# Create a dictionary in Python
capital_city = {"Nepal": "Kathmandu", "Italy": "Rome", "England": "London"}
print(capital_city)

# Dictionaries with keys and values
numbers = {1: "One", 2: "Two", 3: "Three"}
print(numbers)

# Add Elements to python dictionaries
print("Initial Dictionary: ", capital_city)
capital_city["South Sudan"] = "Juba"
print("Updated Dictionary: ", capital_city)

# Change value of Dictionary
student_id = {111: "Eric", 112: "Kyle", 113: "Peni"}
print("Initial Dictionary: ", student_id)
del student_id[111]
print("Updated Dictionary: ", student_id)

# Dictionary Membership test
squares = {1: 1, 3: 9, 5: 25, 7:49, 9:81}
# Output: True
print(1 in squares) # prints True
print(2 not in squares) # prints True
print(49 in squares) # prints False

# Iterating through a Dictionary
for i in  squares:
    print(squares[i])

