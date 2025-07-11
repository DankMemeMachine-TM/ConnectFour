# Initialized when a new round is started, this contains the turn number and the current board state.
# "names" is an argument in case the name is changed in the Session object.
from include import glob as g
from include import session as s

class Round:
    def __init__(self, names = ["", ""], initial = g.PLAYER_ONE):
        self.board = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
        ];
        self.player_names = [names[0], names[1]];
        self.initial_player = initial;
        self.current_player = self.initial_player;
        self.total_turns = 0;
        self.print_round();
    
    def change_current_player(self):
        match self.current_player:
            case 2:
                self.current_player = g.PLAYER_ONE;
            case _:
                self.current_player = g.PLAYER_TWO;
        self.print_current_turn(self.current_player);
        if(self.current_player == self.initial_player):
            self.total_turns += 1;
    
    def insert_circle(player):
        pass; #TODO

    ###################
    # PRINT FUNCTIONS #
    ###################
    def print_round(self):
        self.print_names();
        self.print_current_turn(self.current_player);
        self.print_board();

    def print_names(self):
        for n in range(2):
            print("PLAYER", n + 1, ":", self.player_names[n], end="\t");
        print("\n");
    
    def print_current_turn(self, input):
        print("It is ", self.player_names[input], "'s turn.");

    # Prints the board... were you expecting something else?
    def print_board(self):
        for n in range(4):
            print(self.board[n]);