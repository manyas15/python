# ques 1 - enter name and date using input function
name = input("Enter your name: ")
print("Goodafternoon, " + name)
# or u can use f-string
print(f"Goodafternoon, {name}")


# ques 2 - we have to fill a template with name and date like in this ques
letter = '''Dear <|NAME|>,
You are selected for the job. Congratulations!
Date: <|DATE|>'''
print(letter.replace("<|NAME|>", "Manya").replace("<|DATE|>", "20/06/2024"))
# in this we have first replaced the name and then in that string we have replaced the date using the replace() method.


# ques 3 - write a program to detect double spaces in a string.
string = "I am  a good  girl"
print(string.find("  "))


# ques 4 - replace double space with single space 
space = "Hello  world"
print(space.replace("  ", " "))
print(name)      # -> this will print Hello  world as string is immutable
# when we used replace function a new string was created with single space but the original string remained unchanged.
