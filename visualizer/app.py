import pygame
from .window import Window
from .constants import SCREEN_WIDTH, SCREEN_HEIGHT
from .draw import *
from .generate import random_maze, random_start_end


class App(object):
    def __init__(self, grid_side, run_flags, algorthm):
        pygame.init()
        self.window = Window(SCREEN_WIDTH, SCREEN_HEIGHT, "Pathfinding Visualizer created by @LittleAksMax")
        self.grid_side = grid_side

        # set flags #
        self.quick_solve = run_flags & 1
        self.random_maze = (run_flags >> 1) & 1
        self.random_start_end = (run_flags >> 2) & 1

        self.spot_grid = []
        self.fill_grid()  # fill the grid with default spots

        # perform according flag functions #
        if self.random_maze:
            random_maze(self.spot_grid, self.grid_side)
        if self.random_start_end:
            random_start_end(self.spot_grid, self.grid_side, self.random_maze)

    def fill_grid(self):
        self.spot_grid = [[Spot(i, j) for j in range(self.grid_side)] for i in range(self.grid_side)]

    def start(self):
        self.mainloop()
        pygame.quit()

    def mainloop(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # draw #
            clear_background(self.window)
            draw_grid(self.window, self.grid_side)
            draw_spots(self.window, self.spot_grid, self.grid_side)

            self.window.display.flip()  # update changes
