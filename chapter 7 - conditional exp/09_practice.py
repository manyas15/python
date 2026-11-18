# find whether the given username contains less than 10 characters or not

u = input("Enter username: ")

if(len(u) < 10):
    print("username is valid")
else:
    print("username is invalid")