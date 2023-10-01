# Find the amount of students
number = int(input(f"Enter the number of students: "))

# Set highscore and name
high_score = 0
high_name = ""

for i in range(number):
    name = input("Enter a student name: ")
    score = float(input("Enter a student score: "))

    if score > high_score:
        high_name = name
        high_score = score

print(f"Top student {high_name}'s score is {high_score}")