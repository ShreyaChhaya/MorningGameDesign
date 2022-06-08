#Shreya Chhaya
#make list of words and select one randomly
#give instructions to user
#give hint about type of word and how many letters and let them input guess
#if guess wrong, give one letter and continue for 3 tries
#if guessed write "you won!" and if not write "you lost"
import random 
import os, datetime
date=datetime.datetime.now()
from subprocess import HIGH_PRIORITY_CLASS
os.system('cls')
wordList=['elephant', 'platypus', 'spider', 'gorilla', 'armadillo', 'bobcat', 'giraffe', 'penguin', 'vulture', 'catfish', 'octopus', 'dolphin' ]
wordList2=['apple', 'banana', 'orange', 'pineapple', 'mango', 'watermelon', 'plum', 'peach', 'strawberry', 'blueberry']
wordList3=['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'pink', 'black', 'white', 'gray']
Game=True
cnt=0
name=input('What is your name? ')
#a function in a section the prram that we call when we need it
while Game:
    high=0
    gamec=True
    while gamec:
        print('Hello!')
        #add user's name here to make it more personal and for keeping score
        print(name, 'This is "Guess The Word!')
        print('********************************************************************************************************************************************')
        print('First, I wil give you a hint about what kind of word you have to guess and the number of letters in the word. You will guess the word you think it is, and if you get it wrong, one letter in the word will be provided for you. You are allowed three guesses, getting a new letter each time.')
        print('********************************************************************************************************************************************')
        print('                                             ')
        print('would you like to play game 1,Guess the Animal, game 2, Guess the Fruit, or game 3, Guess the Color')
        choice=input('Please write your choice as 1, 2, or 3.')
        print("Let's get started!")
        print('                                             ')
        print('                                             ')
        
        try: 
            choice=int(choice)
            if choice>0 and choice<4:
                gamec=False
            else: 
                print('I said give me 1, 2, or 3')
        except:
            print('sorry, that is not even a number. type 1, 2 or 3.')


        if choice==1:  
            word=random.choice(wordList)
            print('Your first hint is...this word is an animal. you will also recieve one letter from the word')
            if word is (wordList[0]):
                print('Hint: _ _ _ p _ _ _ _')
            if word is (wordList[1]):
                print('Hint: p _ _ _ _ p _ _')
            if word is (wordList[2]):
                print('Hint: _ _ _ d _ _')
            if word is (wordList[3]):
                print('Hint: _ o _ _ _ _ _')
            if word is (wordList[4]):
                print('Hint: a _ _ a _ _ _ _ _')
            if word is (wordList[5]):
                print('Hint: b _ b _ _ _')
            if word is (wordList[6]):
                print('Hint: _ _ _ _ f f _')
            if word is (wordList[7]):
                print('Hint: _ _ _ g _ _ _')
            if word is (wordList[8]):
                print('Hint: v _ _ _ _ _ _')
            if word is (wordList[9]):
                print('Hint: _ _ _ _ _ _ h')
            if word is (wordList[10]):
                print('Hint: o _ _ o _ _ _')
            if word is (wordList[11]):
                print('Hint: _ _ _ _ _ _ n')
            print('                                   ')
            cnt+=1
            guess1=input("Your first guess is ")
            if guess1==word: 
                print('You are correct! You win!')
                SayScore=True
            else:
                print('Wrong! One more guess! Another letter from the word will be given to you.')
                print('                                                ')
                if word is (wordList[0]):
                    print('Hint: e _ e p _ _ _ _')
                if word is (wordList[1]):
                    print('Hint: p _ _ _ y p _ _')
                if word is (wordList[2]):
                    print('Hint: s _ _ d _ _')
                if word is (wordList[3]):
                    print('Hint: _ o _ _ l l _')
                if word is (wordList[4]):
                    print('Hint: a _ _ a _ _ l l _')
                if word is (wordList[5]):
                    print('Hint: b _ b c _ _')
                if word is (wordList[6]):
                    print('Hint: g _ _ _ f f _')
                if word is (wordList[7]):
                    print('Hint: _ _ n g _ _ n')
                if word is (wordList[8]):
                    print('Hint: v u _ _ u _ _')
                if word is (wordList[9]):
                    print('Hint: c _ _ _ _ _ h')
                if word is (wordList[10]):
                    print('Hint: o _ _ o p _ _')
                if word is (wordList[11]):
                    print('Hint: _ _ l _ _ _ n')
                print('                                       ')
                cnt+=1
                guess2=input('Your final guess is ')
                if guess2==word:
                    print('You  correct! You win!')
                else:
                    print('That is incorrect. You lose. Better luck next time!')
                    print('                                            ')
           
        if choice==2:
            word2=random.choice(wordList2)
            print('Your first hint is, this word is a fruit. You will also recieve the number of letters in the word and one letter from the word')
            if word2 is (wordList2[0]):
                print('Hint: _ p p _ _ ')
            if word2 is (wordList2[1]):
                print('Hint: _ a _ a _ a ')
            if word2 is (wordList2[2]):
                print('Hint: _ _ _ _ g _')
            if word2 is (wordList2[3]):
                print('Hint: p _ _ _ _ p p _ _')
            if word2 is (wordList2[4]):
                print('Hint: m _ _ _ _')
            if word2 is (wordList2[5]):
                print('Hint: _ _ _ e _ _ e _ _ _')
            if word2 is (wordList2[6]):
                print('Hint: _ l _ _')
            if word2 is (wordList2[7]):
                print('Hint: _ _ _ c _')
            if word2 is (wordList2[8]):
                print('Hint: _ _ _ _ _ _ _ r r _')
            if word2 is (wordList2[9]):
                print('Hint: _ _ _ e _ e _ _ _')
            print(' ')
            cnt+=1
            guess3=input('your first guess is: ')
            if guess3==word2:
                print (" That's right!")
            else: 
                print('Wrong! One more guess! Here is your second hint:')
                print('   ')
                if word2 is (wordList2[0]):
                    print('Hint: a p p _ _ ')
                if word2 is (wordList2[1]):
                    print('Hint: b a _ a _ a ')
                if word2 is (wordList2[2]):
                    print('Hint: _ _ _ _ g e')
                if word2 is (wordList2[3]):
                    print('Hint: p _ _ e _ p p _ e')
                if word2 is (wordList2[4]):
                    print('Hint: m _ _ _ o')
                if word2 is (wordList2[5]):
                    print('Hint: w _ _ e _ _ e _ _ _')
                if word2 is (wordList2[6]):
                    print('Hint: _ l _ m')
                if word2 is (wordList2[7]):
                    print('Hint: p _ _ c _')
                if word2 is (wordList2[8]):
                    print('Hint: _ _ _ _ w _ _ r r _')
                if word2 is (wordList2[9]):
                    print('Hint: b _ _ e b e _ _ _')
                print('  ')
                cnt+=1
                guess4=input('Your final guess is: ')
                if guess4==word2:
                    print('You got it! Congrats!')
                else:
                    print('wrong again! You Lose.')
           
        if choice==3:
            word3=random.choice(wordList3)
            print('Your first hint is that the word is a color. One letter, as well as the number of letters in the word will be provided for you')
            if word3 is (wordList3[0]):
                print('Hint: _ e _ ')
            if word3 is (wordList3[1]):
                print('Hint: _ _ _ _ g _ ')
            if word3 is (wordList3[2]):
                print('Hint: _ _ _ _ o _')
            if word3 is (wordList3[3]):
                print('Hint: _ _ e e _')
            if word3 is (wordList3[4]):
                print('Hint: _ _ u _')
            if word3 is (wordList3[5]):
                print('Hint: _ _ _ _ l _')
            if word3 is (wordList3[6]):
                print('Hint: _ _ n _')
            if word3 is (wordList3[7]):
                print('Hint: _ _ a _ _')
            if word3 is (wordList3[8]):
                print('Hint: _ h _ _ _')
            if word3 is (wordList3[9]):
                print('Hint: g _ _ _')
            print(' ')
            cnt+=1
            guess5=input('Your first guess is: ')
            if guess5==word3:
                print('You got it! Congrats!')
            else:
                print('Incorrect. One more shot.')
                print(' ')
                if word3 is (wordList3[0]):
                    print('Hint: r e _ ')
                if word3 is (wordList3[1]):
                    print('Hint: _ r _ _ g _ ')
                if word3 is (wordList3[2]):
                    print('Hint: _ _ l l o _')
                if word3 is (wordList3[3]):
                    print('Hint: _ _ e e n')
                if word3 is (wordList3[4]):
                    print('Hint: _ l u _')
                if word3 is (wordList3[5]):
                    print('Hint: p _ _ p l _')
                if word3 is (wordList3[6]):
                    print('Hint: _ _ n k')
                if word3 is (wordList3[7]):
                    print('Hint: b _ a _ _')
                if word3 is (wordList3[8]):
                    print('Hint: _ h _ t _')
                if word3 is (wordList3[9]):
                    print('Hint: g _ _ y')
                print('   ')
                cnt+=1
                guess5=input('Your final guess is: ')
                if guess5==word3:
                    print('You got it! Congrats!')
                else:
                    print('wrong again. better luck next time!')
    print('        ')
    print('Thank you for playing!')
    playAgain=input('Do you want to play again? If you want to play again, type "yes". if you dont want to play again, type "no" ')
    print('   ')
    if playAgain=="yes":
        Game=True 
    else:
        print('ok, bye!')
        break

score=2000-40*cnt
if score >  high: 
    high=score 
print(name+ 'your score is '+str(score))

input('press enter')
os.system('cls')

cnt==0
print('your highest score is '+ str(score))
myFile=open('guess_game.txt', 'a')
scrLine=str(score)+"\t"+name + "\t" + date.strftime("%m=%d-%Y")+ "\n"
myFile.write(scrLine)
myFile.close



            








