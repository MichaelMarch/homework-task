first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
university_name = input("Enter your university name: ")
field_of_study = input("Enter your field of study: ")

with open("data/student_data.txt", 'w') as file:
    file.write(first_name + '\n')
    file.write(last_name + '\n')
    file.write(university_name + '\n')
    file.write(field_of_study + '\n')