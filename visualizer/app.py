from pygame import init, quit
from .constants import SCREEN_WIDTH, SCREEN_HEIGHT
from .window import Window
from .draw import *
from .generate import random_maze, user_create_maze
from .algorithms import Algorithms, bfs, dfs, astar, dijkstra


class App(object):
    def __init__(self, grid_side, run_flags, algorithm):
        init()  # initialise pygame
        self.window = Window(SCREEN_WIDTH, SCREEN_HEIGHT, "Pathfinding Visualizer created by @LittleAksMax")
        self.grid_side = grid_side

        # set flags #
        self.quick_solve = run_flags & 1
        self.random_maze = (run_flags >> 1) & 1
        self.show_generation = (run_flags >> 2) & 1

        if algorithm == Algorithms.BFS:
            self.algorithm = bfs  # function
        elif algorithm == Algorithms.DFS:
            self.algorithm = dfs
        elif algorithm == Algorithms.AStar:
            self.algorithm = astar
        else:
            self.algorithm = dijkstra

        self.spot_grid = []
        self.fill_grid()  # fill the grid with default spots

        self.start_node = None  # to declare
        self.end_node = None

        # perform according flag functions #
        if self.random_maze:
            self.start_node, self.end_node = random_maze(self.spot_grid, self.grid_side, lambda: self.draw_everything() if self.show_generation else None)
        else:
            self.start_node, self.end_node = user_create_maze(lambda: self.draw_everything(), self.spot_grid, grid_side)

        self.update_spot_neighbors()

    def fill_grid(self):
        self.spot_grid = [[Spot(j, i) for j in range(self.grid_side)] for i in range(self.grid_side)]

    def update_spot_neighbors(self):
        for y in range(self.grid_side):
            for x in range(self.grid_side):
                current = self.spot_grid[y][x]

                # left
                if x > 0:
                    if self.spot_grid[y][x - 1].state != SpotState.Obstacle:
                        current.neighbors.append(self.spot_grid[y][x - 1])

                # right
                if x < self.grid_side - 1:
                    if self.spot_grid[y][x + 1].state != SpotState.Obstacle:
                        current.neighbors.append(self.spot_grid[y][x + 1])

                # up
                if y > 0:
                    if self.spot_grid[y - 1][x].state != SpotState.Obstacle:
                        current.neighbors.append(self.spot_grid[y - 1][x])

                # down
                if y < self.grid_side - 1:
                    if self.spot_grid[y + 1][x].state != SpotState.Obstacle:
                        current.neighbors.append(self.spot_grid[y + 1][x])

    def start(self):
        self.mainloop()
        quit()  # quit pygame

    def draw_everything(self):
        clear_background(self.window)
        draw_spots(self.window, self.spot_grid, self.grid_side)
        draw_grid(self.window, self.grid_side)
        self.window.display.update()  # update changes

    def mainloop(self):
        solved = False
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        if not solved:
                            distance = self.algorithm(self.start_node, self.end_node, self.spot_grid, lambda: self.draw_everything(), self.quick_solve)

                            print(f"Distance: {distance}")

                            # recolor start and end node to make them distinct from the rest of the path, and so they are not masked
                            self.start_node.set_state(SpotState.Start)
                            self.end_node.set_state(SpotState.End)

                            solved = True  # so it doesn't solve again
                        else:
                            running = False

            # draw
            self.draw_everything()

            # TODO: assign a button to clear the screen, popup with flags to check for regeration
