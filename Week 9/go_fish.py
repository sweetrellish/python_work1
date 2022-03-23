from random import shuffle
from card_functions import build_deck
from deck_functions import deal_hand
from deck_functions import shuffle_deck

deck = build_deck()
shuffle_deck(deck)
deal_hand(deck, 7)