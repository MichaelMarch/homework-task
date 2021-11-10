text = str(input("Enter your sentance: "))
letter = str(input("Enter what letter you want to count for: "))

def count_letter(in_, what):
    counter = 0
    
    for c in in_:
        if what == c:
            counter += 1

    return counter

print(f"The letter {letter} occoured {count_letter(text, letter)} times")