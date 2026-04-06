"""
Important note:
This file uses Python's built-in unittest framework.
"""

import unittest
import module_to_test


# ============================================================
# PART 1: FIRST TESTS - BASIC ASSERTIONS
# Main idea:
# - A test checks whether the actual result matches the expected result
# - assertEqual is one of the most common testing tools
# ============================================================

class TestAddFunction(unittest.TestCase):

    def test_add_positive_numbers(self):
        result = module_to_test.add(2, 3)
        self.assertEqual(result, 5)

    def test_add_negative_numbers(self):
        result = module_to_test.add(-4, -6)
        self.assertEqual(result, -10)



# ============================================================
# PART 2: MORE THAN ONE FUNCTION
# Main idea:
# - A program usually has many functions
# - We can write a separate test class for each topic or function group
# ============================================================

class TestSubtractFunction(unittest.TestCase):

    def test_subtract_regular_numbers(self):
        self.assertEqual(module_to_test.subtract(10, 4), 6)

    def test_subtract_to_negative(self):
        self.assertEqual(module_to_test.subtract(3, 8), -5)



# ============================================================
# PART 3: BOOLEAN TESTS
# Main idea:
# - Some functions return True or False
# - For those, assertTrue and assertFalse are very useful
# ============================================================

class TestIsEvenFunction(unittest.TestCase):

    def test_even_number(self):
        self.assertTrue(module_to_test.is_even(8))

    def test_odd_number(self):
        self.assertFalse(module_to_test.is_even(7))

    def test_zero_is_even(self):
        self.assertTrue(module_to_test.is_even(0))



# ============================================================
# PART 4: STRING TESTS
# Main idea:
# - We can test text functions too
# - It is important to test both normal cases and simple edge cases
# ============================================================

class TestCapitalizeTextFunction(unittest.TestCase):

    def test_regular_word(self):
        self.assertEqual(module_to_test.capitalize_text("python"), "Python")

    def test_empty_string(self):
        self.assertEqual(module_to_test.capitalize_text(""), "")

    def test_one_letter(self):
        self.assertEqual(module_to_test.capitalize_text("a"), "A")


# ============================================================
# PART 5: TESTING EXCEPTIONS
# Main idea:
# - Some functions can raise errors
# - Unit tests can check that errors happen exactly where expected
# ============================================================

class TestDivideFunction(unittest.TestCase):

    def test_regular_division(self):
        self.assertEqual(module_to_test.divide(10, 2), 5)

    def test_division_result_with_decimal(self):
        self.assertEqual(module_to_test.divide(9, 2), 4.5)

    def test_divide_by_zero_raises_error(self):
        with self.assertRaises(ZeroDivisionError):
            module_to_test.divide(5, 0)



# ============================================================
# PART 6: ADDITIONAL PRACTICE EXAMPLES
# Main idea:
# - Once students understand the structure, they can test new functions
# - These are great examples for class discussion or mini exercises
# ============================================================

class TestFindMaxFunction(unittest.TestCase):

    def test_first_is_bigger(self):
        self.assertEqual(module_to_test.find_max(9, 3), 9)

    def test_second_is_bigger(self):
        self.assertEqual(module_to_test.find_max(2, 8), 8)

    def test_both_are_equal(self):
        self.assertEqual(module_to_test.find_max(7, 7), 7)


class TestReverseStringFunction(unittest.TestCase):

    def test_regular_string(self):
        self.assertEqual(module_to_test.reverse_string("python"), "nohtyp")

    def test_empty_string(self):
        self.assertEqual(module_to_test.reverse_string(""), "")

    def test_single_character(self):
        self.assertEqual(module_to_test.reverse_string("x"), "x")



# ============================================================
# LESSON SUMMARY
# ============================================================
# Things students should remember:
# 1. A unit test checks one small behavior in the code.
# 2. Each test method should begin with the word test.
# 3. We compare expected results with actual results.
# 4. We can test numbers, strings, booleans, and exceptions.
# 5. Good tests help us detect bugs quickly after changes.


# ============================================================
# RUN ALL TESTS
# ============================================================

if __name__ == "__main__":
    unittest.main()
