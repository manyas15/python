# Multiple except blocks
# What if your code can generate different types of errors?

# You can use multiple except blocks.

try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

except ZeroDivisionError:
    print("Cannot divide by zero!")

except ValueError:
    print("Please enter valid numbers!")

except TypeError:
    print("Invalid data type!")

else:
    print("Result:", a / b)
    print("No error occurred!")

finally:
    print("Program execution completed!")
# The finally block
# The finally block executes whether an exception occurs or not.

