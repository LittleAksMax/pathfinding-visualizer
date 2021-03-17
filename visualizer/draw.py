from .constants import BG_COLOR, GRID_BAR_COLOR, SCREEN_WIDTH, SCREEN_HEIGHT
from .spot_stat import SpotState
from .spot import Spot
import pygame


def clear_background(window):
    window.window.fill(BG_COLOR)


def draw_grid(window, grid_side):
    sqr_sz = SCREEN_WIDTH // grid_side  # should always be relative to width

    x = 0
    y = 0
    for i in range(grid_side):
        x += sqr_sz
        y += sqr_sz

        pygame.draw.line(window.window, GRID_BAR_COLOR, (x, 0), (x, SCREEN_HEIGHT))
        pygame.draw.line(window.window, GRID_BAR_COLOR, (0, y), (SCREEN_WIDTH, y))


def draw_spots(window, spot_grid, grid_side):
    sqr_sz = SCREEN_WIDTH // grid_side
    for row in spot_grid:
        for spot in row:
            if spot.state == SpotState.Unvisited:
                continue  # no need to change color, as unvisited color is background color
            pygame.draw.rect(window.window, Spot.get_rgb_from_state(spot.state), (sqr_sz * spot.x, sqr_sz * spot.y,
                                                                                  sqr_sz, sqr_sz))
