import os

file_name = "student_note.txt"

with open(file_name , "w" ,encoding="utf-8") as file:
        file.write("Hasan Omar\n")
        file.write("50/2\n")
        file.write("I am learning file handling in Python.\n")
        print("File has been created")


