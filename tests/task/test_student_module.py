import unittest
import student_module

# --------------- Part 2 ---------------
class TestAddNumbersFunctions(unittest.TestCase):
    def test_add_positive_numbers(self):
        result = student_module.add(5,3)
        self.assertEqual(result ,8 )

    def test_add_negative_numbers(self):
        result = student_module.add(-6, -3)
        self.assertEqual(result, -9)

    def test_add_zero_with_number(self):
        result = student_module.add(5, 0)
        self.assertEqual(result, 5)

    def test_add_zero_with_half_number(self):
        result = student_module.add(0.5, 0)
        self.assertEqual(result, 0.5)

class TestSubtractNumbersFunctions(unittest.TestCase):
    def test_subtract_positive_numbers(self):
        result = student_module.subtract(5,3)
        self.assertEqual(result ,2 )

    def test_subtract_negative_numbers(self):
        result = student_module.subtract(-6, -3)
        self.assertEqual(result, -3)

    def test_subtract_number_with_itself(self):
        result = student_module.subtract(5, 5)
        self.assertEqual(result, 0)

    def test_subtract_number_with_half_number(self):
        result = student_module.subtract(0.5, 0)
        self.assertEqual(result, 0.5)



# --------------- Part 3 ---------------
class TestEvenNumbersFunctions(unittest.TestCase):
    def test_even_positive_number(self):
        result = student_module.is_even(8)
        self.assertTrue(result)

    def test_odd_positive_number(self):
        result = student_module.is_even(7)
        self.assertFalse(result)

    def test_zero_number(self):
        result = student_module.is_even(0)
        self.assertTrue(result)

    def test_even_negative_number(self):
        result = student_module.is_even(-8)
        self.assertTrue(result)

    def test_odd_negative_number(self):
        result = student_module.is_even(-7)
        self.assertFalse(result)


# --------------- Part 4 ---------------
class TestStringsFunctions(unittest.TestCase):
    def test_lowercase(self):
        result = student_module.capitalize_text("python")
        self.assertEqual(result, "Python")

    def test_empty_string(self):
        result = student_module.capitalize_text("")
        self.assertEqual(result, "")

    def test_one_letter(self):
        result = student_module.capitalize_text("a")
        self.assertEqual(result, "A")

    def test_capitalized_word(self):
        result = student_module.capitalize_text("Kola")
        self.assertEqual(result, "Kola")

    def test_start_with_number(self):
        result = student_module.capitalize_text("5asd")
        self.assertEqual(result, "5asd")



# --------------- Part 5 ---------------
class TestFindMaxFunctions(unittest.TestCase):
    def test_first_number_is_larger(self):
        result = student_module.find_max(7,3)
        self.assertEqual(result,7)

    def test_second_number_is_larger(self):
        result = student_module.find_max(2, 61)
        self.assertEqual(result, 61)

    def test_equal_numbers(self):
        result = student_module.find_max(61, 61)
        self.assertEqual(result, 61)

    def test_positive_negative_numbers(self):
        result = student_module.find_max(3, -1)
        self.assertEqual(result, 3)

    # Why is the case of equal numbers important in unit testing?
    # to make sure the function checks for less than and equal ( <= )
    # or more than and equal ( >= ).

# --------------- Part 6 ---------------
class TestDivideFunctions(unittest.TestCase):
    def test_result_with_whole_number(self):
        result = student_module.divide(10,2)
        self.assertEqual(result,5)

    def test_result_with_decimal_number(self):
        result = student_module.divide(2, 4)
        self.assertEqual(result, 0.5)

    def test_zero_divide_number(self):
        result = student_module.divide(0, 10)
        self.assertEqual(result, 0)

    def test_division_by_zero_number(self):
        with self.assertRaises(ZeroDivisionError):
            student_module.divide(10, 0)

    def test_equal_number(self):
        result = student_module.divide(10, 10)
        self.assertEqual(result, 1)




# --------------- Part 9 - Final Challenge ---------------
class TestFindMinFunctions(unittest.TestCase):
    def test_first_number_is_smaller(self):
        result = student_module.find_min(3,7)
        self.assertEqual(result,3)

    def test_second_number_is_smaller(self):
        result = student_module.find_min(51, 3)
        self.assertEqual(result, 3)

    def test_equal_numbers(self):
        result = student_module.find_min(61, 61)
        self.assertEqual(result, 61)

    def test_positive_negative_numbers(self):
        result = student_module.find_min(3, -1)
        self.assertEqual(result, -1)



# --------------- Part 7 ---------------
if __name__ == "__main__":
    unittest.main()



# --------------- Part 8 ---------------
# 1. What is the difference between checking code with print() and checking code with unit tests?
# it takes long time to check all cases with print.
# it's easier to check edge cases with unit tests.

# 2. Why is it useful to separate the code file from the test file?
# Cleaner Production Builds, Reduced Logic Pollution, Easier Navigation.

# 3. Why do we test edge cases and not only normal cases?
# edge cases reveal how your code handles boundaries,
# unexpected inputs (like None or empty lists), and extreme values.

# 4. When should we use assertTrue or assertFalse instead of assertEqual?
# when the result returns a boolean value.

# 5. Why is it important to test that an error is raised in the correct situation?
# Testing that an error is raised ensures your code fails predictably
# and safely rather than crashing silently or continuing with corrupted data.
