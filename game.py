'''
 game.py
    The program's entry point, this starts up the game.
'''
from include import glob as g
from include import session as s
from include import round as r

# Initialized when the game is booted up, this handles the overall game state.
class Game:
    def __init__(self):
        self.round = any; # This starts out null, but will be turned into an actual Round object when the game starts.
        self.startup();
    
    def startup(self):
        print("TODO: Add code to actually set the game up manually...");

    def start_new_round(self):
        self.round = r.Round(s.player_names, g.PLAYER_ONE);
        s.rounds += 1;

# MAIN LOOP #
game = Game();
game.start_new_round();