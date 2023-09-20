Number = int(input(f"Enter an interger: "))

if Number % 5 == 0 and Number % 6 ==0:
    print(f"Is {Number} divisible by 5 and 6? True")
else: 
    print(f"Is {Number} divisible by 5 and 6? False")

if Number % 5 == 0 or Number % 6 ==0:
    print(f"Is {Number} divisible by 5 or 6? True")
else: 
    print(f"Is {Number} divisible by 5 or 6? False")

if Number % 5 == 0 and Number % 6 ==0:
    print(f"Is {Number} divisible by 5 or 6, but not both? False")
elif Number % 5 == 0 or Number % 6 ==0:
    print(f"Is {Number} divisible by 5 or 6, but not both? True")
else: print(f"Is {Number} divisible by 5 or 6, but not both? False")