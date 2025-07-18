'''
 session.py
    This controls the player names (may be taken out and put into player.py in a future revision), and keeps track of each player's win ratio and how
    many rounds have been played since the program was turned on.
'''
from include import round as r
from include import glob as g

class Session:
    def __init__(self):
        self.player_names = ["Player One", "Player Two"];
        self.win_ratio = [0, 0];
        self.rounds: int = 0;

    def increase_wins(self, player):
        self.win_ratio[player - 1] += 1;

    def print_wins(self):
        print("SCORE:");
        for n in range(2):
            print("\tPLAYER ", n + 1, " (", self.player_names[n], "): ", self.win_ratio[n]);
    
    def game_won(self, winner):
        self.increase_wins(winner);

    def start_new_round(self):
        self.rounds += 1;
        print("\n-= ROUND", self.rounds, "=-\n");
        round = r.Round(self.player_names, g.PLAYER_ONE);
        winner: int = round.current_player; # As current player doesn't change once the game is won, the last current player was the winner
        if(winner > 0): # If winner == 0, game ended in a draw
            self.increase_wins(winner);
        self.print_wins();
        del round; # Make sure old object is deleted, just in case
        self.play_again_prompt();

    def play_again_prompt(self):
        val = input("\nPlay again? Y/n (not case-sensitive): ");
        try:
            val = str(val);
            if(val == "Y" or val == "y"):
                self.start_new_round();
            elif(val == "N" or val == "n"):
                return 0;
        except:
            print("That value is invalid. Please only enter Y or n (not case-sensitive): ");