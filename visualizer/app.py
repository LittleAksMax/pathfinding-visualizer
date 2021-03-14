import pygame
from .window import Window
from .constants import SCREEN_WIDTH, SCREEN_HEIGHT
from .draw import *


class App(object):
    def __init__(self, grid_side, run_flags, algorthm):
        pygame.init()
        self.window = Window(SCREEN_WIDTH, SCREEN_HEIGHT, "Pathfinding Visualizer created by @LittleAksMax")
        self.grid_side = grid_side
        self.flags = run_flags

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

            self.window.display.flip()  # update changes
