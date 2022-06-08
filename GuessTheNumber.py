#Shreya Chhaya
import random
import os
os.system('cls')

name=input('What is your name? ')
print('Nice to meet you', name)
goMenu=input('Press m to go to the main menu ')
Game=True 
while Game:
    if 'm':
        print('                    ')
        print('Menu:')
        print('Click 1 for Instructions')
        print('Click 2 to play Level 1')
        print('Click 3 to play Level 2')
        print('Click 4 to play Level 3')
        print('Click 5 to see your score')
        print('Click 6 to end game')
        choice=input('choose 1-6 to reach your desired destination: ')

    if choice=='1':
        print('           ')
        print('Instructions: ')
        print('From the main menu, click 2, 3, or 4, depending on the level of difficulty you want the game to be.')
        print('Level 1 includes numbers 1-25, level 2 includes numbers 1-50, and level 3 includes numbers 1-100')


    

