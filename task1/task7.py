import os

file_name = "topics.txt"
topics = ["Variables", "Conditions", "Loops", "Functions", "Files"]

with open(file_name, "w" , encoding="utf-8") as file:
    for item in topics:
        file.write(item + "\n")

with open(file_name , "r" , encoding="utf-8") as file:
    lines = file.readlines()
    for i,line in enumerate(lines,1):
        print(f"{i}) {line.strip()}")








