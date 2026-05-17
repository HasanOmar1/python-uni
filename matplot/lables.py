"""
Lesson File 2 - Labels, Readability, and Better Graphs

Goal:
Teach students how to make graphs easier to understand.

Estimated time:
12-15 minutes
"""

import matplotlib.pyplot as plt


# ============================================================
# Example 1: Axis Labels
# ============================================================

days = [1, 2, 3, 4, 5]
hours_studied = [2, 3, 2, 5, 4]

plt.plot(days, hours_studied, marker="o")

# xlabel describes the x-axis.
plt.xlabel("Day")

# ylabel describes the y-axis.
plt.ylabel("Hours Studied")

plt.title("Study Progress")
plt.show()


# ============================================================
# Example 2: Grid
# ============================================================
# A grid makes the graph easier to read.

days = [1, 2, 3, 4, 5]
hours_studied = [2, 3, 2, 5, 4]

plt.plot(days, hours_studied, marker="o")

plt.xlabel("Day")
plt.ylabel("Hours Studied")
plt.title("Study Progress")

# grid(True) shows background lines.
plt.grid(True)

plt.show()


# ============================================================
# Example 3: Multiple Lines and Legend
# ============================================================

days = [1, 2, 3, 4, 5]

student_a = [2, 3, 2, 5, 4]
student_b = [1, 2, 3, 3, 5]

# label gives a name to each line.
plt.plot(days, student_a, marker="o", label="Student A")
plt.plot(days, student_b, marker="s", label="Student B")

plt.xlabel("Day")
plt.ylabel("Hours Studied")
plt.title("Study Comparison")

plt.grid(True)

# legend() displays the labels of the lines.
plt.legend()

plt.show()