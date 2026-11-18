# can you change the values inside a list which is contained in set
s = {1, 2, 3, [4, 5]}  # will give error because list is mutable and set can only contain immutable elements

s = {1, 2, 3, (4, 5)}  # will not give error because tuple is immutable and set can contain immutable elements