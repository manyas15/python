friends = ["Apple", "Orange", 5, 5.5, True]
print(friends)

friends.append("Mango")      # adding an element to the end of the list
print(friends)

a = [1,34,56,2,7]
a.sort()      # sorting the list in ascending order
print(a)

b = [1,34,56,2,7]
b.reverse()     # reversing the list
print(b)

c = [1,34,56,2,7]
c.insert(2, 100)      # inserting an element at index 2
print(c)

d = [1,34,56,2,7]
# d.pop()      # removing the last element from the list
d.pop(2)      # removing the element at index 2
print(d)