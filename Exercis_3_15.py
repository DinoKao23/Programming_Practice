# (Game: lottery) 
# Generate a three-digit lottery number. The program prompts the user to enter a three-digit number and determines whether the user wins according to the following rules:
# If the user input matches the lottery number in the exact order, the award is $10,000. 
# If all the digits in the user input match all the digits in the lottery number, the award is $3,000. 
# If one digit in the user input matches a digit in the lottery number, the award is $1,000.

# Import package
import random

# Enter a three digits number
#num = input(f"Enter your lottery pick (three digits number):")

#test
num = str(random.randint(0,999)).zfill(3)
print(f"I pick {num}")
# Generate lottery number
lottery = str(random.randint(0,999)).zfill(3)

#Print out the lottery number
print(f"The lottery is {lottery}")


# Check if ourpick has same output as lottery
if num == lottery:
    print(f"Congratulation! You win 10,000 dollars.")
elif (num[0] == lottery[0] or num[0] == lottery[1] or num[0] == lottery[2]) and (num[1] == lottery[0] or num[1] == lottery[1] or num[1] == lottery[2]) and (num[2] == lottery[0] or num[2] == lottery[1] or num[2] == lottery[2]):
    print("Congradulation! You win 3,000 dollars")
elif num[0] == lottery[0] or num[1] == lottery[1] or num[2] == lottery[2]:
    print("Congradulation! You win 1,000 dollars")
else:
    print("Sorry. No match.")