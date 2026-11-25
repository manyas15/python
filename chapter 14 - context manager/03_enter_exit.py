# Creating Custom Context Managers
# Now let's understand the second learning objective.

# Python also allows us to create our own context managers.

# For this, we use two special methods:
# - __enter__()
# - __exit__()
# These are called dunder methods (double underscore methods).
# Important: These methods are used inside classes.

# A. __enter__() method
# It runs when Python enters the with block.
# Its job is to perform setup work and optionally return a value.

# B. __exit__() method
# It runs when Python leaves the with block.
# Its job is to perform cleanup work, such as:
# - Closing a resource.
# - Releasing a lock.
# - Disconnecting a connection.
# - Cleaning temporary files.


# Example: Custom context manager
class MyContext:

    def __enter__(self):
        print("Entering the context")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting the context")


with MyContext():
    print("Inside the with block")

# with MyContext() -> Python creates the context manager.

# __enter__() executes -> Prints "Entering the context".

# Inside the with block -> Prints "Inside the with block".

# __exit__() executes -> Prints "Exiting the context".

# What are exc_type, exc_value, and traceback?
# These are the three arguments received by __exit__().
# Argument	   Meaning
# exc_type	   Type of exception that occurred
# exc_value	   Actual exception message or object
# traceback	   Information about where the exception occurred

# If no exception occurs, all three are None.