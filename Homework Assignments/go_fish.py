import random
import deck_functions
import card_functions

deck = card_functions.build_deck()
deck_functions.shuffle_deck(deck)
#create deck and shuffle

print("\t~Welcome to Go-Fish!~\n-----Here is your starting hand-----")
user = deck_functions.deal_hand(deck, 7)
print(user)
#start screen and starting hand

comp = deck_functions.deal_hand(deck, 7)
print(f'Computer:{comp}')
#init computer hand

count = 1               #dictionary table counter
while True:             #game loop
    pair =[]                        #pair list
    clones = user.copy()            #clone hand to check pairs

    table = {}                      #table dictionary to store played pairs

    menu = "-----Action Menu-----\n1)\tDraw a card \n2)\tPlay a pair\n3)\tAsk for a card\n4)\tQuit"     #action menu interface
    prompt = input(f'{menu}\nEnter your selection: ')                                                   #prompt for player
    prompt = int(prompt)
    if prompt == 1:
        user.append(deck_functions.deal_top_card(deck))                                                 #draws the top card into the hand
        print(f'\tHAND\n{user}')
        print(f'\tCOMPUTER HAND\n{comp}')
    if prompt == 2:
        pair = deck_functions.hand_pairs(user, clones)                                                  #checks for pairs
        if pair:
            for pairs in pair:
                table[f'Pair {count}'] = pairs                                                          #if pair exists, loop through to add each pair to table
            pair.remove(pairs)                                                                          #remove pair list
            table_image = f'\tTABLE\n-------------------------\n|{table}\t\t\n-------------------------\n'
            count += 1
            print(table_image)
            print(f'\tHAND\n{user}')
            print(f'\tCOMPUTER HAND\n{comp}')
            continue
    if prompt == 3:
       fish = input('What card would you like?\n')
       flag = 0
       #f'{fish}' in comp:
       try:
            for chand in comp:
                    if card_functions.same_Value(fish, chand):                            #fish for cards in computers hand
                        user.append(chand)                                                #if card is in computers hand (has same value), adds card to hand
                        clones.append(chand)
                        table[f'Pair {count}'] = chand                                    #takes card from computers hand, could be made to method()
                        comp.remove(chand)                                                #adds to user hand and clone, adds pair to table, removes from computer hand
                        deck_functions.hand_pairs(user, clones)                           #checks for pairs and prints hands
                        print(table_image)
                        print(f'\tHAND\n{user}')
                        print(f'\tCOMPUTER HAND\n{comp}')
                        flag += 1
                        count += 1
            if flag == 0:                                                                 #if no pairs found, print go-fish
                    print('Go-Fish!')
                    print(f'\tHAND\n{user}')
                    print(f'\tCOMPUTER HAND\n{comp}')
       except ValueError:
            print('Card not in hand...')                                                  #exception block for error message

    if prompt == 4 or user == '' or deck == '' or comp == '':                             #loop exit conditions
        break
    


#OLD CODE 4/13/2022

# for cards in user:                      #nested for loop to check value and ensure true pair, could act as method for handPairs(), adds to pair list and removes from hand
#     for clone in clones:                
#         if card_functions.get_Value(cards) == card_functions.get_Value(clone) and card_functions.get_suit(cards) != card_functions.get_suit(clone):
#             pair.append(cards)
#             pair.append(clone)
#             user.remove(cards)
#             user.remove(clone)
#             print(f"Storing {cards, clone} into pairs...")

# if pair:
#     print(f'Pairs: {pair}\n')
# else:
#     print('You have no pairs.\n')


# print("\n-----Here is the Computer's hand-----")
# comp = deck_functions.deal_hand(deck, 7)
# print(comp)

# print("\nSearching for pairs now...")
# clone = user.copy()
# user.sort()

# pair = []

# for num in range(7):
#     if card_functions.get_Value(user[num]) in clone[num]:
#         pair.append(user[num])

# if pair:
#     print(f'You have a pair of {pair}')
# else:
#     print('You have no pairs.')

# while uwin == 0 or cwin == 0:
#     menu = "-----Action Menu-----\n1)\tDraw a card \n2)\tPlay a pair\n3)\tAsk for a card\n4)\tGo-Fish!"
#     prompt = input(f'{menu}\nEnter your selection: ')
#     prompt = int(prompt)
#     if prompt == 1:
#         new_card = deck_functions.deal_top_card(deck)
#         user.append(new_card)
#     elif prompt == 2:
#         for card in pair:
#             table = pair.pop(card)
#             user.pop(card)
#             print(f'You have played {table[card]}')
#     elif prompt == 3:
#         query = input("What card do you want to ask for?\nEnter the exact card:")
#         print(f'Do you have a {query}?')
#         for card in comp:
#             if query in card:
#                 ccard = comp.pop(f'{card}')
#                 user.append(ccard)
#     elif prompt == 4:
#         print('Go-Fish!')
        
#     if user == None:
#         uwin += 1
#     elif comp == None:
#         cwin += 1

        

