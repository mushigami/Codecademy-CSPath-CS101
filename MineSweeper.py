"""
A terminal Minesweeper clone game using Python 3.10

First a welcome screen with a prompt to input the grid size and amount of mines
A 2D integer list to store the grid
A 2D boolean list to store the cells if there is a bomb

"""


class Game:
    def __init__(self, game_screen=None, mines=0):
        self.game_screen = game_screen
        self.mines = mines

    def play_game(self):
        self.reset_game()
        self.game_screen = Screen()
        self.game_screen.get_user_input()

    def reset_game(self):
        self.game_screen = None


class Screen:

    def __init__(self, num_row=0, num_col=0, num_mines=0):
        self.num_row = num_row
        self.num_col = num_col
        self.num_mines = num_mines

    def get_user_input(self):
        self.num_row, self.num_col, self.num_mines = input(
            "Enter grid size as 'row' 'col' and the number of mines with spaces in "
            "between [ex: 4 6 7]: ").split()
        print("Grid: " + str(self.num_row) + "x" + str(self.num_col) + " mines: " + str(self.num_mines))

    def place_mines(self):
        pass


new_game = Game()
new_game.play_game()
