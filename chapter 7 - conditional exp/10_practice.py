# find whether a given name is present in a list or not

l = ["john", "jane", "doe", "smith", "alice"]
name = input("Enter name: ")

if(name in l):
    print("name is present in the list")
else:
    print("name is not present in the list")


# if we write John then it will return name is not present in the list 
# because it is case sensitive

# we can use "in" keyword in list as well in strings
# to check if a substring or element is present in a string or not / list or not