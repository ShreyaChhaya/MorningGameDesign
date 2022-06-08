#Shreya Chhaya
#calculate BMI
#get weight and height
import os
os.system('cls')
weight=int(input('Your weight in pounds')) #get weight
height=int(input('your height in inches')) #get height
BMI=weight/(height*height)*703 #put values into formula
print('your BMI is', BMI)  #give answer to user
if BMI<18.5:
    print('unweight') #tells if under or overweight
if BMI>24.9:
    print('overweight')

