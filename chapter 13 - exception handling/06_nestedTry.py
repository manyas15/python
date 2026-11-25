# What are Nested Try Blocks?
# A nested try block means writing one try-except block inside another try-except block.
# In simple words, a try block inside another try block is called a nested try block.
# We use it when we want to handle different errors at different levels of our program.

try:
    print("Outer try block started")

    try:
        a = 10
        b = 0

        print(a / b)

    except ZeroDivisionError:
        print("Inner except: Cannot divide by zero")

    print("Outer try block completed")

except Exception:
    print("Outer except: Something went wrong")


# What if the inner block cannot handle the exception?
# Python will look for a matching exception handler in the outer try-except block.


# Why do we use Nested Try Blocks?
# Imagine an application where:
# - Outer try handles database-related operations.
# - Inner try handles file reading.
# - Another inner try handles data conversion.
# This allows you to handle errors separately rather than putting everything into one large exception handler.

# However, don't use nested try blocks unnecessarily. Keep your code simple and readable.