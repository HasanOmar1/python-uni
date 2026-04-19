import unittest

from classes import LibraryItem,ReadingList


class TestReadingList(unittest.TestCase):

    def test_new_library_item_starts_with_zero_pages_and_not_completed(self):
        item = LibraryItem("Python Basics", "Programming", 300)

        self.assertEqual(item.pages_read, 0)
        self.assertFalse(item.is_completed)

    def test_read_pages_updates_item_correctly(self):
        item = LibraryItem("Python Basics", "Programming", 300)

        item.read_pages(100)

        self.assertEqual(item.pages_read, 100)
        self.assertFalse(item.is_completed)

    def test_reading_up_to_total_pages_marks_item_completed(self):
        item = LibraryItem("Python Basics", "Programming", 300)

        item.read_pages(300)

        self.assertEqual(item.pages_read, 300)
        self.assertTrue(item.is_completed)

    def test_remaining_pages_returns_correct_value(self):
        item = LibraryItem("Python Basics", "Programming", 300)

        item.read_pages(120)

        self.assertEqual(item.remaining_pages(), 180)

    def test_find_item_by_title_returns_correct_object(self):
        item1 = LibraryItem("Python Basics", "Programming", 300)
        item2 = LibraryItem("Short Story", "Fiction", 120)
        reading_list = ReadingList([item1, item2])

        result = reading_list.find_item_by_title("Short Story")

        self.assertEqual(result, item2)

    def test_find_item_by_title_returns_none(self):
        item1 = LibraryItem("Python Basics", "Programming", 300)
        item2 = LibraryItem("Short Story", "Fiction", 120)
        reading_list = ReadingList([item1, item2])

        result = reading_list.find_item_by_title("Science Article")

        self.assertIsNone(result)

    def test_count_completed_items_returns_correct_number(self):
        item1 = LibraryItem("Python Basics", "Programming", 300)
        item2 = LibraryItem("Short Story", "Fiction", 120)
        item3 = LibraryItem("Science Article", "Science", 50)

        item1.read_pages(300)
        item2.read_pages(120)

        reading_list = ReadingList([item1, item2, item3])

        self.assertEqual(reading_list.count_completed_items(), 2)

    def test_total_pages_left_returns_correct_total(self):
        item1 = LibraryItem("Python Basics", "Programming", 300)
        item2 = LibraryItem("Short Story", "Fiction", 120)
        item3 = LibraryItem("Science Article", "Science", 50)

        item1.read_pages(100)
        item2.read_pages(20)
        item3.read_pages(50)

        reading_list = ReadingList([item1, item2, item3])

        self.assertEqual(reading_list.total_pages_left(), 300)


if __name__ == "__main__":
    unittest.main()