# (Conversion from kilograms to pounds) 
#Write a program that displays the following table (note that 1 kilogram is 2.2 pounds)

kg = int(input(f"Show X kg to X pound: "))

for i in range(kg+1):
    print(f"Kilograms\tPounds")
    print(f"{i}\t\t {round(2.2*i,1)}")