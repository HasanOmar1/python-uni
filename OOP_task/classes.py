
class LibraryItem:
    def __init__(self, title, category , total_pages):
        self.title = title
        self.category = category
        self.total_pages = total_pages
        self.pages_read = 0
        self.is_completed = False

    def show_info(self):
        print("Title: " + self.title)
        print("Category: " + self.category)
        print("Total Pages: " + str(self.total_pages))
        print("Pages Read: " + str(self.pages_read))
        print("Completed: " + str(self.is_completed))
        print()


    def read_pages(self,amount):
        if amount <= 0:
            amount = 0

        self.pages_read = self.pages_read + amount
        if self.pages_read >= self.total_pages:
            self.pages_read = self.total_pages
            self.is_completed = True

    def remaining_pages(self):
        return self.total_pages - self.pages_read

    def completion_percentage(self):
        return self.pages_read / self.total_pages * 100

    def is_long_item(self):
        return self.total_pages >= 250



class ReadingList:
    def __init__(self , library_items : list[LibraryItem]):
        self.library_items = library_items

    def add_item(self,item):
        self.library_items.append(item)

    def show_all_items(self):
        for item in self.library_items:
            item.show_info()

    def find_item_by_title(self,title):
        for item in self.library_items:
            if title == item.title:
                return item
        return None

    def read_item(self, title , amount):
        for item in self.library_items:
            if title == item.title:
                item.read_pages(amount)


    def count_completed_items(self):
        count = 0
        for item in self.library_items:
            if item.is_completed:
                count += 1
        return count

    def get_long_items(self):
        count = 0
        for item in self.library_items:
            if item.is_long_item():
                count += 1

    def total_pages_left(self):
        totalPages = 0
        for item in self.library_items:
            totalPages += item.remaining_pages()
        return totalPages

