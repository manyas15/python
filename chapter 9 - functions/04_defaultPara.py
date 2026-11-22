# we can have a value as default argument in a function
# like if we specify name like "manya" in the line containing def
# this value is used when no argument is passed

def greet(name, ending = "thank you"):
    print("have a good day " + name)
    print(ending)

greet("manya" , "thanks")
greet("dhriti")