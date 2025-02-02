import random
num_dice= int(input("How many dice do you have?")) #taking user's input in the number of dice

def roll_dice (num_dice):
    num_sides= [1,2,3,4,5,6] #number of sides of dice is six
    for x in range(num_dice):
        random_num= random.randint(1,6) #randomizing the number
        print ("DICE", x +1 , ':',random_num) #showing result for each dice
roll_dice(num_dice)
