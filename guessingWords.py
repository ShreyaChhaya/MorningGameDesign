#Shreya Chhaya
#make list of words and select one randomly
#give instructions to user
#give hint about type of word and how many letters and let them input guess
#if guess wrong, give one letter and continue for 3 tries
#if guessed write "you won!" and if not write "you lost"
import random 
import os
os.system('cls')
wordList=['elephant', 'platypus', 'spider', 'gorilla', 'armadillo', 'bobcat', 'giraffe', 'penguin', 'vulture', 'catfish', 'octopus', 'dolphin' ]
print('Hello!')
print('This is "Guess The Word!"')
print('********************************************************************************************************************************************')
print('First, I wil give you a hint about waht kind of word you have to guess and the number of letters in the word. You will guess the word you think it is, and if you get it wrong, one letter in the word will be provided for you. You are allowed three guesses, getting a new letter each time.')
print('********************************************************************************************************************************************')
print('                                             ')
print("Let's get started!")
print('                                             ')
print('Your first hint is...this word is an animal')
print('                                             ')

word=random.choice(wordList)
if word is (wordList[0]):
    print('Number of Letters: _ _ _ _ _ _ _ _')

if word is (wordList[1]):
    print('Number of Letters: _ _ _ _ _ _ _ _')

if word is (wordList[2]):
    print('Number of Letters: _ _ _ _ _ _')

if word is (wordList[3]):
    print('Number of Letters: _ _ _ _ _ _ _')

if word is (wordList[4]):
    print('Number of Letters: _ _ _ _ _ _ _ _ _')

if word is (wordList[5]):
    print('Number of Letters: _ _ _ _ _ _')

if word is (wordList[6]):
    print('Number of Letters: _ _ _ _ _ _ _')

if word is (wordList[7]):
    print('Number of Letters: _ _ _ _ _ _ _')

if word is (wordList[8]):
    print('Number of Letters: _ _ _ _ _ _ _')

if word is (wordList[9]):
    print('Number of Letters: _ _ _ _ _ _ _')

if word is (wordList[10]):
    print('Number of Letters: _ _ _ _ _ _ _')

if word is (wordList[11]):
    print('Number of Letters: _ _ _ _ _ _ _')
print('                                         ')
guess1=input("Your first guess is ")
if guess1==word:
    print("That's right! Congragulations, you win!")
else:
    print('That is incorrect! One letter will be provided for you.')
    print('                                                      ')
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
    guess2=input("Your second guess is ")
    if guess2==word: 
        print('You are correct! You win!')
    else:
        print('Wrong again! One more guess! Another letter from the word will be given to you.')
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
        guess3=input('Your final guess is ')
        if guess3==word:
            print('You are correct! You win!')
        else:
            print('That is incorrect. You lose. Better luck next time!')
            print('                                            ')


        








