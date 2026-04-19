from classes import LibraryItem, ReadingList

def main():
    libraryItem1 = LibraryItem("Sonic","Action",420)
    libraryItem2 = LibraryItem("Batman","Action",350)
    libraryItem3 = LibraryItem("Harry Potter","Fantasy",700)
    libraryItem4 = LibraryItem("The 5th Wave","Horror",670)

    listOfLibraryItems = [libraryItem1, libraryItem2, libraryItem3, libraryItem4]

    readingList = ReadingList(listOfLibraryItems)
    readingList.show_all_items()

    readingList.find_item_by_title("Sonic").read_pages(100)
    readingList.find_item_by_title("Batman").read_pages(300)
    readingList.find_item_by_title("The 5th Wave").read_pages(700)

    readingList.show_all_items()


    numOfCompletedBooks = readingList.count_completed_items()
    print("Completed Books: ", numOfCompletedBooks)

    numOfPagesLeftToRead = readingList.total_pages_left()
    print("Total Pages Left to Read: ", numOfPagesLeftToRead)

    print("Title of long books")
    for item in readingList.library_items:
        if item.is_long_item():
            print(item.title)

if __name__ == '__main__':
    main()