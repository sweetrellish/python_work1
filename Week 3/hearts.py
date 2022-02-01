heart_deck = [] #card number list
total_heart = [] #total face and number cards
count = 0 
card = 2
#initialize all variables

while count < 9:
    nameCard = f"{card} of Hearts"
    heart_deck.append(nameCard)
    card += 1
    count += 1
#while loop that adds card values to string list heart_deck

faceCards = ['Ace of Hearts', 'Jack of Hearts', 'Queen of Hearts', 'King of Hearts']
heart_deck.insert(0, faceCards[0])
heart_deck.insert(count+1, faceCards[1])
heart_deck.insert(count+2, faceCards[2])
heart_deck.insert(count+3, faceCards[3])

#print(heart_deck)

print("Here's a list of all the Heart cards:")
print_count = 0
while print_count < 13:
    print(heart_deck[print_count])
    print_count += 1
#use while loop to print all elements of heart deck
 
