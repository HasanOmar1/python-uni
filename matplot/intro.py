"""
Lesson File 1 - Matplotlib Introduction

Goal:
Introduce Matplotlib and show how to create a simple graph.

Estimated time:
10-12 minutes
"""

import matplotlib.pyplot as plt


# ============================================================
# Example 1: Basic Line Plot
# ============================================================
# Matplotlib is a Python library used to create graphs and charts.
# The most common module is pyplot, usually imported as plt.

# x values usually represent the horizontal axis.
days = [1, 2, 3, 4, 5]

# y values usually represent the vertical axis.
hours_studied = [2, 3, 2, 5, 4]

# plot() creates a line graph.
plt.plot(days, hours_studied)


# show() opens the graph window.
plt.show()


# ============================================================
# Example 2: Adding a Simple Title
# ============================================================

days = [1, 2, 3, 4, 5]
hours_studied = [2, 3, 2, 5, 4]

plt.plot(days, hours_studied)

# A title helps the reader understand what the graph is about.
plt.title("Hours Studied During the Week")

plt.show()


# ============================================================
# Example 3: Changing Line Style
# ============================================================

days = [1, 2, 3, 4, 5]
hours_studied = [2, 3, 2, 5, 4]

# marker="o" adds a circle on every data point.
# linestyle="--" changes the line to a dashed line.
plt.plot(days, hours_studied, marker="o", linestyle="--")

plt.title("Hours Studied During the Week")
plt.show()