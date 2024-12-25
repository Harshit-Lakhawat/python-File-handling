#write in python file 

txt_data = "i like pizza"

file_path = ("output.txt")

with open(file =file_path,mode ="w") as file:
    file.write(txt_data)
    print(f"txt file {file_path} was created ")



#write in python file on diff loc
txt_data = "i like pizza"

file_path = ("C:/Users/Admin/Desktop/output.txt")

with open(file =file_path,mode ="w") as file:
    file.write(txt_data)
    print(f"txt file {file_path} was created ")


#write in list in python file on diff loc
txt_data = "i like pizza"

employees = ["harshit","abc","vaibhav","shubhankar"]

file_path = ("C:/Users/Admin/Desktop/output.txt")

try:
    with open(file =file_path,mode ="w") as file:
        for employee in employees:
            file.write(employee + " ")
        print(f"txt file {file_path} was created ")
except FileExistsError:
    print("that file already exists!")



#write json file on diff loc
import json

employee = {
    "name" : "harhsit",
    "age" : 18,
    "job" : "manager"
}

file_path = ("C:/Users/Admin/Desktop/output.json")

try:
    with open(file =file_path,mode ="w") as file:
        json.dump(employee, file , indent = 4)
        print(f"json file {file_path} was created ")
except FileExistsError:
    print("that file already exists!")


#write csv file on diff loc
import json
import csv

employees = [["name", "age", "job"],
            ["harshit",18,"manager"],
            ["vaibhav",22,"airforce"],
            ["shubhankar",22,"navy"]]

file_path = ("C:/Users/Admin/Desktop/output.csv")

try:
    with open(file =file_path,mode ="w",newline = "") as file:
        writer = csv.writer(file)
        for row in employees:
            writer.writerow(row)
        print(f"csv file {file_path} was created ")
except FileExistsError:
    print("that file already exists!")
