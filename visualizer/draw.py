from .constants import BG_COLOR, GRID_BAR_COLOR, SCREEN_WIDTH, SCREEN_HEIGHT
import pygame


def clear_background(window):
    window.window.fill(BG_COLOR)


def draw_grid(window, grid_side):
    sqr_sz = SCREEN_WIDTH // grid_side  # should always be relative to width

    x = 0
    y = 0
    for i in range(grid_side + 1):  # + 1 is just in case it is not long enough
        x += sqr_sz
        y += sqr_sz

        pygame.draw.line(window.window, GRID_BAR_COLOR, (x, 0), (x, SCREEN_HEIGHT))
        pygame.draw.line(window.window, GRID_BAR_COLOR, (0, y), (SCREEN_WIDTH, y))

    x = 0
    y = 0
    for i in range(grid_side):
        pass
