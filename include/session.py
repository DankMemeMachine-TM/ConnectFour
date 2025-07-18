'''
 session.py
    This controls the player names (may be taken out and put into player.py in a future revision), and keeps track of each player's win ratio and how
    many rounds have been played since the program was turned on.
'''
player_names = ["Player One", "Player Two"];
win_ratio = [0, 0];
rounds = 0;

def increase_wins(player):
    win_ratio[player - 1] += 1;

def print_wins():
    print("SCORE:");
    for n in range(2):
        print("\tPLAYER ", n + 1, " (", player_names[n], "): ", win_ratio[n]);

def start_new_round():
    print("TOdo");