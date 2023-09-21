# #(Generate vehicle plate numbers) 
# Assume a vehicle plate number consists of three uppercase letters followed by four digits. 
# Write a program to generate a plate number.

import random

num = random.randint(0,9999)
c1 = random.randint(ord('A'), ord('Z'))
c2 = random.randint(ord('A'), ord('Z'))
c3 = random.randint(ord('A'), ord('Z'))


print(chr(c1)+chr(c2)+chr(c3)+str(num).zfill(4))