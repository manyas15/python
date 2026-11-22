# os module
# it is a built in module
# things that you do manually can be automated

# if we want to delete anything automatically a named 1.py or 1.jgp anything
# this can be done using os


import os

if(not os.path.exists("data")):
    os.mkdir("data")
# this means if the directory does not exist it will create the directory

for i in range(0,100):
    os.mkdir(f"data/Day{i + 1}")

# to rename all files together
for i in range(0,100):
    os.mkdir(f"data/Day{i + 1}" , f"data/Tutorial{i + 1}")
