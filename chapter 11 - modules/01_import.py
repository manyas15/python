# import in pyhton is used to load code from python module into current script
# import statement followed by name of the module

# import pandas
# import math  -> more mathematical functions like sqrt()
# from keyword      -> from math import sqrt, pi
# like if we want to import only 1-2 functions

# from math import *    -> imports everything from math



# as keyword
# import math as m
# to write in short form
# eg -  result = m.sqrt(9) * m.pi


# dir function
# built in function
# we use it to view the names of all functions and variables defined in a module
# import math
# print(dir(math))


# we can also import functions from another file
# like we made a file manya.py and there we have written
# def wlcm():
#     print("you are wlcm")
# manya = "a good girl"

# to import this
# from manya import wlcm, manya
# wlcm()
# print(manya)
# to import every file from manya
# from manya import *



# if we write import manya as m
# then we have to write
# m.wlcm()
# print(m.manya)