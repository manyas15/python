# Iterator - an object that returns elements one at a time from a seq (or data stream)
# it remembers its position between calls

# in easy language An iterator is an object that allows you to access elements one by one instead of accessing all elements at once.


# a python object is iterator if it has:
# __iter__() -> returns the iterator object itslef
# __next__() -> return the next item in seq


# For example, when you use a for loop over a list, Python internally uses an iterator.

# Normal iteration
numbers = [10, 20, 30, 40]

for num in numbers:
    print(num)

# Python internally gets an iterator from the list.


# like in this
fruits = ["Apple", "Mango", "Banana"]

x = iter(fruits)      # Creates an iterator from an iterable (like a list).

print(next(x))
print(next(x))
print(next(x))

# next() call 1  Apple
# next() call 2  Mango
# next() call 3  Banana

# What if you call next() for the fourth time?
# print(next(x))

# You get StopIteration because there are no more elements.