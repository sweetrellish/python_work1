import hearts
import diamonds
import clubs
import spades
#import all card types

cardDeck = []
plus = 0
while plus < 13:
    cardDeck.append(hearts.heart_deck[plus])
    cardDeck.append(diamonds.diamond_deck[plus])
    cardDeck.append(clubs.club_deck[plus])
    cardDeck.append(spades.spade_deck[plus])
    plus += 1
#assign values of types to entire deck list

print("\n\nHere's the entire deck:")
count = 0 
while count < 52:
    print (cardDeck[count])
    count += 1
#print values of entire deck



