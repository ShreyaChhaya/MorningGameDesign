#Shreya Chhaya
#calculate BMI
#get weight and height
import os
os.system('cls')
weight=int(input('Your weight in pounds'))
height=int(input('your height in inches'))
BMI=weight/(height*height)*703
print('your BMI is', BMI) 
if BMI<18.5:
    print('unweight')
if BMI>24.9:
    print('overweight')
