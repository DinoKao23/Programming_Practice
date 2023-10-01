#  (Find the two highest scores) 
# Write a program that prompts the user to enter the number of students and each student’s name and score, and displays the highest and second-highest name and scores. 
# Assume that the number of students is at least 2.

# Know how many students are in this data set
student = int(input(f"Enter the number of students: "))
# Use dictionary to put name and score together
student_dict = {}
second_high_score =0

# Use num to see how many times have the loop run
num = 0

# Use while loop to check total student
while student > num:
    name = input("Enter a student name: ")
    score = float(input("Enter a student score: "))
    student_dict.update({name:score})
    num +=1

score_list = list(student_dict.values())

# Find the max number in student_dict
max_name = max(student_dict, key=student_dict.get)
max_score= student_dict[max_name]

for i in score_list:
    if i != max_score and i > second_high_score:
        second_high_score = i

# Find the identify name for this value
for key, value in student_dict.items():
    if value == second_high_score:
        second_high_name = key

print("Top two students:")
print(f"{max_name}'s score is {max_score}")
print(f"{second_high_name}'s score is {second_high_score}")