current_ids = ['Ryan', 'Bridget', 'Sam', 'Justin', 'Alex']
new_ids = ['Ryan', 'ALEX', 'Richard', 'Anna', 'Connor']

for user in new_ids:
    if user not in current_ids and user == user.title():
        print(f"The username {user} is available.")
    # elif user in new_ids != current_ids:
    #     print(f"The username {user} is taken, \nplease select another username.")
        
for user in new_ids:
    for name in current_ids:
        if user.title() == name.title():
            user = user.title()
            print(f"The username {user} is taken, \nplease select another username.")
#nested for loop to check for capitilization