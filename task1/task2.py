import os

file_name = "student_note.txt"

if os.path.exists(file_name):
        with open("student_note.txt" , "r" ,encoding="utf-8") as file:
            # content = file.read()
            # print(content)
            # line = file.readline()
            # print(line)

            content_list = file.readlines()
            for line in content_list:
                print(line)
