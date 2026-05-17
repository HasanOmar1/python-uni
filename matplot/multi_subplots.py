"""
Lesson File 3 - Multiple Graphs and Subplots

Goal:
Show how to create different chart types and how to display more than one graph.

Estimated time:
15 minutes
"""

import matplotlib.pyplot as plt


# ============================================================
# Example 1: Bar Chart
# ============================================================
# Bar charts are useful for comparing categories.

subjects = ["Python", "Math", "English", "Java"]
grades = [90, 75, 88, 82]

plt.bar(subjects, grades)

plt.title("Grades by Subject")
plt.xlabel("Subject")
plt.ylabel("Grade")

plt.show()


# ============================================================
# Example 2: Scatter Plot
# ============================================================
# Scatter plots are useful for showing a relationship between two values.

hours_studied = [1, 2, 3, 4, 5, 6]
exam_scores = [55, 60, 68, 75, 85, 90]

plt.scatter(hours_studied, exam_scores)

plt.title("Study Hours and Exam Scores")
plt.xlabel("Hours Studied")
plt.ylabel("Exam Score")

plt.grid(True)

plt.show()


# ============================================================
# Example 3: Subplots
# ============================================================
# Subplots allow us to show more than one graph in the same window.

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


# ============================================================
# Example 4: Basic Interactive Idea
# ============================================================
# Matplotlib windows are interactive by default in many environments.
# Students can zoom, move, and save the graph from the window toolbar.
#
# Important:
# In some IDEs, graphs may appear inside the editor instead of a new window.
# This depends on the environment settings.

months = ["Jan", "Feb", "Mar", "Apr", "May"]
sales = [1200, 1500, 1100, 1800, 2000]

plt.plot(months, sales, marker="o")

plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.grid(True)

plt.show()