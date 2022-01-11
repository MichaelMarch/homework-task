class EBook:
    def __init__(self, title, author, number_of_pages):
        self.title = title
        self.author = author
        self.number_of_pages = number_of_pages
        self.current_page = -1
    
    def open(self):
        self.current_page = 1
    
    def read(self):
        if self.current_page == -1:
            print("You need to open the book first to read it!")
            return
        
        self.current_page += 1
    
    def close(self):
        self.current_page = -1
    
    def __str__(self):
        return (
            f"Title:       {self.title}\n"
            f"Author:      {self.author}\n"
            f"Pages:       {self.number_of_pages}\n"
            F"CurrentPage: {self.current_page}"
        )