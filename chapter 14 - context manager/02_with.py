# How does the with statement work?
with open("demo.txt", "r") as file:
    print(file.read())

# in this syntax
# Part	                    Meaning
# with	                    Starts the context manager
# open()	                Opens the file
# as file	                Stores the opened file in a variable
# Indented block	        Code that uses the resource

# The general syntax is:
# with context_manager as variable:
#     Perform your work