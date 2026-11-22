# function is a group of statements performing a specific task

# when program gets bigger in size
# complexity increases
# to keep track on each piece of code we use function


# function can be reused by the programmer

# write a function to find the average
# a = 12
# b = 45
# c = 56
# average = (a + b + c) / 3
# print(average)
# to avoid solving this again and again for diff number
# we can give this piece of code a name that is function

# this is function definition
def avg():
    a = int(input("enter: "))
    b = int(input("enter: "))
    c = int(input("enter: "))

    average = (a + b + c) / 3
    print(average)

avg()
avg()
# this is function call
# you can call this function any number of times