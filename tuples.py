# Creating a Python Tuple With one Element
var1 = ("hello")
print(type(var1)) # <class 'str'>

# Creating a tuple having one element
var2 = ("hello")
print(type(var2)) # <class 'tuple'>

# Parenthesis is optional
var3 = "hello"
print(type(var3)) # <class 'tuple'>

# 1. Indexing
letters = ("p","r","o","g","r","a","m","i","z")
print(letters[0]) # prints p
print(letters[5]) # prints a

# 2. Negative indexing
print(letters[-1]) # prints z
print(letters[-3]) # prints m

# Python Tuple Method
my_tuple = ("a","p","p","l","e")
print(my_tuple['p']) # Prints 2