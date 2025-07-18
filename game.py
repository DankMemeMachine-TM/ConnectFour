'''
 game.py
    The program's entry point, this starts up the game.
'''
from include import glob as g
from include import session as s
from include import round as r

# Initialized when the game is booted up, this doesn't do much right now, but I may add some more initialization features.
class Game:
    def __init__(self):
        self.startup();
    
    def startup(self):
        pass;

# MAIN LOOP #
game = Game();
session = s.Session();
session.start_new_round();