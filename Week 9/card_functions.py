#Some commented code is still in drafting and is used for experiment
def build_deck():
    """Builds a deck with for loops and lists,
       And returns list of cards in order"""
    deck = []
    hearts =[]
    spades =[]
    diamonds =[]
    clubs = []
    face = ['Jack', 'Queen', 'King', 'Ace']
    count = 0
    count1 = 0
    count2 = 0
    count3 = 0

    for num in range(2,15):
        hearts = f'{num} of Hearts'
        if num >= 11:
            hearts = f'{face[count]} of Hearts'
            count += 1
        deck.append(hearts[:])

    for card in range(2,15):
        spades = f'{card} of Spades'
        if card >= 11:
            spades = f'{face[count1]} of Spades'
            if face[count1] == 'Ace':
                spades = f'{face[count1]} of Spades'
            count1 += 1
        deck.append(spades[:])

    for card in range(2,15):
        diamonds = f'{card} of Diamonds'
        if card >= 11:
            diamonds = f'{face[count2]} of Diamonds'
            count2 += 1 
        deck.append(diamonds[:])  

    for card in range(2,15):
        clubs = f'{card} of Clubs'
        if card >= 11:
            clubs = f'{face[count3]} of Clubs'
            count3 += 1
        deck.append(clubs[:])
#for loops defining each card and suit
#      
    # for card in deck:   
    #     print(card)
    return deck    

def get_suit(card):
    """Takes in card argument and returns suit of that card."""
    if 'Hearts' in card:
        print('Hearts')
    if 'Spades' in card:
        print('Spades')
    if 'Clubs' in card:
        print('Clubs')
    if 'Diamonds' in  card:
        print('Diamonds')
#returns suit of card

def same_Value(card1, card2, *card3):
    """Takes number of cards and tests value equivalency of each card."""
    def get_Value(card):
        """Takes in card argument and returns number value of that card."""
        face = ['Ace', 'Jack', 'Queen', 'King']
        for num in range(2,11):
            num = f'{num}'
            if num in card:
                #print(num)
                return num
                
        for value in face:
            if value in card:
                #print(value)
                return value
    #returns value of card number

    num1 = get_Value(card1)
    num2 = get_Value(card2)
    num3 = get_Value(card3)
    if num1 == num2 and num2 == num3:
        print(f'{num1} and {num2} are pairs.')
        return True
    else :
        print('False')
        return False
    #checks if card number values are equivalent
    #Functions are nested so that get_Value can be called within the function to determine equivalency

def same_Suit(card1, card2, card3):
    """Takes suit of cards and tests equivalency of each card."""
    suit = ['Hearts', 'Spades', 'Clubs', 'Diamonds']
    for card in suit:
        if card in card1 and card in card2 and card in card3:
            print(card)
        # if card in card3:
        #     print(card)
#checks if card suit values are equivalent

def get_Value(card):
        """Takes in card argument and returns number value of that card."""
        face = ['Ace', 'Jack', 'Queen', 'King']
        for num in range(2,11):
            num = f'{num}'
            if num in card:
                #print(num)
                return num
                
        for value in face:
            if value in card:
               # print(value)
                return value
    #returns value of card number


# build_deck()
# get_suit('2 of Hearts')
# get_Value('Jack of Hearts')
# same_Value('2 of Spaces', '2 of Hearts', '2 of Hearts')
# same_Suit('2 of Hearts', '2 of Hearts', '2 of Hearts')

#All functions are working as needed 3/24/2022