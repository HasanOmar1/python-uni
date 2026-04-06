import os

file_name = "student_note.txt"

if os.path.exists(file_name):
    with open(file_name , "a" ,encoding="utf-8") as file:
        file.write("Today's topic: Working with files\n")
        file.write("Python is useful for handling data\n")

    with open(file_name , "r" , encoding="utf-8") as file:
        content = file.read()
        print(content)


