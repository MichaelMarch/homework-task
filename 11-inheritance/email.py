from message import Message


class Email(Message):
    
    def __init__(self, sender_address, recipient_address, subject):
        self.sender_address = sender_address
        self.recipient_address = recipient_address
        self.subject = subject
    
    def send(self):
        msg = (
            "Sending message..."
            f"From:    {self.sender_address}"
            f"To:      {self.recipient_address}"
            f"Subject: {self.subject}"
            f"{self.message}"
        )
        print(msg)