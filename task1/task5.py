import os

file_name = "student_note.txt"
back_up_name = "backup_note.txt"

if os.path.exists(file_name):
    with open(file_name , "r" , encoding="utf-8") as file:
        with open(back_up_name , "w" , encoding="utf-8") as back_up_file:
            back_up_file.write(file.read())
            print("Back up created successfully")



