from book import Book

class EBook(Book):
    
    def __init__(self, title, author, genre, uri):
        super().__init__(title, author, genre)
        self.uri = uri
    
    def __str__(self):
        return super().__str__() + f", Path: {self.uri}"