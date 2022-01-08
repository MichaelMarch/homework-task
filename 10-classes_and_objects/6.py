class Book:
    def __init__(self, author, page_count, title):
       self.author = author
       self.page_count = page_count
       self.title = title
    
    def open(self, page = 0):
        pass
    
    def close(self):
        pass

    def turn_page(self):
        pass


class TelephoneConnection:
    def __init__(self, time_passed, caller, receiver):
        self.time_passed = time_passed
        self.caller = caller
        self.receiver = receiver
        
    def call(self, who):
        pass
    
    def hang_up(self):
        pass
    
    def freeze(self):
        pass

class StudentGroup:
    def __init__(self, count, name, average_iq):
        self.count = count
        self.name = name
        self.average_iq = average_iq
    
    def study(self, what):
        pass
    
    def add_student(self, student):
        pass
    
    def remove_student(self, studet):
        pass