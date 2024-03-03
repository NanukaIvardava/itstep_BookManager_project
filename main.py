class Book:
    # Constructor for the Book class, initializes book's title, author and publication year'
    def __init__(self, title, author, pub_year):
        self.title = title
        self.author = author
        self.pub_year = pub_year

    # Showing book details
    def show_details(self):
        print(f"--📘--\nTitle: {self.title}\nAuthor: {self.author}\nPublication Year: {self.pub_year}\n")

class BookManager:
    # Constructor for the BookManager class, initializes book list
    def __init__(self):
        self.books = []

    # adding a new book to the list
    def add_book(self, title, author, pub_year):
        new_book = Book(title.strip(), author.strip(), pub_year)
        self.books.append(new_book)
        print("\n✅ Book added successfully ✅\n")

    # displaying all the books
    def all_books(self):
        if not self.books:
            print("\n⛔ No books to display ⛔")
        else:
            print("\n🧾 List of all books:")
            for book in self.books:
                book.show_details()

    # searching for a book by  title
    def search_book(self, title):
        for book in self.books:
            if book.title.lower().strip() == title.lower().strip():
                print("\n🔎 Book found:")
                book.show_details()
                return
        print("\n⛔ Book not found ⛔")

    # removing a book from the list
    def remove_book(self, title):
        for book in self.books:
            if book.title.lower().strip() == title.lower().strip():
                self.books.remove(book)
                print("\n✅ Book removed successfully ✅")
                return
        print("\n⛔ Book not found ⛔")