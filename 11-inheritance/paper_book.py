from book import Book

class PaperBook(Book):
    def __init__(self, title, author, genre, no_pages):
        super().__init__(title, author, genre)
        self.no_pages = no_pages
    
      
    def __str__(self):
        return super().__str__() + f", Number of pages: {self.no_pages}"