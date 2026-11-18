import os 

#specify the directory path you want to list
directory_path = '/'

# use the os module to list the directory content
contents = os.listdir(directory_path)

#print contents of directory
# for item in contents:
#     print(item)
# use the above method or just write

print(contents)