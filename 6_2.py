# *6.2 (Sum the digits in an integer) Write a function that computes the sum of the digits in an integer.
# For example,234 returns 2 + 3 + 4 
# Hint: Use the  operator to extract digits, and the operator to remove the extracted digit. 
# For instance, to extract  from  use     To remove  from  use  
# Use a loop to repeatedly extract and remove the digits until all the digits are extracted.
# Write a test program that prompts the user to enter an integer and displays the sum of all its digits.

def main():
    while True:
        try:
            user_input = int(input("Enter an integer: "))
            break
        except ValueError:
            print("This is not an integer")
    print(f"The sum of digits for {user_input} is {sumDigits(user_input)}")

def sumDigits(n):
    total = 0

    n_len = len(str(len))
    for i in range(n_len+1):
        total += n % 10
        n = n //10
    return total

main()
