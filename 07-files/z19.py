with open("data/shoppinglist.txt", 'w') as shopping_file:
    with open("data/MeatAndFish.txt", 'r') as list1_file:
        shopping_file.writelines(list1_file)
        
    shopping_file.write('\n')
    
    with open("data/GrainsAndBread.txt", 'r') as list2_file:
        shopping_file.writelines(list2_file)