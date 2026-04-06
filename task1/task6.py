import os

file_name = "student_note.txt"

if os.path.exists(file_name):
    with open(file_name , "r" , encoding="utf-8") as file:
        content = file.read()
        updated_content = content.replace("learning" , "practicing")

        with open(file_name, "w" , encoding="utf-8") as file:
            file.write(updated_content)
            print(updated_content)





