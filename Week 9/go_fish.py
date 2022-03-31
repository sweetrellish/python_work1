import random
import deck_functions
import card_functions

deck = deck_functions.build_deck()
deck_functions.shuffle_deck(deck)
uwin = 0
cwin = 0

print("\tWelcome to Go-Fish!\n-----Here is your starting hand-----")
user = deck_functions.deal_hand(deck, 7)
#print(user)
print("\n-----Here is the Computer's hand-----")
comp = deck_functions.deal_hand(deck, 7)
#print(comp)

print("\nSearching for pairs now...")
clone = user.copy()
user.sort()

pair = []

for num in range(7):
    if card_functions.get_Value(user[num]) in clone[num]:
        pair.append(user[num])

if pair:
    print(f'You have a pair of {pair}')
else:
    print('You have no pairs.')

while uwin == 0 or cwin == 0:
    menu = "-----Action Menu-----\n1)\tDraw a card \n2)\tPlay a pair\n3)\tAsk for a card\n4)\tGo-Fish!"
    prompt = input(f'{menu}\nEnter your selection: ')
    prompt = int(prompt)
    if prompt == 1:
        new_card = deck_functions.deal_top_card(deck)
        user.append(new_card)
    elif prompt == 2:
        for card in pair:
            table = pair.pop(card)
            user.pop(card)
            print(f'You have played {table[card]}')
    elif prompt == 3:
        query = input("What card do you want to ask for?\nEnter the exact card:")
        print(f'Do you have a {query}?')
        for card in comp:
            if query in card:
                ccard = comp.pop(f'{card}')
                user.append(ccard)
    elif prompt == 4:
        print('Go-Fish!')
        
    if user == None:
        uwin += 1
    elif comp == None:
        cwin += 1

        

