# (Display an integer reversed) 
# Write a function with the following header to display an integer in reverse order

def main():
    try:
        user_input = int(input("Enter an integer and perform the output: "))
    except: 
        ValueError
        print("Please enter a number")
    print(reverse(user_input))    

def reverse(num):
    return str(num)[::-1]

main()

