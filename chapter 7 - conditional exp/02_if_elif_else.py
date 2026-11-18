# if-elif-else ladder
# -> used to check multiple conditions
a = int(input("Enter a age: "))

if(a >= 18):
    print("You are eligible to vote")
elif(a<0):
    print("invalid age")
elif(a == 0):
    print("invalid age 0")
else:
    print("You are not eligible to vote")

print("end")

# if one condition matches other are ignored

# elif statements can be multiple but else statement can be only one and it is optional

# last else statement is executed when all the above conditions are false