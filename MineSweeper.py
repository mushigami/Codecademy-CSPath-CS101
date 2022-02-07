"""
A terminal Minesweeper clone game using Python 3.10

First a welcome screen with a prompt to input the grid size and amount of mines
A 2D integer list to store the grid
A 2D boolean list to store the cells if there is a bomb

play_game:
    start_game:
        get_grid_input
    update_game:
        get_user_input
        check if already selected
        check if there is a mine
            if there is a mine:
                update_grid
                show_grid
                show_game_over
                ask_to_play_again:
                    yes:
                        start_game:
                    no:
                        end_game
            else:
                update_grid
                show_grid

"""
import random

n = 8
grid = [[' ' for y in range(n)] for x in range(n)]


def draw_grid(grid_2d):
    n: int = len(grid_2d[0])

    print()
    print("\t\t\t\tMINESWEEPER\n")

    st = "   "
    for i in range(n):
        st = st + "     " + str(i + 1)
    print(st)

    for r in range(n):
        st = "     "
        if r == 0:
            for col in range(n):
                st = st + "______"
            print(st)

        st = "     "
        for col in range(n):
            st = st + "|     "
        print(st + "|")

        st = "  " + str(r + 1) + "  "
        for col in range(n):
            st = st + "|  " + str(grid_2d[r][col]) + "  "
        print(st + "|")

        st = "     "
        for col in range(n):
            st = st + "|_____"
        print(st + '|')

    print()

draw_grid(grid)