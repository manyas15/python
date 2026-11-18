# program to write dictionary of hindi with values as their english traslation
dictionary = {
    "haan" : "yes",
    "nahi" : "no"
}

dict = input("Enter hindi word: ")
print(dictionary[dict])


# program to input 8 numbers and display all unique numbers(once)

s = set()

n = input("Enter number 1: ")
s.add(int(n))         # adding number in int

n = input("Enter number 2: ")
s.add(int(n))

n = input("Enter number 3: ")
s.add(int(n))

n = input("Enter number 4: ")
s.add(int(n))

n = input("Enter number 5: ")
s.add(int(n))

n = input("Enter number 6: ")
s.add(int(n))

n = input("Enter number 7: ")
s.add(int(n))

n = input("Enter number 8: ")
s.add(int(n))
print(s)  # will print all unique numbers