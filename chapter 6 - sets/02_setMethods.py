s = set()
s = {1, 3, 4, 32, 5, 5, "Harry"}
print(s)   # will also print harry

# add method
s.add(6)
print(s)


# copy
s1 = s.copy()
print(s1)

# difference
s2 = {1, 2, 3, 4, 5}
print(s.difference(s2))  # will print the difference between s and s2



# operations that we can use in set
# len
print(len(s))  # will print the length of the set

# remove
s.remove(3)  # will remove 3 from the set
print(s)


# pop
s.pop()  # will remove a random element from the set
print(s)


# union
s3 = {7, 8, 9}
print(s.union(s3))  # will print the union of s and s3


# intersection
print(s.intersection(s2))  # will print the intersection of s and s2


# clear
#s.clear()
# will print set() after clear


# subset
print(s.issubset(s2))  # will print True if s is a subset of s2

# superset
print(s.issuperset(s2))  # will print True if s is a superset of s2

