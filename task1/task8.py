import os

file_name = input("Enter file name:")

if os.path.exists(file_name):
    with open(file_name, "w" , encoding="utf-8") as file:
        print("file exists")
else:
    print("File not found")








