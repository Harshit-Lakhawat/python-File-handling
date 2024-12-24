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
