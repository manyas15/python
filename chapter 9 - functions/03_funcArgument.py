# a function can accept some value it can work with
# we can put these values in parentheses

def goodDay(name , ending):                      # here name is a parameter
    print("Good day, " + name)
    print(ending)

goodDay("Manya" , "Thank you")       # we have passed manya as a name which came inside a variable
goodDay("Dhriti" , "Thank you")
goodDay("A" , "Thank you")           # this way we can add 2 parameters

# these are functions with arguments



def goodDay(name , ending):
    print("Good day, " + name)
    print(ending)
    return "done"               # means function take a value with him and whatever variable ask give it to it

a = goodDay("Manya" , "Thanks")
print(a)
# the string will be returned in a as done