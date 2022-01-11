from message import Message

class SMS(Message):
    
    def __init__(self, sender, receiver):
        self.sender = sender
        self.receiver = receiver
    
    def send(self):
        msg = (
            "Sending message...\n"
            f"From:    {self.sender}\n"
            f"To:      {self.receiver}\n"
            f"{self.message}"
        )
        print(msg)