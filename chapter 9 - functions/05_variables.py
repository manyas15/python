# var is a named location in memory that stores a value
# in python we assign values to a variable using assignment operator =

# there are 2 types of this
# local and global

# local is the variable that we define within the function and is only accessible within that function
# it is created when the func is called and destroyed when the func returns
# global is the variable that we define outside the function and is accessible from within any func in your code

x = 4
print(x)   # now this is global as they are not in any function

def hello():
    y = 5
    print("local var is " , y)
    print("hello")

# print(f"the local x is {y}")  # this will give error
hello()

print(f"the global x is {x}")  # here 4


def hy():
    a = 5
    global x
    x = 7
    print(a)

print(x)   # now this will print 7 not 4

