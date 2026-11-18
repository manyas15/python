# ques - greet the person on list whose name starts with "S"

l = ["Sam", "John", "Steve", "Alice", "Bob"]

for name in l:
    if(name.startswith("S")):
        print("Hello", name)