import os

file_name = "diary.txt"
while True:
    print("Choose an option")
    print("1 - Add diary entry")
    print("2 - Show all diary entries")
    print("3 - Delete diary file")
    print("4 - Exit")

    option = input("Enter Option:")

    if option == "1":
        diary = input("Enter diary name:")
        with open(file_name , "a" , encoding = "utf-8") as file:
            file.write(diary + "\n")
            print("Added Diary Entry")

    elif option == "2":
        if os.path.exists(file_name):
            with open(file_name , "r" , encoding = "utf-8") as file:
                content = file.read()
                if(content):
                    print(content)
                else:
                    print("Diaries are empty")
        else:
            print("File not found")

    elif option == "3":
        if os.path.exists(file_name):
            os.remove(file_name)
            print("File has been deleted successfully")
        else:
            print("File not found")

    elif option == "4":
        break



