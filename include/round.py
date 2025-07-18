'''
 round.py
    The largest file for the game, this controls all of the main game logic.
'''
from include import glob as g
from include import session as s
from include import player as p

SUCCESS = 0;
FAILURE = 1;

class Round:
    ############################
    # INITIALIZATION FUNCTIONS #
    ############################
    def __init__(self, names = ["", ""], initial = g.PLAYER_ONE):
        self.board = [
            ['-', '-', '-', '-', '-', '-', '-'],
            ['-', '-', '-', '-', '-', '-', '-'],
            ['-', '-', '-', '-', '-', '-', '-'],
            ['-', '-', '-', '-', '-', '-', '-'],
            ['-', '-', '-', '-', '-', '-', '-'],
            ['-', '-', '-', '-', '-', '-', '-'],
        ];
        self.player_names = {
            g.PLAYER_ONE: names[0], 
            g.PLAYER_TWO: names[1]
        };
        self.initial_player = initial;
        self.current_player = self.initial_player;
        self.total_turns = 0;
        self.print_round();
        self.input_handling();
    
    ###################
    # INPUT FUNCTIONS #
    ###################
    def input_handling(self):
        val = input("Please enter a column number between 1 and 7: ");
        try:
            val = int(val);
            self.take_action(self.current_player, val);
        except:
            print("Looks like that input is invalid; please try entering a valid input.");
            self.input_handling();
    
    # Currently, this doesn't give you a unique error message if a row/column is full.
    def take_action(self, player, column):
        if(column > 7 or column < 1):
            print("Position" , column, " is not a valid column. Please only enter a value from 1 to 7.");
            self.input_handling();
        elif (self.insert_marker(player, column - 1) == 0):
            if (self.check_if_win(player) == True):
                self.win_game(player);
            else:
                if (self.check_if_board_full() == True):
                    self.draw_game();
                else:
                    self.change_current_player();
                    self.print_round();
                    self.input_handling();
        else:
            print("Position ", column, " is invalid. Please try a different position.");
            self.input_handling();
    
    ######################
    # GAMEPLAY FUNCTIONS #
    ######################
    def change_current_player(self):
        match self.current_player:
            case g.PLAYER_TWO:
                self.current_player = g.PLAYER_ONE;
            case _:
                self.current_player = g.PLAYER_TWO;
        self.print_current_turn(self.current_player);
        if(self.current_player == self.initial_player):
            self.total_turns += 1;
    
    def insert_marker(self, player, column):
        insertion = any;
        self.board.reverse();
        for row in range(6):
            if(self.board[row][column]) == '-':
                insertion = row;
                break;
        if(type(insertion) != int):
            self.board.reverse();
            return FAILURE;
        self.board[insertion][column] = g.PLAYER_ICON_MAP[player];
        self.board.reverse();
        print("\nPlaced marker into row ", (6 - insertion), ", column", column + 1, ".");
        return SUCCESS;

    def check_if_board_full(self) -> bool:
        for n in range(6):
            if('-' in self.board[n]): # An occupied element exists, so board is not full
                return False;
        return True;
    
    def check_if_win(self, player) -> bool:
        marker = g.PLAYER_ICON_MAP[player];
        game_won = False;
        # WIN CONDITION CHECK
        game_won = self.win_check_vertical(marker);
        game_won = self.win_check_horizontal(marker) if game_won == False else game_won == True;
        game_won = self.win_check_diagonal(marker) if game_won == False else game_won == True;
        return game_won;
    
    def win_check_vertical(self, marker) -> bool:
        if(g.DEBUG_MODE):
            print("vertical");
        temp = 0;
        for column in range(7):
            for row in range(6):
                if(self.board[row][column] == marker):
                    temp += 1;
                    if (self.win_counter_check(temp)):
                        return True;
                else:
                    temp = 0;
                    continue;
            temp = 0;
        return False;

    def win_check_horizontal(self, marker) -> bool:
        if(g.DEBUG_MODE):
            print("horizontal");
        temp = 0;
        for row in range(6):
            for column in range(7):
                if(self.board[row][column] == marker):
                    temp += 1;
                    if (self.win_counter_check(temp)):
                        return True;
                else:
                    temp = 0;
                    continue;
            temp = 0;
        return False;

    # This function is kind of messy; I may try to see if I can refactor it to be a bit cleaner
    def win_check_diagonal(self, marker) -> bool:
        if(g.DEBUG_MODE):
            print("diagonal");
        temp: int = 0;
        for column in range(7):
            for row in range(6):
                if(self.board[row][column] == marker):
                    temp += 1; # Mark current
                    temp += self.diagonal_loop(marker, 1, 1, row, column);
                    if (self.win_counter_check(temp)):
                        return True;
                    temp = 1; # Keep the initial one marked while we go the other way
                    temp += self.diagonal_loop(marker, -1, 1, row, column);
                    if (self.win_counter_check(temp)):
                        return True;
                    temp = 0;
            temp = 0;
        return False;

    def diagonal_loop(self, marker, row_dir, column_dir, start_row, start_column):
        temp = 0;
        diagonal_row = start_row + row_dir;
        diagonal_column = start_column + column_dir;
        while(diagonal_row < 6 and diagonal_row >= 0 and  diagonal_column < 7 and diagonal_column >= 0):
            if(self.board[diagonal_row][diagonal_column] == marker):
                temp += 1;
            diagonal_row += row_dir;
            diagonal_column += column_dir;
        return temp;

    def win_counter_check(self, input) -> bool:
        if(input >= 4):
            return True;
        return False;

    ######################
    # POSTGAME FUNCTIONS #
    ######################
    def win_game(self, player):
        print("\nPlayer ", player, " (", self.player_names[player], ")  wins!!");
        self.print_board();
        return;

    def draw_game(self):
        print("DRAW GAME!!");
        self.print_board();
        self.current_player = g.DRAW_GAME;
        return;

    ###################
    # PRINT FUNCTIONS #
    ###################
    def print_round(self) -> any:
        self.print_names();
        self.print_current_turn(self.current_player);
        self.print_board();

    def print_names(self):
        for n in self.player_names:
            print("PLAYER", n, ":", self.player_names[n], end="\t");
        print("\n");
    
    def print_current_turn(self, player):
        print("\nIt is ", self.player_names[player], " (", g.PLAYER_ICON_MAP[player], ")'s turn.\n");

    # Prints the board... were you expecting something else?
    def print_board(self):
        print("\n",end="      ");
        for n in range(7):
            print(n + 1,end="    ");
        print(end="\n");
        for n in range(6):
            print(n + 1, " ", self.board[n]);
        print("\n");