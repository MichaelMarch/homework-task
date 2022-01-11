from message import Message


class EMail(Message):
    
    def __init__(self, sender_address, recipient_address, subject):
        self.sender_address = sender_address
        self.recipient_address = recipient_address
        self.subject = subject
    
    def send(self):
        msg = (
            "Sending message...\n"
            f"From:    {self.sender_address}\n"
            f"To:      {self.recipient_address}\n"
            f"Subject: {self.subject}\n"
            f"{self.message}"
        )
        print(msg)