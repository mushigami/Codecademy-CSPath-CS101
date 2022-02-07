"""
A terminal Minesweeper clone game using Python 3.10

First a welcome screen with a prompt to input the grid size and amount of mines
A 2D integer list to store the grid
A 2D boolean list to store the cells if there is a bomb

start_game:
    get_grid_input
play_game:
    get_user_input
    check if already selected
    check if there is a mine
        if there is a mine:
            update_grid
            show_grid
            show_game_over
            ask_to_play_again
        else:
            update_grid
            show_grid

"""
import random


def draw_grid(grid_size):
    pass
