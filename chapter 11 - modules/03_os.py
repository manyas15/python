import os

folders = os.listdir("data")
print(folders)

# to print vertically
for folder in folders:
    print(folder)
    print(os.listdir(f"data/{folder}"))  # to print any folder within folder


# to see in which directory you are then use
print(os.getcwd)
# to change the directory
os.chdir("/users")
# now after printing it will be changed
print(os.getcwd())


# to delete a file
# os.remove()

# to remove an empty directory
# os.rmdir()

# to delete a dic and all its contents
# shutil.rmtree()


# to study for other methods google it
