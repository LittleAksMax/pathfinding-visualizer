from .spot_stat import SpotState
from random import randint, shuffle


def create_maze(spot, spot_grid, grid_side):
    directions = ["N", "E", "S", "W"]

    shuffle(directions)  # get random order

    # you check 2 spots in the same direction to make sure there are no cascading blocks, and only straight lines
    # so this is bad:
    #       []
    #    []
    # []
    # but this is good
    #       [] []
    #    [] []
    # [] []
    for direction in directions:
        if direction == "N":
            if spot.y - 2 > 0:  # check if exists
                if spot_grid[spot.y - 2][spot.x].state == SpotState.Obstacle:  # check if already visited
                    for i in range(3):  # make each obstacle in line a path
                        spot_grid[spot.y - 2 + i][spot.x].set_state(SpotState.Unvisited)
                    create_maze(spot_grid[spot.y - 2][spot.x], spot_grid, grid_side)

        elif direction == "W":
            if spot.x - 2 > 0:
                if spot_grid[spot.y][spot.x - 2].state == SpotState.Obstacle:
                    for i in range(3):
                        spot_grid[spot.y][spot.x - 2 + i].set_state(SpotState.Unvisited)
                    create_maze(spot_grid[spot.y][spot.x - 2], spot_grid, grid_side)

        elif direction == "S":
            if spot.y + 2 < grid_side - 1:
                if spot_grid[spot.y + 2][spot.x].state == SpotState.Obstacle:
                    for i in range(3):
                        spot_grid[spot.y + i][spot.x].set_state(SpotState.Unvisited)
                    create_maze(spot_grid[spot.y + 2][spot.x], spot_grid, grid_side)

        else:
            if spot.x + 2 < grid_side - 1:
                if spot_grid[spot.y][spot.x + 2].state == SpotState.Obstacle:
                    for i in range(3):
                        spot_grid[spot.y][spot.x + i].set_state(SpotState.Unvisited)
                    create_maze(spot_grid[spot.y][spot.x + 2], spot_grid, grid_side)


def fill_maze(spot_grid):
    for spot_row in spot_grid:
        for spot in spot_row:
            spot.set_state(SpotState.Obstacle)


# completely fill maze with obstacles
# traverse from random position on left border DFS
# keep going recursively until no more moves left
def random_maze(spot_grid, grid_side):
    fill_maze(spot_grid)

    random_y = randint(1, grid_side - 2) // 2 * 2 + 1
    random_x = randint(1, grid_side - 2) // 2 * 2 + 1  # make sure they are odd

    create_maze(spot_grid[random_y][random_x], spot_grid, grid_side)  # start at random spot on left edge

    random_start = 0
    random_end = 0  # declare

    invalid = True
    while invalid:
        random_start = randint(1, grid_side - 2)
        if spot_grid[random_start][1].state != SpotState.Unvisited:
            continue
        invalid = False

    invalid = True
    while invalid:
        random_end = randint(1, grid_side - 2)
        if spot_grid[random_end][grid_side - 2].state != SpotState.Unvisited:
            continue
        invalid = False

    spot_grid[random_start][0].set_state(SpotState.Start)  # create start point at random location
    spot_grid[random_end][grid_side - 1].set_state(SpotState.End)  # create end point at random location

    return spot_grid[random_start][0], spot_grid[random_end][grid_side - 1]  # start and end nodes
