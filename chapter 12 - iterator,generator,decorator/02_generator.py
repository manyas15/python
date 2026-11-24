# generators - Generating values when needed
# A generator is a function that uses the yield keyword instead of just return.

def gen(n):
    for i in range(n):
        yield i

print(gen(10000000))

# now instead of printing all numbers upto 1 crore as it uses too much ram
# this simply store it in an object
# <generator object gen at 0x000001A306199A40>
# now whenever we call a func like

for i in gen(10000):
    print (i)

# Numbers are generated only when required.
# This makes generators useful for large amounts of data.
# Remember: Generator = Function + yield + One value at a time.

# we have already used a ram above while storing 1 crore using yield
# so after running this fun no extra ram is used


# in this function
def my_numbers():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5


for num in my_numbers():
    print(num)

# this will print every number 1 to 5

# but in case if we use return here like
def add():
    return 10
    return 20

print(add())
# this will only print 10
# Because return ends the function immediately.

# The difference:
# - return gives a result and finishes the function.
# - yield gives a result but pauses the function. It can continue from where it stopped.

