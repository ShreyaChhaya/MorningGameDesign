#shreya chhaya
#write code that tells if number input by user is even or odd 
#if number is multiple of 3 or 5
from asyncio import events
import os
os.system('cls')
number=int(input('your number is'))
if (number%2==0):
    print('number is even')
else:
    print('number is odd')
if (number%3==0):
    print ('this is a multiple of three')
if (number%5==0):
    print('this is a multiple of five')
if (number%3==0 and number%5==0):
    print('this is a multiple of three and five')




