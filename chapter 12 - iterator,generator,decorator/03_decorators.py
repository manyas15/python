# Decorators – Adding extra functionality to a function

# Suppose you have a function:
# def greet():
#       print("Hello!")

# When you call it:
# greet()

# Output:
# Hello!


# Now suppose you want to print something before and after this function executes.

# You could change the function itself:
# def greet():
#        print("Starting...")
#        print("Hello!")
#        print("Finished!")


# But what if you have 100 functions and want to add the same functionality to all of them?

# Instead of modifying every function, Python gives us Decorators.

# A decorator adds extra functionality to an existing function without changing its original code.
# Let's understand with an example

def my_decorator(func):         # my_decorator – The decorator function.
    def wrapper():              # wrapper – A function that adds extra functionality.
        print("Starting function")
        func()                  # func – The original function that we want to decorate.
        print("Ending function")
        return wrapper          # Returns the new function with additional behaviour.

@my_decorator
def greet():
    print("Hello!")

greet()

# Output:
# Starting function
# Hello!
# Ending function