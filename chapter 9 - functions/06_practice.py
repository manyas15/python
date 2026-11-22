# find greatest of 3 numbers
a = 4
b = 5
c = 6

def greatest():
    if(a > b and a > c):
        return a
    elif(b > a and b > c):
        return b
    else:
        return c

print(greatest())



# covert celsius to fahrenheit
def f_to_c(f):
    return 5*(f-32)/9

f = int(input("enter temp in F"))
print(f_to_c(f) , 2)  # round off to 2 decimal places



# to avoid printing in another line
print("a")
print("b")
print("c", end="")
print("d", end="")