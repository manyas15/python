marks = {
    "Manya" : 100,
    "Dhriti" : 90,
    "list" : [1, 2, 3],
    "a" : "100"
}


print(marks.items())
# prints all the items in the dictionary as a list of tuples
# dict_items([('Manya', 100), ('Dhriti', 90), ('list', [1, 2, 3]), ('a', '100')])


print(marks.keys())
# prints all the keys in the dictionary as a list
# dict_keys(['Manya', 'Dhriti', 'list', 'a'])


print(marks.values())
# prints all the values in the dictionary as a list
# dict_values([100, 90, [1, 2, 3], '100'])


marks.update({"Manya" : 95})
# updates the value of Manya's marks to 95
print(marks) # prints the updated dictionary


print(marks.get("Manya"))
# prints the value of Manya's marks using the get() method



# difference between marks["Manya"] and marks.get("Manya")
# is that if the key is not present in the dictionary, marks["Manya"] will raise a KeyError,
# while marks.get("Manya") will return None (or a default value if specified).


# more methods
# dict.clear() - removes all items from the dictionary
# marks.clear()

# dict.copy() - returns a shallow copy of the dictionary
marks_copy = marks.copy()
print(marks_copy)


# dict.fromkeys() - creates a new dictionary with keys from an iterable and values set to a specified value
keys = ['a', 'b', 'c']
new_marks = marks.fromkeys(keys, 0)
print(new_marks) # prints {'a': 0, 'b': 0, 'c': 0}


# dict.pop() - removes the item with the specified key and returns its value
removed_value = marks.pop("Dhriti")
print(removed_value) # prints 90
print(marks) # prints the dictionary after removing Dhriti's marks