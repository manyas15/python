# set is a collection of non -repetitive elements.
# It is unordered and unindexed.
# Sets are mutable.

# like
s = {1, 2, 3, 4, 5}

# to make empty set we have to use set() function
# dont use empty = {} -> this will create empty dictionary not set

empty = set()

print(type(s))


# a set will take every value only once
# like if s = {1,4,6,1,1,1}
# after print(s) -> it will print {1,4,6}

# when we need order we use list
# like if s = {1,5,3,3,7}
# in list it will print [1,3,3,5,7] but in set it will print {1,5,3,7} but not in order
# and when we dont want to repeat elements we use set