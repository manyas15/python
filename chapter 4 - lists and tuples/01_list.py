# List is container to store a set of values of any data type.
friends = ["Apple", "Orange", 5, 5.5, True]       # different data types can be stored in a list
print(friends[0])

# you can change the elements in list , lists are mutable
# you can add, remove, or change elements in a list in any way you want.

friends[0] = "Banana"      # changing the first element of the list
print(friends[0])
print(friends) 
print(friends[1:4])    # slicing the list to get elements from index 1 to 3