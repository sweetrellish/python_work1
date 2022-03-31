def deal_top_card(deck):
    """Takes deck argument and returns top card value and removes from the deck"""
    card = deck.pop(0)
    print(card)
    return card
    #print(f'Here is the top card {card}')

def get_random_card(deck):
    """Given argument deck, returns random card in deck."""
    from random import randrange
    num = randrange(52)
    card = deck.pop(num)
    print(card)
    return card

def shuffle_deck(deck):
    """Takes deck argument and returns shuffled deck."""
    import random
    random.shuffle(deck)
    return deck

def deal_hands(deck, hand_num, hands = 1):
    """Takes deck, hand amount and number of hands and returns the hands."""
    wcount = 0
    fcount = 0
    new_hand = []
    while wcount < hands:
        for card in range(hand_num):     
            card = deck.pop(fcount)
            print(card)
            new_hand.append(card)
            fcount += 1
        wcount += 1
    return new_hand
    

def deal_hand(deck, hand):
    """Takes argument for one hand only and returns hand."""
    #print("Here is your starting hand:\n")
    new_hand =[]
    for card in range(hand):
        new_hand.append(deck.pop(card))
        print(new_hand[card])
    return new_hand

from card_functions import build_deck

deck = build_deck()
shuffle_deck(deck)
# deal_top_card(deck)
# get_random_card(deck)
#deal_hand(deck, 7)
#deal_hands(deck, 7)

#All functions are working as needed 3/24/22