# multiple if statements
a = int(input("Enter number: "))

if(a % 2 == 0):
    print("Even number")

# here we can see after this if no else statement is there
# so upper if statement will be executed independently 
# and lower if statement independently
if(a >= 18):
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")
