# (Find the highest score) 
# Write a program that prompts the user to enter the number of students and each student’s name and score, and displays the name and highest score. 
# Assume that the number of students is at least 1.

# Know how many students are in this data set
student = int(input(f"Enter the number of students: "))
# Use dictionary to put name and score together
student_dict = {}


# Use num to see how many times have the loop run
num = 0

# Use while loop to check total student
while student > num:
    name = input("Enter a student name: ")
    score = float(input("Enter a student score: "))
    student_dict.update({name:score})
    num +=1

# Find the max number in student_dict
max_name = max(student_dict, key=student_dict.get)
max_score= student_dict[max_name]

print(f"Top student {max_name}'s score is {max_score} ")