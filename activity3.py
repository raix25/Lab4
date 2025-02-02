import random

min_val= int(input("enter the minimum value:"))
max_val= int(input("enter the maximum value:"))

def generate_random_number(min_val,max_val):
 random_num= random.randint(min_val,max_val) #generating random number using user's input for minimum and maximum value
 print ("The random number is:", random_num)

generate_random_number(min_val,max_val)