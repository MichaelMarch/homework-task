from message import Message

class SMS(Message):
    
    def __init__(self, sender, receiver):
        self.sender = sender
        self.receiver = receiver
    
    def send(self):
        msg = (
            "Sending message..."
            f"From:    {self.sender}"
            f"To:      {self.receiver}"
            f"{self.message}"
        )
        print(msg)