import os

file_name = "backup_note.txt"

if os.path.exists(file_name):
    os.remove(file_name)
    print("File has been deleted")
else:
    print("File not found")








