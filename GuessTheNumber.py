#Shreya Chhaya
import random
import os, datetime
os.system('cls')
import time

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
        guessing = True 
        if choice== '1':
            print('           ')
            print('This is Guess the Number!')
            print('       ')
            print('Instructions: ')
            print('You will guess a number, and depending on the number you guess, you will be told if the answer is higher or lower than your number until you get the answer.')
            print('From the main menu, click 2, 3, or 4, depending on the level of difficulty you want the game to be.')
            print('Level 1 includes numbers 1-25, level 2 includes numbers 1-50, and level 3 includes numbers 1-100')
            guessing = False
            time.sleep(5)
        elif choice =='2':
            theNum= random.randint(1,25)
            print('Guess a number from 1 to 25.')
            max=25
        elif choice =='3':           
            theNum= random.randint(1,50)
            print('Guess a number from 1 to 50.')
            max=50
        elif choice =='4':
            theNum= random.randint(1,100)
            print('Guess a number from 1 to 100.')
            max=100
        #I want them to guess again - loop
        if choice =='5': 
            print(name, 'your score is: ',(score))
            time.sleep(3)
            high = 0
            if score>high:
                high=score
            two=0
            if score>two and score<high:
                two=score
            three =0
            if score>three and score<two:
                three=score
            four=0
            if score>four and score<three:
                four=score
            five=0
            if score>five and score<four:
                five=score
            date=datetime.datetime.now()
            scrLine=str(high)+"\t " +name + "\t" +date.strftime('%m/%d/%Y')+ "\n"
            scrLine2=str(two)+"\t " +name + "\t" +date.strftime('%m/%d/%Y')+ "\n"
            scrLine3=str(three)+"\t " +name + "\t" +date.strftime('%m/%d/%Y')+ "\n"
            scrLine4=str(four)+"\t " +name + "\t" +date.strftime('%m/%d/%Y')+ "\n"
            scrLine5=str(five)+"\t " +name + "\t" +date.strftime('%m/%d/%Y')+ "\n"
            myFile=open('scre.txt', 'w')
            myFile.write(scrLine+scrLine2+scrLine3+scrLine4+scrLine5)
            myFile.close()
            myFile = open("scre.txt", 'r')
            stuff=myFile.readlines()
            stuff.sort(reverse=True)
            myFile.close()
            for line in stuff:
                print(line)
            guessing = False 
            time.sleep(5)
        if choice == '6':
            print('ok, bye!')
            Game = False 
            guessing = False # making guessing false so ends game
        count=0 

        while(guessing):
            guess=int(input('Your guess is: '))
            count +=1
            if guess==theNum:
                print('Congrats! You got it! Wait for the menu to appear.')
                time.sleep(3)
                score = max-count
                #higher level gives more points
                guessing = False
            if guess>theNum:
                print('Hint: the correct answer is lower than', guess) 
            if guess<theNum:
                print('Hint: The correct answer is higher than', guess)
 
        
