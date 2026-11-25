# Scenario	              What the context manager does
# File management	      Closes files automatically
# Database management	  Handles transactions or connection cleanup
# Lock management	      Releases locks automatically
# Temporary files	      Deletes temporary files after use
# Timer	                  Starts a timer on entry and calculates execution time on exit



# For example, imagine you want to calculate how much time a piece of code takes.

# A custom context manager could:
# 1. Start the timer in __enter__().
# 2. Execute your code inside with.
# 3. Calculate and print the time in __exit__().
# This makes your code cleaner and avoids repeating setup and cleanup logic.




# Quick revision: Important points
# Concept	               Remember
# Context Manager	       Manages resources automatically
# with	                   Used to work with a context manager
# __enter__()	           Runs at the beginning
# __exit__()	           Runs at the end
# open()	               Built-in example of a context manager
# exc_type	               Exception type
# exc_value	               Exception details
# traceback	               Error location information


# One important interview question:
# What is the main advantage of using a context manager?
# Answer: It ensures proper resource management
# by automatically handling setup and cleanup, even when an exception occurs.