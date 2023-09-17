# # Write a program that prompts the user to enter a three-digit integer and determines whether it is a palindrome number. 
# A number is palindrome if it reads the same from right to left and from left to right.

num = input(f"Enter a three digit numbers: ")

# Compare the first and last digit
if num[0] == num[2]:
    print(f"{num} is a palindrome number.")
elif len(num) > 3 or len(num) <3:
    print(f"Please enter a three digit numbers")
else: print(f"{num} is not a palindrome number.")
