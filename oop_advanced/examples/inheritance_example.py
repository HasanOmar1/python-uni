"""
02_inheritance_demo.py

This file introduces inheritance in Python.

Main teaching goals:
1. Explain that a child class inherits attributes and methods from a parent class.
2. Show method overriding.
3. Show the use of super().
4. Show how inheritance helps avoid repeated code.
"""


class Employee:
    """
    Base class for all employees.
    """

    def __init__(self, name, employee_id, salary):
        """
        Create a new employee.
        in: name, employee id, salary
        out: Employee object
        """
        self.name = name
        self.employee_id = employee_id
        self._salary = salary

    def introduce(self):
        """
        Print employee introduction.
        in: none
        out: none
        """
        print(f"Hello, my name is {self.name}. My employee ID is {self.employee_id}.")

    def calculate_yearly_salary(self):
        """
        Return yearly salary.
        in: none
        out: yearly salary
        """
        return self._salary * 12

    def describe_role(self):
        """
        Print a general role description.
        in: none
        out: none
        """
        print("I am a general employee.")


class Teacher(Employee):
    """
    Teacher class that inherits from Employee.
    """

    def __init__(self, name, employee_id, salary, subject):
        """
        Create a new teacher.
        in: name, employee id, salary, subject
        out: Teacher object
        """
        super().__init__(name, employee_id, salary)
        self.subject = subject

    def describe_role(self):
        """
        Override the parent method.
        in: none
        out: none
        """
        print(f"I am a teacher and I teach {self.subject}.")

    def teach(self):
        """
        Print teaching message.
        in: none
        out: none
        """
        print(f"{self.name} is teaching {self.subject}.")


class OfficeWorker(Employee):
    """
    OfficeWorker class that inherits from Employee.
    """

    def __init__(self, name, employee_id, salary, department):
        """
        Create a new office worker.
        in: name, employee id, salary, department
        out: OfficeWorker object
        """
        super().__init__(name, employee_id, salary)
        self.department = department

    def describe_role(self):
        """
        Override the parent method.
        in: none
        out: none
        """
        print(f"I work in the {self.department} department.")

    def manage_documents(self):
        """
        Print office task message.
        in: none
        out: none
        """
        print(f"{self.name} is managing documents.")


def main():
    """
    Run examples for inheritance.
    in: none
    out: none
    """
    employee = Employee("Noa", 1001, 7000)
    teacher = Teacher("Michael", 2001, 9000, "Python")
    office_worker = OfficeWorker("Dana", 3001, 8000, "Administration")

    print("=== EMPLOYEE ===")
    employee.introduce()
    employee.describe_role()
    print(employee.calculate_yearly_salary())

    print("\n=== TEACHER ===")
    teacher.introduce()
    teacher.describe_role()
    teacher.teach()
    print(teacher.calculate_yearly_salary())

    print("\n=== OFFICE WORKER ===")
    office_worker.introduce()
    office_worker.describe_role()
    office_worker.manage_documents()
    print(office_worker.calculate_yearly_salary())

    print("\n=== INHERITANCE CHECK ===")
    print(isinstance(teacher, Teacher))
    print(isinstance(teacher, Employee))
    print(isinstance(office_worker, Employee))


if __name__ == "__main__":
    main()