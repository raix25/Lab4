temp= float(input("enter the temperature:"))

c_to_f= (temp* 9/5) +32 #converting celcius to ferenheit 
f_to_c= (temp-32) *5/9 #converting ferenheit to celcius 

def convert_temperature(temp):
    print("converting the temperature to Fahrenheit", c_to_f)
    print("converting the temperature to Celsius", f_to_c)

convert_temperature(temp)