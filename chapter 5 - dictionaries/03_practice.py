# create an empty dictionary and add friends to enter their favourite language as value
# and use key as their name and print the dictionary
d = {}

name = input("Enter friends name : ")
lang = input("Enter language name: ")
d.update({name : lang})

name = input("Enter friends name : ")
lang = input("Enter language name: ")
d.update({name : lang})

name = input("Enter friends name : ")
lang = input("Enter language name: ")
d.update({name : lang})

print(d)

# if 2 names means key(identifier) are same then it will print the latest one like one the we put at last
# this is because of update

# but if languages means values are same then it will for both