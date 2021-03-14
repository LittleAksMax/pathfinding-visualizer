import pygame
from .window import Window
from .constants import WIDTH, HEIGHT
from .draw import *


class App(object):
    def __init__(self, grid_width, grid_height, run_flags):
        pygame.init()
        self.window = Window(WIDTH, HEIGHT, "Pathfinding Visualizer created by @LittleAksMax")
        self.grid_width = grid_width
        self.grid_height = grid_height
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
            draw_grid(self.window, self.grid_width, self.grid_height)

            self.window.display.flip()  # update changes
