# dictionary is a collection of key-value pairs
# it is unordered
# it is mutable
# it is indexed by keys
# it cannot have duplicate keys

d = {} # empty dictionary
marks = {
    "Manya" : 100,
    "Dhriti" : 90,
    "list" : [1, 2, 3],
    "a" : "100"
}
print(marks)

# we cant write print(marks[0]) because it is not indexed by numbers but by keys
# instead we can write print(marks["Manya"]) to get the value of Manya's marks

print(marks["Manya"]) # prints 100