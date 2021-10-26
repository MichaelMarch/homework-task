dog_age_in_human_years = int(input("Enter the dog's age in human years: "))



if dog_age_in_human_years <= 2:
    real_dog_age = dog_age_in_human_years * 10.5
else:
    real_dog_age = 21 + (dog_age_in_human_years - 2) * 4
    
print(f"The dog's age in dog years is {real_dog_age} years.")