
# reading a txt file
file_path = "C:/Users/Admin/desktop/input/txt"

try:
    with open(file_path,"r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("balle balle not found")
except PermissionError:
    print("yashu ko permission ni h")


# reading a json file
import json
file_path = "C:/Users/Admin/desktop/output.json"

try:
    with open(file_path,"r") as file:
        content = json.load(file)
        print(content)
        print(content["name"])
except FileNotFoundError:
    print("balle balle not found")
except PermissionError:
    print("yashu ko permission ni h")



# reading a csv file
import csv
file_path = "C:/Users/Admin/desktop/output.csv"

try:
    with open(file_path,"r") as file:
        content =csv.reader(file) #gives memory address
        for line in content:
            print(line)
            print(line[1])

except FileNotFoundError:
    print("balle balle not found")
except PermissionError:
    print("yashu ko permission ni h")
