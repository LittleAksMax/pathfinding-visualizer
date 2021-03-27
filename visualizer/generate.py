from .spot_stat import SpotState
from random import randint, shuffle


def create_maze(spot, spot_grid, grid_side):
    neighbors = []

    # left
    if spot.x > 0:
        if spot_grid[spot.y][spot.x - 1].state == SpotState.Obstacle:
            neighbors.append(spot_grid[spot.y][spot.x - 1])
    # right
    if spot.x < grid_side - 1:
        if spot_grid[spot.y][spot.x + 1].state == SpotState.Obstacle:
            neighbors.append(spot_grid[spot.y][spot.x + 1])

    # up
    if spot.y > 0:
        if spot_grid[spot.y - 1][spot.x].state == SpotState.Obstacle:
            neighbors.append(spot_grid[spot.y - 1][spot.x])

    # down
    if spot.y < grid_side - 1:
        if spot_grid[spot.y + 1][spot.x].state == SpotState.Obstacle:
            neighbors.append(spot_grid[spot.y + 1][spot.x])

    # return if more than two blanks around you, to make sure some obstacles remain
    # easily checked by simply checking length of neighbors, as only obstacles were added
    if not len(neighbors) > 2:
        return

    spot.set_state(SpotState.Unvisited)  # change state so it isn't visited again

    for i in range(4):  # it doesn't matter if less, as it will just continue if neighbors is empty
        if len(neighbors) == 0:
            break

        neighbor = neighbors[randint(0, len(neighbors) - 1)]  # get random neighbor to continue from
        neighbors.remove(neighbor)  # remove so it doesn't show up again
        if neighbor.state == SpotState.Unvisited:  # skip if not a wall (as we fill the entire grid with walls)
            continue

        create_maze(neighbor, spot_grid, grid_side)


def create_maze2(spot, spot_grid, grid_side):
    directions = ["N", "E", "S", "W"]

    shuffle(directions)  # get random order

    for direction in directions:
        if direction == "N":
            if spot.y > 1:  # check if exists
                if spot_grid[spot.y - 2][spot.x].state == SpotState.Obstacle:  # check if already visited
                    for i in range(2):  # make each obstacle a path
                        spot_grid[spot.y - 2 + i][spot.x].set_state(SpotState.Unvisited)
                    create_maze2(spot_grid[spot.y - 2][spot.x], spot_grid, grid_side)

        elif direction == "E":
            if spot.x > 1:
                if spot_grid[spot.y][spot.x - 2].state == SpotState.Obstacle:
                    for i in range(2):
                        spot_grid[spot.y][spot.x - 2 + i].set_state(SpotState.Unvisited)
                    create_maze2(spot_grid[spot.y][spot.x - 2], spot_grid, grid_side)

        elif direction == "S":
            if spot.y < grid_side - 2:
                if spot_grid[spot.y + 2][spot.x].state == SpotState.Obstacle:
                    for i in range(2):
                        spot_grid[spot.y + 2 - i][spot.x].set_state(SpotState.Unvisited)
                    create_maze2(spot_grid[spot.y + 2][spot.x], spot_grid, grid_side)

        else:
            if spot.x < grid_side - 2:
                if spot_grid[spot.y][spot.x + 2].state == SpotState.Obstacle:
                    for i in range(2):
                        spot_grid[spot.y][spot.x + 2 - i].set_state(SpotState.Unvisited)
                    create_maze2(spot_grid[spot.y][spot.x + 2], spot_grid, grid_side)


def fill_maze(spot_grid, grid_side):
    for spot_row in spot_grid:
        for spot in spot_row:
            spot.set_state(SpotState.Obstacle)


# completely fill maze with obstacles
# traverse from random position on left border DFS
# keep going recursively until no more moves left
def random_maze(spot_grid, grid_side):
    fill_maze(spot_grid, grid_side)
    random_start = randint(0, grid_side - 2)
    create_maze2(spot_grid[random_start][0], spot_grid, grid_side)  # start at random spot on left edge

    spot_grid[random_start][0].set_state(SpotState.Start)  # create start point at random location

    # at this start_point, the entire right border/side is accessible, therefore I can just randomly pick one
    invalid = True
    while invalid:
        random_end = randint(1, grid_side - 2)
        if spot_grid[random_end][grid_side - 2].state == SpotState.Unvisited:  # check if node to left is not wall
            spot_grid[random_end][grid_side - 1].set_state(SpotState.End)  # if not, valid end point
            invalid = False
