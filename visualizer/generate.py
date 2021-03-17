from .spot_stat import SpotState
from random import randint  # for random_start_end


def create_border(spot_grid, grid_side):
    # top and bottom #
    for x in range(grid_side):
        spot_grid[0][x].set_state(SpotState.Obstacle)
        spot_grid[grid_side - 1][x].set_state(SpotState.Obstacle)

    # left and right #
    for y in range(grid_side):
        spot_grid[y][0].set_state(SpotState.Obstacle)
        spot_grid[y][grid_side - 1].set_state(SpotState.Obstacle)
    

def random_maze(spot_grid, grid_side):
    create_border(spot_grid, grid_side)


def random_start_end(spot_grid, grid_side, maze_created):
    if maze_created:  # generate on borders, else anywhere

        y1 = 0  # to make y1 and y2 in scope
        y2 = 0

        invalid = True  # invalid until block on right is unvisited
        while invalid:
            y1 = randint(1, grid_side - 2)
            if spot_grid[y1][1].state == SpotState.Unvisited:
                invalid = False

        invalid = True  # invalid until block on left is unvisited
        while invalid:
            y2 = randint(1, grid_side - 2)
            if spot_grid[y2][grid_side - 2].state == SpotState.Unvisited:
                invalid = False

        spot_grid[y1][0].set_state(SpotState.Start)
        spot_grid[y2][grid_side - 1].set_state(SpotState.End)
    else:
        x1 = randint(0, grid_side - 1)
        y1 = randint(0, grid_side - 1)

        x2 = randint(0, grid_side - 1)
        y2 = randint(0, grid_side - 1)

        spot_grid[y1][x1].set_state(SpotState.Start)
        spot_grid[y2][x2].set_state(SpotState.End)
