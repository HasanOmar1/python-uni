"""
Python Exceptions – Review File
All examples + questions under each example.
All answers are at the bottom in comments so they will not run.
"""


# ============================================================
# EXAMPLE 1: Basic try / except (ValueError + ZeroDivisionError)
# ============================================================

def example_1_basic_try_except():
    try:
        x = int(input("Enter a number: "))
        print(10 / x)
    except ValueError:
        print("Invalid number")
    except ZeroDivisionError:
        print("Cannot divide by zero")
    finally:
        print("done")


# Questions (Example 1):
# 1) Run the function. What happens if the user types: hello ?
# 2) Run the function. What happens if the user types: 0 ?
# 3) Change the function so it prints 10 divided by the number (instead of 100).
# 4) Add a print that always runs at the end: "Done".


# ============================================================
# EXAMPLE 2: try / except / else
# ============================================================

def example_2_else_block():
    try:
        num = int(input("Enter a number: "))
    except ValueError:
        print("Invalid input")
    else:
        print("You entered:", num)
        print("Square:", num ** 2)
        print("Cube:", num ** 3)

# Questions (Example 2):
# 5) When will the else block run?
#   if no errors
# 6) Add another line in else that prints the cube of the number.
#   line 43
# 7) What happens if the user types: abc ? Which block runs?
#    the except


# ============================================================
# EXAMPLE 3: finally (always runs)
# ============================================================

def example_3_finally_block():
    filename = input("Enter file name: ")
    try:
        f = open(filename, "r")
        content = f.read()
        print(content)
    except FileNotFoundError:
        print("File not found")
    finally:
        # Note: This runs whether an error happened or not.
        print("Finished file operation")


# Questions (Example 3):
# 8) What prints if the file does not exist?
# 9) What prints if the file exists and is read successfully?
# 10) Improve the code: make sure the file is closed when it is opened (hint: with).


# ============================================================
# EXAMPLE 4: raise (create your own error)
# ============================================================

def example_4_raise_value_error():
    age = int(input("Enter age: "))

    if age < 0 or age > 120:
        raise ValueError("Invalid age")

    print("Age is valid")


# Questions (Example 4):
# 11) What happens if the user types: -5 ?
# 12) What happens if the user types: 200 ?
# 13) Add handling so the program does not crash, and prints the error message nicely.


# ============================================================
# EXAMPLE 5: Catching any exception (not always recommended)
# ============================================================

def example_5_catch_all():
    try:
        text = input("Enter a number: ")
        num = int(text)
        print("Result:", 10 / num)
    except ValueError:
        print("Invalid input")
    except ZeroDivisionError:
        print("Cannot divide by zero")



# Questions (Example 5):
# 14) What type of error is caught if the user types: abc ?
# ValueError
# 15) What type of error is caught if the user types: 0 ?
# ZeroDivisionError
# 16) Change the code to catch ValueError and ZeroDivisionError separately (no generic Exception).


# ============================================================
# EXAMPLE 6: Custom function with validation
# ============================================================

def safe_divide(a, b):
    if b == 0:
        raise ZeroDivisionError("b cannot be 0")
    if b < 0:
        raise ValueError("b is negative")
    return a / b


def example_6_using_safe_divide():
    try:
        while True:
            a = float(input("Enter a: "))
            b = float(input("Enter b: "))
            result = safe_divide(a, b)
            print("Result:", result)
            break
    except ValueError as e:
        print("Value Error: Invalid number format, ", e)
    except ZeroDivisionError as e:
        print("Division error:", e)



# Questions (Example 6):
# 17) What happens if b is 0?
# zero division error
# 18) Change safe_divide so it raises ValueError if b is negative.
# 19) Add a loop so the user keeps trying until they succeed.


# ============================================================
# EXAMPLE 7: Loop until valid input (common real-life pattern)
# ============================================================

def example_7_loop_until_valid():
    count = 0
    while True:
        try:
            if count >= 3:
                print("Too many tries")
                return
            x = int(input("Enter a number (not 0): "))
            print("10 / x =", 10 / x)
            break
        except ValueError:
            print("Please enter a valid integer.")
            count += 1
        except ZeroDivisionError:
            print("Please do not enter 0.")
            count += 1






example_7_loop_until_valid()
# Questions (Example 7):
# 20) Why is this pattern useful?
# it ensures the user inputs correct input
# 21) Add a limit: after 3 failed attempts, stop and print "Too many tries".
