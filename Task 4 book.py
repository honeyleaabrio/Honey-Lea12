class Book:
    def __init__(self, title, author, year_published):
        self.title = title
        self.author = author
        self.year_published = year_published

    def describe(self):
        """Display the details of the book."""
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Year Published: {self.year_published}")
        print()

book1 = Book("Harry Potter and the Sorcere's Stone", "J.K. Rawling", 2001)
book2 = Book("Harry Potter and the Half-Blood Prince", "J.k. Rawling", 2005)
book3 = Book("Harry Potter and the Order of the Phoenix", "J.k. Rawling", 2003)

book1.describe()
book2.describe()
book3.describe()

