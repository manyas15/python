# count
a = (1, 4, 7, 67, False, "Hello")
print(a.count(4)) # count the number of occurrences of 4 in the tuple


# index
print(a.index(7)) # find the index of the first occurrence of 7 in the tuple

# always a new tuple is created when we perform operations on a tuple
# since tuples are immutable.



# operations
# concatenation
b = (1, 2, 3)
c = (4, 5, 6)
d = b + c # concatenating two tuples
print(d)


# repetition
e = (1,2,3)
repeat = e * 3
print(repeat) # repeating the tuple 3 times


# membership  - 'in' operator
f = (1, 2, 3, 4, 5)
print(2 in f) # checking if 2 is in the tuple
# will return True if 2 is in the tuple, otherwise False


# len()
g = (1, 2, 3, 4, 5)
print(len(g)) # getting the length of the tuple


# min and max
h = (1, 2, 3, 4, 5)
print(min(h))
print(max(h)) # getting the minimum and maximum values in the tuple


# slicing
i = (1, 2, 3, 4, 5)
print(i[1:4]) # slicing the tuple from index 1 to 3 (


# unpacking
j = (1, 2, 3)
a, b, c = j # unpacking the tuple into variables
print(a)
print(b)
print(c)
# or print(a, b, c)


# function
# sum
k = (1, 2, 3, 4, 5)
print(sum(k)) # getting the sum of all elements in the tuple