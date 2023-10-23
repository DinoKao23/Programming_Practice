# (Sum a series) Write a program to sum the following series:
# 1/3 + 3/5 + 5/7 + 7/9 + 9/11 + 11/13 + ... + 95/97 + 97/99

n = 0

for i, j in zip(range(1,99,2), range(3,101,2)):
    n += i/j

print(n)