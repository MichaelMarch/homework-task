product_name = input("Enter the name of a product: ")

with open("data/shopping.txt", 'a') as file:
    file.write(product_name + '\n')