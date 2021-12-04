
import random
       

#sets hands to blank
dealerHand = []
playerHand = []
playerScore = 0
dealerScore = 0

def pick_up_card(newHand, sourceHand):
    newHand.append(sourceHand.pop(0))

def score_calc(sourceHand, sourceScore):
    for numbers in range(len(sourceHand)):
            if(sourceHand[numbers][0] == 'J' or playerHand[numbers][0] == 'Q' or playerHand[numbers][0] == 'K'):
                scoreEquiv = 10
                sourceScore += scoreEquiv
            elif(sourceHand[numbers][0] == 'Ace'):
                if sourceScore + 11 > 
                scoreEquiv = 11
                sourceScore += scoreEquiv
            else:
                scoreEquiv = playerHand[numbers][0]
                sourceScore += scoreEquiv
            if playerScore > 21 and 'Ace' in playerHand:
                playerScore -= 10
    



#attempts at a deck via list

##constructs deck with suits, face cards and number values
lstdeck = []
facecards = ['J', 'Q', 'K', 'Ace']
suits = [' Clubs', ' Diamonds', ' Hearts', ' Spades']
for numbers in range(2,11,1):
    for suit in suits:
        lstdeck.append((numbers, suit))

for faces in facecards:
    for suit in suits:
        lstdeck.append((faces, suit))

#shuffles deck once complete
random.shuffle(lstdeck)

#deals to player and dealer
pick_up_card(playerHand, lstdeck)
pick_up_card(dealerHand, lstdeck)
pick_up_card(playerHand, lstdeck)
pick_up_card(dealerHand, lstdeck)

print("You have " + str(playerHand) + " in your hand")
print("\nThe dealer has " + str(dealerHand) + " in their hand")


#Prints out total score right now for player
for numbers in range(len(playerHand)):
        if(playerHand[numbers][0] == 'J' or playerHand[numbers][0] == 'Q' or playerHand[numbers][0] == 'K'):
            scoreEquiv = 10
            playerScore += scoreEquiv
        elif(playerHand[numbers][0] == 'Ace'):
            scoreEquiv = 11
            playerScore += scoreEquiv
        else:
            scoreEquiv = playerHand[numbers][0]
            playerScore += scoreEquiv
if playerScore > 21 and 'Ace' in playerHand:
    playerScore -= 10
    
print("\nYou total score right now: " + str(playerScore))


#dealer logic




print("\nThe deck has " + len(lstdeck) + " remaining.")

#player score
while playerScore <= 21:
    print("You have " + str(playerHand) + " in your hand. Please push lowercase y to get hit.")
    answer = input()
    if answer == 'y':
        pick_up_card(playerHand, lstDeck)
        for numbers in range(len(playerHand)):
            if(playerHand[numbers][0] == 'J' or playerHand[numbers][0] == 'Q' or playerHand[numbers][0] == 'K'):
                scoreEquiv = 10
                playerScore += scoreEquiv
            elif(playerHand[numbers][0] == 'Ace'):
                scoreEquiv = 11
                playerScore += scoreEquiv
            else:
                scoreEquiv = playerHand[numbers][0]
                playerScore += scoreEquiv
            if playerScore > 21 and 'Ace' in playerHand:
                playerScore -= 10
    if dealerScore < 16:
        print("As score is less than 16, dealer will hit.\n")
        pick_up_card(dealerHand, lstdeck)
    elif dealerScore > 21:
        print("Dealer busts. You win!!!")
    elif dealerScore == 21:
        print("Dealer gets Blackjack! You lose!")
    else:
        print("Dealer will stay.")
    print(playerScore)
    
print("\n\n\nYou busted!!!")
