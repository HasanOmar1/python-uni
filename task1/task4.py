import os

file_name = "student_note.txt"

if os.path.exists(file_name):
    with open(file_name , "r" , encoding="utf-8") as file:
        content = file.read()
        number_of_lines = len(content.splitlines())
        number_of_words = len(content.split())
        number_of_characters = len(content)
        print("Number of lines: ", number_of_lines)
        print("Number of words: ", number_of_words)
        print("Number of characters: ", number_of_characters)


