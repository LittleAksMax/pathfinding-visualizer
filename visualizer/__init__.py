from .app import App

ASTAR = 0b00001
BFS = 0b00010
DFS = 0b00100
DIJKSTRA = 0b01000
QUICK_SOLVE = 0b10000  # no drawing until end


def run(grid_width, grid_height, run_flags=0b0000):
    application = App(grid_width, grid_height, run_flags)
    application.start()
