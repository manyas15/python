# exception handling
# An exception is an error that occurs while a program is running and interrupts its normal execution.

# like
# a = 10
# b = 0

# print(a / b)

# print("Program completed")

# output is -> ZeroDivisionError: division by zero

# What is a Runtime Exception?
# A runtime exception is an error that occurs while a program is executing.

a = 10
b = 0

result = a / b

print("Hello")

# Here, the code has no syntax error. Python understands the code, but when it tries to divide 10 by 0, it encounters a ZeroDivisionError.
# The program stops before printing "Hello".



# What happened?
# - Python tried to divide 10 by 0.
# - Dividing a number by zero is not allowed.
# - Python raised an exception.
# - The program stopped before printing "Program completed".
# Exception handling allows us to handle such errors so that our program doesn't terminate unexpectedly.

# - try – Contains code that might generate an error.
# - except – Handles the error if it occurs.


n = int(input("Enter a number: "))

try:
    for i in range(1 , 11):
        print(f"{n} x {i} = {n * i}")
# if anyone wants to anything else instead of number then we can use this
except Exception as e:
    print("invalid input")