from .spot_stat import SpotState


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
        pass
    else:
        pass
