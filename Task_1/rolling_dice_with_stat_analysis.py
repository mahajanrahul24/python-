# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 16:49:00 2018
This is Rolling dice game.
User can play with positive input i.e. yes and exit the game with negative input i.e. no
If you have dice number 6 then you get JACKPOT.
@author: rahulm99
"""
import random
MIN_VAL = 1
MAX_VAL = 6

def rolling_dice():
    """Function returns the random value between 1 to 6"""
    return random.randint(MIN_VAL, MAX_VAL)

MYLIST = []

print("------------------------------------------")
print("++++++ WELCOME TO ROLLING DICE GAME ++++++")
print("------------------------------------------")
print("RULE:")
print("You have 2 chances to ROLL the DICE")
print("------------------------------------------")

for i in range(2):
    input_1 = input("Do you want to roll dice?")
    input_1 = input_1.lower()
    while input_1 != 'yes' and input_1 != 'y' and input_1 != 'no' and input_1 != 'n':
        print("Invalid input")
        print("\nPlease enter Yes or NO")
        input_1 = input("\nDo you want to play? ")
        input_1 = input_1.lower()
    if input_1 in ('yes', 'y'):
        if i > 0:
            print("previous number was:", MYLIST[0])
        dice_num = rolling_dice()
        MYLIST.append(dice_num)
        print("Number on dice is: ", dice_num)
        if dice_num == 6:
            print("JACKPOT")
    elif input_1 in ('no', 'n'):
        print("Exiting the GAME")
        break
print("________________FINISHED__________________")
