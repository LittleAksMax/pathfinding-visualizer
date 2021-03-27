from .spot_stat import SpotState
from random import randint, shuffle


def create_maze(spot, spot_grid, grid_side):
    directions = ["N", "E", "S", "W"]

    shuffle(directions)  # get random order

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
    random_start = randint(1, grid_side - 2)
    random_start = 15
    create_maze(spot_grid[random_start][0], spot_grid, grid_side)  # start at random spot on left edge

    spot_grid[random_start][0].set_state(SpotState.Start)  # create start point at random location

    # at this start_point, the entire right border/side is accessible, therefore I can just randomly pick one
    invalid = True
    random_end = -1  # to declare
    while invalid:
        random_end = randint(1, grid_side - 2)
        if spot_grid[random_end][grid_side - 2].state == SpotState.Unvisited:  # check if node to left is not wall
            spot_grid[random_end][grid_side - 1].set_state(SpotState.End)  # if not, valid end point
            invalid = False

    return spot_grid[random_start][0], spot_grid[random_end][grid_side - 1]  # start and end nodes
