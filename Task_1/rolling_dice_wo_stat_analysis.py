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
    input_1=input("Do you want to play? \n")
    input_1=input_1.lower()
    while input_1 != 'yes' and input_1 != 'y' and input_1 != 'no' and input_1 != 'n':
        print("Invalid input")
        print("\nPlease enter Yes or NO")
        input_1=input("\nDo you want to play? ")
        input_1=input_1.lower() 
    if(input_1=="yes" or input_1=="y"):
        if(i>0):
            print("previous number was:", mylist[0])        
        dice_num=rolling_dice()
        mylist.append(dice_num)
        print ("Number on dice is: ", dice_num)
        if(dice_num==6):
            print("JACKPOT")
    elif (input_1=="no" or input_1=="n"):
        print("Exiting the GAME")
        break 
     
print("________________FINISHED__________________")