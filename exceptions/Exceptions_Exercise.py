def ex():

        dict = {}
        while True:
            try:
                student_name = input("Enter your name: ")

                if student_name.strip() == "stop":
                    break
                if student_name.strip() == "":
                    raise ValueError("Student name cannot be empty.")
                if student_name.strip() in dict:
                    raise ValueError("Student name already exists.")
                if student_name.isdigit():
                    raise TypeError("Student name cannot be an integer.")

                grade = input("Enter your grade: ")

                if not grade.isdigit():
                    raise TypeError("Grade must be an integer.")

                grade = int(grade)
                if grade < 0 or grade > 100:
                    raise ValueError("Grade must be between 0 and 100.")

                dict[student_name] = grade

            except ValueError as e:
                print("Value Error: ", e)
            except TypeError as e:
                print("Type Error: ", e)

        if len(dict) == 0:
            print("No Student Data Entered.")
        else:

            for key,value in dict.items():
                print(key, ": ", value)

            avg = sum(dict.values()) / len(dict)
            print("Average: ", avg)
            student_max_grade = max(dict , key=dict.get)
            max_grade = max(dict.values())
            print(f"Highest Grade: {student_max_grade} - {max_grade}")

            # Menu
            while True:
                print("\nMenu:")
                print("1. Show all students")
                print("2. Show average")
                print("3. Search for a student")
                print("4. Exit")

                choice = input("Enter your choice: ").strip()

                try:
                    if choice == "1":
                        if len(dict) == 0:
                            print("No students found")
                        else:
                            print("\nStudents and grades:")
                            for name, grade in dict.items():
                                print(name, ":", grade)

                    elif choice == "2":
                        if len(dict) == 0:
                            print("No students available to calculate average")

                        average = sum(dict.values()) / len(dict)
                        print("Average grade:", average)

                    elif choice == "3":
                        search_name = input("Enter student name to search: ").strip()

                        if search_name not in dict:
                            raise KeyError("Student does not exist")

                        print(search_name, "grade is", dict[search_name])

                    elif choice == "4":
                        print("Exiting program...")
                        break

                    else:
                        raise ValueError("Invalid menu choice")

                except ValueError as e:
                    print("Error:", e)

                except KeyError as e:
                    print("Error:", e)





ex()




