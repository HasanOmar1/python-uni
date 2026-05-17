"""
04_full_example_school_system.py

This file combines several OOP ideas in one larger example:
1. Encapsulation
2. Inheritance
3. Abstract classes
4. Overriding
5. Protected and private attributes

Main teaching goal:
Show students how OOP concepts work together in a more realistic design.
"""

from abc import ABC, abstractmethod


class Person(ABC):
    """
    Abstract base class for people in the school.
    """

    def __init__(self, name, age):
        """
        Create a person.
        in: name and age
        out: Person object
        """
        self.name = name
        self._age = age

    @abstractmethod
    def get_role(self):
        """
        Return the person's role.
        in: none
        out: role string
        """
        pass

    def introduce(self):
        """
        Print basic introduction.
        in: none
        out: none
        """
        print(f"My name is {self.name}. I am {self._age} years old.")


class Student(Person):
    """
    Student class that inherits from Person.
    """

    def __init__(self, name, age, student_id, grade):
        """
        Create a student.
        in: name, age, student id, grade
        out: Student object
        """
        super().__init__(name, age)
        self.student_id = student_id
        self.__grade = grade

    def get_role(self):
        """
        Return role name.
        in: none
        out: string
        """
        return "Student"

    def get_grade(self):
        """
        Return the student's grade.
        in: none
        out: grade
        """
        return self.__grade

    def update_grade(self, new_grade):
        """
        Update grade if valid.
        in: numeric grade
        out: none
        """
        if 0 <= new_grade <= 100:
            self.__grade = new_grade
            print(f"{self.name}'s grade was updated.")
        else:
            print("Grade must be between 0 and 100.")


class Teacher(Person):
    """
    Teacher class that inherits from Person.
    """

    def __init__(self, name, age, employee_id, subject):
        """
        Create a teacher.
        in: name, age, employee id, subject
        out: Teacher object
        """
        super().__init__(name, age)
        self.employee_id = employee_id
        self.subject = subject

    def get_role(self):
        """
        Return role name.
        in: none
        out: string
        """
        return "Teacher"

    def teach(self):
        """
        Print teaching action.
        in: none
        out: none
        """
        print(f"{self.name} is teaching {self.subject}.")


class Classroom:
    """
    Classroom class that manages students and a teacher.
    """

    def __init__(self, room_name, teacher):
        """
        Create a classroom.
        in: room name and Teacher object
        out: Classroom object
        """
        self.room_name = room_name
        self.teacher = teacher
        self.students = []

    def add_student(self, student):
        """
        Add a student to the classroom.
        in: Student object
        out: none
        """
        self.students.append(student)

    def show_class_info(self):
        """
        Print classroom information.
        in: none
        out: none
        """
        print(f"Classroom: {self.room_name}")
        print(f"Teacher: {self.teacher.name} ({self.teacher.get_role()})")
        print("Students:")
        for student in self.students:
            print(f"- {student.name}, Grade: {student.get_grade()}")

    def class_average(self):
        """
        Return average grade of the class.
        in: none
        out: average grade or 0
        """
        if len(self.students) == 0:
            return 0

        total = 0
        for student in self.students:
            total += student.get_grade()

        return total / len(self.students)


def main():
    """
    Run the full school system example.
    in: none
    out: none
    """
    teacher = Teacher("Michael", 26, 501, "Python")

    student1 = Student("Liam", 21, 1001, 88)
    student2 = Student("Emma", 22, 1002, 94)
    student3 = Student("Noah", 20, 1003, 76)

    classroom = Classroom("Software Engineering A", teacher)

    classroom.add_student(student1)
    classroom.add_student(student2)
    classroom.add_student(student3)

    print("=== INTRODUCTIONS ===")
    teacher.introduce()
    print(teacher.get_role())
    teacher.teach()

    print()
    student1.introduce()
    print(student1.get_role())

    print("\n=== CLASSROOM INFO ===")
    classroom.show_class_info()

    print("\n=== CLASS AVERAGE ===")
    print(classroom.class_average())

    print("\n=== UPDATE GRADE ===")
    student3.update_grade(85)
    classroom.show_class_info()
    print("New average:", classroom.class_average())


if __name__ == "__main__":
    main()