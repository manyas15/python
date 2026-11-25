# Types of Common Exceptions in Python
# Python has different types of built-in exceptions.

# 1. ZeroDivisionError
# Occurs when you divide a number by zero.
a = 10
b = 0
print(a / b)



# 2. ValueError
# Occurs when the value is of the correct type but is not valid for the operation.
num = int("hello")
# You cannot convert "hello" into an integer.


# 3. TypeError
# Occurs when an operation is performed on incompatible data types.
a = 10
b = "Hello"
print(a + b)
# You cannot directly add an integer and a string.


# 4. IndexError
# Occurs when you try to access an index that doesn't exist.
numbers = [10, 20, 30]
print(numbers[5])
# The list has indexes 0, 1 and 2. Index 5 doesn't exist.


# 5. KeyError
# Occurs when you try to access a dictionary key that doesn't exist.
student = {
    "name": "Manya",
    "age": 22
    }
print(student["marks"])

# The key "marks" doesn't exist.


# NameError ->	Variable not defined
# FileNotFoundError ->	File doesn't exist
# ImportError ->  Import operation fails