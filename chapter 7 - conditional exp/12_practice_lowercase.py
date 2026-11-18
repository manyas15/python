statement = input("Enter a statement: ")

if("Harry".lower() in statement.lower()):
    print("Harry is present")
else:
    print("Harry is not present")

# basically we are converting both the statement and the word "Harry" to lowercase 
# and then checking if it is present or not