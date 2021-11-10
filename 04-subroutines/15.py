#import mymath
from mymath import *

winning_number = generate_number()

while True:
    num = read_number()
    
    if num == winning_number:
        print("You won!")
        break
    else:
        print("Try again")
    
    