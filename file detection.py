# file in same location (outside folder) in pycharm

import os
file_path = "test.txt"

if os.path.exists(file_path):
    print(f"The location {file_path} exists ")
else:
    print("Does not exists ")

    
# file in different directory or folder in pycharm

import os
file_path = "stuff/test.txt"

if os.path.exists(file_path):
    print(f"The location {file_path} exists ")
else:
    print("Does not exists ")


# file in our PC not in pycharm \\ or / both slash works

import os
file_path = "C:\\Users\\Admin\\Desktop\\test.txt"

if os.path.exists(file_path):
    print(f"The location {file_path} exists ")
else:
    print("Does not exists ")



#file not a drectory(folder)
import os
file_path = "C:\\Users\\Admin\\Desktop\\test.txt"

if os.path.exists(file_path):
    print(f"The location {file_path} exists ")

    if os.path.isfile(file_path): #file not a drectory
        print("That is a file")
else:
    print("Does not exists ")



#directory (folder) not a file 

import os
file_path = "C:\\Users\\Admin\\Desktop\\test"

if os.path.exists(file_path):
    print(f"The location {file_path} exists ")

    if os.path.isfile(file_path): #file not a drectory
        print("That is a file")
    elif os.path.isdir(file_path):
        print("That is a directory")
else:
    print("Does not exists ")
