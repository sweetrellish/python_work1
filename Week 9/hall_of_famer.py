def make_HOF(list, hof_list):
    """Adds Hall of Famer to each player in list"""
    for player in list:
        player = f'Hall of Famer {player}'
        hof_list.append(player)

def show_players(player_list):
    """Passes list to print players in list"""
    for player in player_list:
        print(player)
    
players = ['Kobe Bryant', 'Shaq', 'Michael Jordan']
hof_players = []
make_HOF(players, hof_players)
show_players(hof_players)