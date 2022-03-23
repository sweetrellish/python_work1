def deal_top_card(deck):
    """Takes deck argument and returns top card value and removes from the deck"""
    card = deck.pop(deck[0])
    print(f'Here is the top card {card}')

def get_random_card(deck):
    """Given argument deck, returns random card in deck."""
    from random import randrange
    num = randrange(52)
    card = deck.pop(num)
    print(card)

def shuffle_deck(deck):
    """Takes deck argument and returns shuffled deck."""
    from random import randrange
    # for card in deck:
        # print(card)
    for card in deck:
        num = randrange(52)
        card = deck[num]
        # print(card)

def deal_hands(deck, hand_num, hands):
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
    for card in range(hand):
        print(deck.pop(card))



