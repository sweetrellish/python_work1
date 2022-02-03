import hearts
import diamonds
import clubs
import spades

plus = 0
while plus < 13:
    cardDeck = [f"{hearts.heart_deck[plus]}", f"{diamonds.diamond_deck[plus]}", f"{clubs.club_deck[plus]}", f"{spades.spade_deck[plus]}"]
count = 0 
while count < 3:
    print (cardDeck[count])
    count += 1



