import random
#taking user's input 
amount= int(input("Enter the amount that you will be investing:"))
years= int(input("Enter how many years are you going to keep it as an investment:"))
rate_min= float(input("Enter the minimum rate of interest:"))
rate_max= float(input("Enter the maximum rate of interest:"))

def simulate_investment (amount, years, rate_min, rate_max):
    rate= random.uniform(rate_min,rate_max) #generating random rate to use in equation
    # using simple PTR equation
    interest= (amount * years * rate) / 100
    final_amt= amount + interest
    print(f'the interest rate applied is: {rate:.2f}')
    print (f'The final amount is ..: {final_amt:.2f}')

simulate_investment(amount, years, rate_min, rate_max)