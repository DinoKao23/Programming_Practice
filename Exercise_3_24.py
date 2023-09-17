# (Game: pick a card) Write a program that simulates picking a card from a deck of 52 cards.
#Your program should display the rank and suit of the card. 

import random

# Create dictionary for num
dict_of_num ={
    1:1, 2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9, 10:10, 11:"Jack", 12:"Queen", 13:"King"
}

# Create dictionary for shape
dict_of_shape ={
    1:"Spade",
    2:"Heart",
    3:"Diamonds",
    4:"Clubs"
}

# Generate random number for num and shape
num = random.randint(1,13)
shape = random.randint(1,4)

# Print the result
print(f"You pick a {dict_of_num[num]} of {dict_of_shape[shape]}")