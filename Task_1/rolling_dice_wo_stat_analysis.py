import random
min_val = 1
max_val = 6

def rolling_dice():
    return random.randint(min_val, max_val)
            
mylist=[]

print("------------------------------------------")
print("++++++ WELCOME TO ROLLING DICE GAME ++++++")
print("------------------------------------------")
print("RULE:")
print("You have 2 chances to ROLL the DICE")
print("------------------------------------------")

for i in range(2):
    input_1 = input("Do you want to roll dice?")
    if(input_1=="yes" or input_1=="y" or input_1=="Y" or input_1=="YES"  or input_1=="Yes"):
        if(i>0):
            print("previous number was:", mylist[0])        
        dice_num=rolling_dice()
        mylist.append(dice_num)
        print ("Number on dice is: ", dice_num)
        if(dice_num==6):
            print("JACKPOT")
    else:
        print("Run program again and press yes on keyboard")
        break
print("________________FINISHED__________________")