from .spot_stat import SpotState
from random import randint, shuffle
import pygame  # for player creation of maze
from .constants import SCREEN_WIDTH  # same as SCREEN_HEIGHT as display is square


# ------------------------------------ USER GENERATED ------------------------------------ #


def get_clicked_pos(pos, rows, width):
    gap = width // rows
    y, x = pos

    row = y // gap
    col = x // gap

    return col, row


def user_create_maze(draw, spot_grid, grid_side):
    start = None
    end = None

    run = True
    while run:
        # draw
        draw()

        # user input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # so it doesn't crash when pressed, but I don't want it to do anything
                pass

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if start is not None and end is not None:
                        run = False

            if pygame.mouse.get_pressed()[0]:  # LEFT
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, grid_side, SCREEN_WIDTH)
                spot = spot_grid[row][col]
                if not start and spot != end:
                    start = spot
                    start.set_state(SpotState.Start)

                elif not end and spot != start:
                    end = spot
                    end.set_state(SpotState.End)

                elif spot != end and spot != start:
                    spot.set_state(SpotState.Obstacle)

            elif pygame.mouse.get_pressed()[2]:  # RIGHT
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, grid_side, SCREEN_WIDTH)
                spot = spot_grid[row][col]
                spot.set_state(SpotState.Unvisited)
                if spot == start:
                    start = None
                elif spot == end:
                    end = None
    return start, end


# ---------------------------------- RANDOMLY GENERATED ---------------------------------- #


def create_maze(spot, spot_grid, grid_side, draw):  # draw will be None if user didn't want to show steps
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

                    # draw
                    if draw != None:
                        draw()

                    create_maze(spot_grid[spot.y - 2][spot.x], spot_grid, grid_side, draw)

        elif direction == "W":
            if spot.x - 2 > 0:
                if spot_grid[spot.y][spot.x - 2].state == SpotState.Obstacle:
                    for i in range(3):
                        spot_grid[spot.y][spot.x - 2 + i].set_state(SpotState.Unvisited)

                    # draw
                    if draw is not None:
                        draw()

                    create_maze(spot_grid[spot.y][spot.x - 2], spot_grid, grid_side, draw)

        elif direction == "S":
            if spot.y + 2 < grid_side - 1:
                if spot_grid[spot.y + 2][spot.x].state == SpotState.Obstacle:
                    for i in range(3):
                        spot_grid[spot.y + i][spot.x].set_state(SpotState.Unvisited)

                    # draw
                    if draw is not None:
                        draw()

                    create_maze(spot_grid[spot.y + 2][spot.x], spot_grid, grid_side, draw)

        else:
            if spot.x + 2 < grid_side - 1:
                if spot_grid[spot.y][spot.x + 2].state == SpotState.Obstacle:
                    for i in range(3):
                        spot_grid[spot.y][spot.x + i].set_state(SpotState.Unvisited)

                    # draw
                    if draw is not None:
                        draw()

                    create_maze(spot_grid[spot.y][spot.x + 2], spot_grid, grid_side, draw)


def fill_maze(spot_grid):
    for spot_row in spot_grid:
        for spot in spot_row:
            spot.set_state(SpotState.Obstacle)


# completely fill maze with obstacles
# traverse from random position on left border DFS
# keep going recursively until no more moves left
def random_maze(spot_grid, grid_side, draw):
    fill_maze(spot_grid)

    random_y = randint(1, grid_side - 2) // 2 * 2 + 1
    random_x = randint(1, grid_side - 2) // 2 * 2 + 1  # make sure they are odd

    create_maze(spot_grid[random_y][random_x], spot_grid, grid_side, draw)  # start at random spot on left edge

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
