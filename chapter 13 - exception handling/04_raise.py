# Sometimes you want to generate an exception yourself when a particular condition is not satisfied.

# For that, Python provides the raise keyword.

age = 15
if age < 18:
    raise ValueError("You must be 18 or older!")
print("Access granted")

# Output:
# ValueError: You must be 18 or older!


# Here:
# - We checked whether the age is below 18.
# - If yes, raise generates a ValueError.
# - The program stops unless the exception is handled.

# Another example:
try:
    age = 15
    if age < 18:
        raise ValueError("Not eligible")
except ValueError as e:
    print(e)

# Output:
# Not eligible

# e stores the exception object, allowing us to print its error message.