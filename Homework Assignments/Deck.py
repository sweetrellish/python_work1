"""Module containing functions that relate to card and deck manipulation"""
class Deck:
    """Class defining a deck of cards, and contains methods of deck functions"""
    def __init__(self):
        self.values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        self.suits = ['♠','♥','♦','♣']
        
        deck = []
        for suit in self.suits:
            for value in self.values:
                card = value + suit
                deck.append(card)

        self.deck = deck
    #creates deck   
    def deal_top_card(self):
        """Takes deck argument and returns top card value and removes from the deck"""
        card = self.deck.pop(0)
        return card
    #returns top card from deck

    def get_random_card(self):
        """Given argument deck, returns random card in deck."""
        from random import randrange
        num = randrange(52)
        card = self.deck.pop(num)
        return card
    #returns random card from the deck, removes from deck

    def shuffle_deck(self):
        """Takes deck argument and returns shuffled deck."""
        import random
        random.shuffle(self.deck)
        return self.deck
    #shuffles deck

    def deal_hands(self, hand_num, hands = 1):
        """Takes deck, hand amount and number of hands and returns the hands."""
        wcount = 0
        fcount = 0
    
        new_hands = {}
    
        while wcount < hands:
            for card in range(hand_num):     
                card = self.deck.pop(fcount)
                new_hands[f'{wcount}'].append(card)
                fcount += 1
            wcount += 1
        return new_hands
    #deals multiple hands
        

    def deal_hand(self, hand):
        """Takes argument for one hand only and returns hand."""
        new_hand =[]
        for card in range(hand):
            new_hand.append(self.deck.pop(card))
        return new_hand
    #deals hand to user/computer, removes cards from deck

class Card(Deck):
    """Class defining methods for card manipulation"""
    def __init__(self):
        """Initialize parent class"""
        super().__init__()
        

    def get_suit(self):
        return self.card[-1]
    #returns suit of card

    def same_Value(card1, card2):
        """Takes number of cards and tests value equivalency of each card."""
        value1 = card1[0]
        value2 = card2[0]
        if value1 == value2:
            return True
        else:
            return False
    #checks if card values are equivalent

    def same_Suit(card1, card2):
        """Takes suit of cards and tests equivalency of each card."""
        suit1 = card1[-1]
        suit2 = card2[-1]
        if suit1 == suit2:
            return True
        else:
            return False
    #checks if card suits are equivalent

    def get_Value(card):
            """Takes in card argument and returns number value of that card."""
            value = card[0]
            return value
    #returns value of card number