if '__main__' == __name__:
    club_deck = [] #total card number list
    count = 0 
    card = 2
    #initialize all variables

    while count < 9:
        nameCard = f"{card} of Clubs"
        club_deck.append(nameCard)
        card += 1
        count += 1
    #while loop that adds card values to string list heart_deck

    faceCards = ['Ace of Clubs', 'Jack of Clubs', 'Queen of Clubs', 'King of Clubs']
    club_deck.insert(0, faceCards[0])
    club_deck.insert(count+1, faceCards[1])
    club_deck.insert(count+2, faceCards[2])
    club_deck.insert(count+3, faceCards[3])

    #print(heart_deck)

    print("Here's a list of all the Club cards:")
    print_count = 0
    while print_count < 13:
        print(club_deck[print_count])
        print_count += 1
    #use while loop to print all elements of heart deck

    #UNUSED CODE FROM HEARTS.PY
    # print("\nHere's a list of number cards:")
    # print2_count = 1
    # while print2_count < 10:
    #     print(club_deck[print2_count])
    #     print2_count += 1
    # # while loop printing only number cards

    # print("\nHere's all the face cards:")
    # print3_count = 1
    # while print3_count < 4:
    #     print(faceCards[print3_count])
    #     print3_count += 1
    # # while loop printing only face cards
    