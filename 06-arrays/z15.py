colors = ["czerwony", "zielony", "czarny", "bilardowa zieleń"]

with open("colors.txt", 'w', encoding="utf-8") as file:
    for color in colors:
        file.write_line(f"{color}\n")
        

