class Account:
    
    def __init__(self, number):
        self.number = number
        self.balance = 0
    
    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        if amount < self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds on the account")
    
    def __str__(self):
        return f"Bank Account No: {self.number} Balance: PLN {self.balance / 100}"