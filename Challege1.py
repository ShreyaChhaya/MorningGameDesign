#first let's import random procedures since we will be shuffling
import random, os, enum
os.system('cls')
deck=[]
#next, let's start building list holders so we can place our cards in there:
def create_DECK():
    global deck
    numberCards = []
    suits = ["♥️","♦️", "♣️", "♠️"]
    royals = ["J", "Q", "K", "A"]
    

    #now, let's start using loops to add our content:
    for i in range(2,14):
        numberCards.append(str(i))
        #this adds numbers 2-10 and converts them to string data

    for j in range(4):
        numberCards.append(royals[j])
        #this will add the royal faces to the cardbase

    
    for k in range(4):
        for l in range(13):
            card = (numberCards[l] + " " + suits[k])
            #this makes each card, cycling through suits, but first through faces
            deck.append(card)
            #this adds the information to the "full deck" we want to make

    #now let's see the cards!
    counter=0
    for row in range(4):
        for col in range(13):
            print(deck[counter], end=" ")
            counter +=1
        print()
    #now let's shuffle our deck!
def playerCards():
    random.shuffle(deck)
    player1=[]
    player2=[]
    for l in range(52):
        if l%2==0:
            player1.append(deck[l])
        else:
            player2.append(deck[l])
    print("player1 ",player1)
    print()
    print("player2 ",player2)
    #I also want to see what the deck looks like before shuffling. We should have
        #done that a while ago... oh well!
create_DECK()
playerCards()

#My turn: 

#give each card a value in order to compare bigger or smaller
cardDict={'A ♥️': 1, '2 ♥️': 2, '3 ♥️': 3, '4 ♥️': 4, '5 ♥️': 5, '6 ♥️': 6, '7 ♥️': 7, '8 ♥️': 8, '9 ♥️': 9, '10 ♥️': 10, 'J ♥️': 11, 'Q ♥️': 12, 'K ♥️': 13, 'A ♦️': 1, '2 ♦️': 2, '3 ♦️': 3, '4 ♦️': 4, '5 ♦️': 5, '6 ♦️': 6, '7 ♦️': 7, '8 ♦️': 8, '9 ♦️': 9, '10 ♦️': 10, 'J ♦️': 11, 'Q ♦️': 12, 'K ♦️': 13, 'A ♣️': 1, '2 ♣️': 2, '3 ♣️': 3, '4 ♣️': 4, '5 ♣️': 5, '6 ♣️': 6, '7 ♣️': 7, '8 ♣️': 8, '9 ♣️': 9, '10 ♣️': 10, 'J ♣️': 11, 'Q ♣️': 12, 'K ♣️': 13, 'A ♠️': 1, '2 ♠️': 2, '3 ♠️' :3, '4 ♠️': 4, '5 ♠️': 5, '6 ♠️': 6, '7 ♠️': 7, '8 ♠️': 8, '9 ♠️': 9, '10 ♠️': 10, 'J ♠️': 11, 'Q ♠️': 12, 'K ♠️': 13}
#define player
print()
player1=input('Player 1, input your name: ')
player2=input('Player 2, input your name: ')
#first score is the number of cards per person
player1_score=26
player2_score=26
player1Deck=[]
player2Deck=[]
print()
#each player draws first card from deck
def pickCard(player):
    card=deck[0]
    deck.remove(deck[0])
    print(player + ' drew ' + str(card))


game=0
z=0
while game <50:
    player1Card=pickCard(player1) #here i want the pick card function to apply to each of the players
    player2Card=pickCard(player2)
    #ERROR IN CODE:
    #next lines (82,8, and 853) do not work-i realized you cannot compare teh value of two playing cards so 
    # i made a dictionary above giving each card a numerical value.
    #then i wanted to compare teh numerical values of each card instead of the cards themselves to see which is bigger
    #i knew my logic would work but i didn't know how to change it to the number value
    #below i tried to say that the value of each card is the dictionary number corresponding with the card
    #but this is the innocrect way to figure it out
    # I believe that the rest of my code would work properly if I could figure out this one part
    #However, i'm unable to compare the numerical value of the card and therefore, the code does not continue
    #from this point due to the error in my syntax

    card1Value=cardDict[player1Card]  
    card2Value=cardDict[player2Card]
    #pick winner of round - who has biggest card gets both 
    if card1Value > card2Value: 
        print(player1, ' has the bigger card!')
        biggest=player1
        player1_score+=1 #changes each player's score accordingly
        player2_score-=1
        player1Deck.append(player1Card, player2Card) #since card was removed from deck before - add both cards to winner deck
        print(player1, ' has the score: ', player1_score)
        print(player2, ' has the score: ', player2_score) #print scores
        print(player1, player1Deck) #print deck
        print(player2, player2Deck)
    elif cardDict(player1Card) < cardDict(player2Card): # do the same as before but with the opposite 
        print(player2, ' has the biggest card!')
        biggest=player2
        player1_score-=1
        player2_score+=1
        player2Deck.append(player1Card, player2Card)
        print(player1, ' has the score: ', player1_score)
        print(player2, ' has the score: ', player2_score)
        print(player1, player1Deck)
        print(player2, player2Deck)
    #if round ends in tie 
    if cardDict(player1Card)==cardDict(player2Card): #if there's a tie-pick again
        print('There is a tie. Both players will draw again')
        player1Card=pickCard(player1)
        player2Card=pickCard(player2)
    if game>=50: #once 50 rounds is over
        if len(player1Deck)>len(player2Deck): #winner has the bigger deck at the end
            winner=player1
        if len(player2Deck)>len(player1Deck):
            winner=player2
        if len(deck)==0: #if no more cards left, person with cards left wins 
            print('Game over. ', winner, ' wins the game')
            game=False







