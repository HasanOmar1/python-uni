import matplotlib.pyplot as plt


# Task 1
# Gaming Hours
days = [1, 2, 3, 4, 5]
hours_studied = [2, 3, 2, 5, 4]

plt.plot(days, hours_studied , marker="o")
plt.title("Gaming Hours")
plt.xlabel("Days")
plt.ylabel("Hours")
plt.grid(True)
plt.show()

# Task 2

subjects = ["Math" , "English" , "Chemistry"]

student_a_grades = [70, 93, 81]
student_b_grades = [100, 81, 77]

plt.plot(subjects, student_a_grades, marker="o", label="Student A")
plt.plot(subjects, student_b_grades, marker="s", label="Student B")

plt.xlabel("Subjects")
plt.ylabel("Grades")
plt.title("Comparison of 2 students Grades")
plt.grid(True)
plt.legend()
plt.show()


# Task 3
subjects = ["Python", "Math", "English", "Java","React"]
grades = [90, 75, 88, 82, 99]

plt.bar(subjects, grades)

plt.title("Grades by Subject")
plt.xlabel("Subject")
plt.ylabel("Grade")

plt.show()


# Task 4
hours_studied = [1, 2, 3, 4, 5, 6]
exam_scores = [55, 60, 68, 75, 85, 90]

plt.scatter(hours_studied, exam_scores)

plt.title("Study Hours and Exam Scores")
plt.xlabel("Hours Studied")
plt.ylabel("Exam Score")

plt.grid(True)

plt.show()

# Task 5
days = [1, 2, 3, 4, 5]
hours_studied = [2, 3, 2, 5, 4]
questions_solved = [5, 8, 6, 12, 10]

# Create a figure with 1 row and 2 columns.
plt.subplot(1, 2, 1)
plt.plot(days, hours_studied, marker="o")
plt.title("Hours Studied")
plt.xlabel("Day")
plt.ylabel("Hours")
plt.grid(True)

plt.subplot(1, 2, 2)
plt.bar(days, questions_solved)
plt.title("Questions Solved")
plt.xlabel("Day")
plt.ylabel("Questions")

# tight_layout improves spacing between graphs.
plt.tight_layout()

plt.show()

