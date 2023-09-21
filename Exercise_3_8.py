# Write a program that prompts the user to enter three numbers and displays them in increasing order.
# Can't use sort()
# print(sorted([a,b,c], reverse = True))

a =float(input(f"Enter a number: "))
b =float(input(f"Enter a number: "))
c =float(input(f"Enter a number: "))

if b >= a:
    a,b =b,a
elif c >= a:
    a, c= c,a
elif c >= b:
    b, c =c, b

print(f"The sorted orders are {a}, {b}, {c}.")

