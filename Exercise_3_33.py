#(Business: check ISBN-10) An ISBN-10 (International Standard Book Number) consists of 10 digits:.
#If the checksum is 10, the last digit is denoted as X according to the ISBN-10 convention. 
# The last digit, d10, is a checksum, which is calculated from the other nine digits using the following formula:
# (d1 * 1 + d2 * 2 + d3 * 3 + d4 * 4 + d5 * 5 + d6 * 6 + d7 * 7 + d8 * 8 + d9 * 9) % 11
# Write a program that prompts the user to enter the first 9 digits and displays the checksum. 
# Your program should read the input as an integer. 
# If the integer starts with 0s, don’t enter these zeros in the input.

# Try to use for loop in the future

isbn9 = int(input(f"Enter the first 9 digits of an ISBN as integer:"))

# Translate the number into str to find the position, fill the blank with zero
sisbn9 = str(isbn9).zfill(9)

d1 = int(sisbn9[0])
d2 = int(sisbn9[1])
d3 = int(sisbn9[2])
d4 = int(sisbn9[3])
d5 = int(sisbn9[4])
d6 = int(sisbn9[5])
d7 = int(sisbn9[6])
d8 = int(sisbn9[7])
d9 = int(sisbn9[8])

#Then, we can use the number to do the calculation
d10 =  (d1 * 1 + d2 * 2 + d3 * 3 + d4 * 4 + d5 * 5 + d6 * 6 + d7 * 7 + d8 * 8 + d9 * 9) % 11

#print the result
if d10 == 10:
    print(f"The checksum is X")
else: print(f"The checksum is {d10}")
