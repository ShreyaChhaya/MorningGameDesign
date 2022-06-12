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
while game <50:
    player1Card=pickCard(player1)
    player2Card=pickCard(player2)
    #pick winner of round - who has biggest card gets both 
    if cardDict[player1Card] > cardDict[player2Card]: 
        print(player1, ' has the bigger card!')
        biggest=player1
        player1_score+=2
        player2_score-=2
        player1Deck.append(player1Card, player2Card)
        print(player1, ' has the score: ', player1_score)
        print(player2, ' has the score: ', player2_score)
        print(player1, player1Deck)
        print(player2, player2Deck)
    elif cardDict(player1Card) < cardDict(player2Card):
        print(player2, ' has the biggest card!')
        biggest=player2
        player1_score-=2
        player2_score+=2
        player2Deck.append(player1Card, player2Card)
        print(player1, ' has the score: ', player1_score)
        print(player2, ' has the score: ', player2_score)
        print(player1, player1Deck)
        print(player2, player2Deck)
    #if round ends in tie 
    if cardDict(player1Card)==cardDict(player2Card):
        print('There is a tie. Both players will draw again')
        player1Card=pickCard(player1)
        player2Card=pickCard(player2)

    if len(player1Deck)>len(player2Deck):
        winner=player1
    if len(player2Deck)>len(player1Deck):
        winner=player2
    if len(deck)==0:
        print('Game over. ', biggest, ' wins the game')
        game=False







