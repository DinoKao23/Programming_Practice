# Find the amount of students
number = int(input(f"Enter the number of students: "))

# Set highscore and name
high_score = 0
high_name = ""
second_high_score = 0
second_high_name = ""

# Use for loop to put multiple input
for i in range(number):
    name = input("Enter a student name: ")
    score = float(input("Enter a student score: "))

    if score > high_score:
        second_high_score = high_score
        second_high_name = high_name
        high_name = name
        high_score = score
    elif score >second_high_score:
        second_high_score = score
        second_high_name = name


print("Top two students:")
print(f"{high_name}'s score is {high_score}")
print(f"{second_high_name}'s score is {second_high_score}")