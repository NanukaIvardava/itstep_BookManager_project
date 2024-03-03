class Book:
    # Constructor for the Book class, initializes book's title, author and publication year'
    def __init__(self, title, author, pub_year):
        self.title = title
        self.author = author
        self.pub_year = pub_year

    # Showing book details
    def show_details(self):
        print(f"--📘--\nTitle: {self.title}\nAuthor: {self.author}\nPublication Year: {self.pub_year}\n")