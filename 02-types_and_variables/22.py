import random

hidden_number = random.randrange(1, 6 + 1)

while True:
    guess = int(input("Try to guess the number (1 - 6): "))
    if guess < 1 or guess > 6:
        continue
    
    if guess == hidden_number:
        print("True")
        break