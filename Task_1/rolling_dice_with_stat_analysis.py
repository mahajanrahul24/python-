# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 16:49:00 2018

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
    if input_1 in ('yes', 'y'):
        if i > 0:
            print("previous number was:", MYLIST[0])
        dice_num = rolling_dice()
        MYLIST.append(dice_num)
        print("Number on dice is: ", dice_num)
        if dice_num == 6:
            print("JACKPOT")
    else:
        print("Run program again and press yes on keyboard")
        break
print("________________FINISHED__________________")
