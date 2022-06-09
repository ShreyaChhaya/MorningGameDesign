#Shreya Chhaya
import random
import os
os.system('cls')

name=input('What is your name? ')
print('Nice to meet you', name)
Game=True 
while Game:
        print('                    ')
        print('Menu:')
        print('Click 1 for Instructions')
        print('Click 2 to play Level 1')
        print('Click 3 to play Level 2')
        print('Click 4 to play Level 3')
        print('Click 5 to see your score')
        print('Click 6 to end game')
        choice=input('choose 1-6 to reach your desired destination: ')
        os.system('cls')
        if choice== '1':
            print('           ')
            print('This is Guess the Number!')
            print('       ')
            print('Instructions: ')
            print('You will guess a number, and depending on the number you guess, you will be told if the answer is higher or lower than your number until you get the answer.')
            print('From the main menu, click 2, 3, or 4, depending on the level of difficulty you want the game to be.')
            print('Level 1 includes numbers 1-25, level 2 includes numbers 1-50, and level 3 includes numbers 1-100')
            print('        ')
            goMenu=input('Click m to return to the main menu and begin the game: ')
            os.system('cls')
        if choice =='2':
            theNum= random.randint(1,25)
            print('Guess a number from 1 to 25.')
        if choice =='3':           
            theNum= random.randint(1,50)
            print('Guess a number from 1 to 50.')
        if choice =='4':
            theNum= random.randint(1,100)
            print('Guess a number from 1 to 100.')
        guess=input('Your guess is: ')
        if guess==theNum:
            print('Congrats! You got it!')
            goMenu=input('Click m to return to the main menu. Then you can play again, see your score, or end the game: ')
        if guess>theNum:
            print('Hint: The number is lower than your first guess') 
        if guess<theNum:
            print('Hint: The answer is higher than the number you guessed')

    
