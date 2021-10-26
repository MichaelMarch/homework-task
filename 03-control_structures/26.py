PIN = "0805"

for i in range(0, 3):
    user_entered_pin = str(input("Enter the PIN code: "))
    if user_entered_pin != PIN:
        print("Incorrect...")
    else:
        print("Correct :)")
else:
    print("Sorry, your payment card has been blocked.")