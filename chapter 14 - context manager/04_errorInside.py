# What happens if an error occurs inside a custom context manager?
# Let's understand with an example:
class MyContext:

    def __enter__(self):
        print("Start")

    def __exit__(self, exc_type, exc_value, traceback):
        print("Cleanup")
        return False


with MyContext():
    print(10 / 0)

# Output
# Start
# Cleanup
# ZeroDivisionError

# The important thing is:

# Even when an error occurs inside the with block, __exit__() still executes.

# return False means Python should not suppress the exception. It will continue propagating normally.

# If __exit__() returns True, it tells Python that the exception has been handled, so Python suppresses it.