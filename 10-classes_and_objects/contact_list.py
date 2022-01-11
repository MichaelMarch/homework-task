class ContactList():
    def __init__(self):
        self.contacts = []
    
    def add(self, contact):
        self.contacts.append(contact)
    
    def __str__(self):
        msg = ""
        for contact in self.contacts:
            msg += f"{contact}"
        return msg
    