# A context manager is a feature in Python that helps us manage resources automatically.

# Resources are things that we use temporarily in a program, such as:
# - Files
# - Database connections
# - Network connections
# - Locks in multithreading
# For example, suppose you open a file, read its contents, and finish your work. You must close the file afterward.

# If you forget to close it, it can cause problems, such as wasting system resources.

# A context manager handles this cleanup automatically.

# Simple meaning: A context manager takes care of setting something up before work and cleaning it up afterward.


# The with statement
# Python uses the with statement to work with context managers.
# Let's first see how we normally open and close a file.

# Without with:
file = open("demo.txt", "r")

content = file.read()
print(content)

file.close()

# Here:
# 1. We open the file.
# 2. We read its contents.
# 3. We manually close the file.
# What if an error occurs before file.close()?

# The file might remain open.

# With with:
with open("demo.txt", "r") as file:
    content = file.read()
    print(content)

# Now Python automatically closes the file when the with block finishes, even if an exception occurs inside it.

# Important
#  You don't need to write file.close() when using with.