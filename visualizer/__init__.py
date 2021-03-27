from .app import App
from .algorithms import Algorithms


QUICK_SOLVE = 0b01  # no drawing until end
RANDOM_MAZE = 0b10  # generate a random maze for solve, creates random start and end point


def run(grid_side, algorithm, run_flags=0b00):
    if algorithm == "A*":
        alg = Algorithms.AStar
    elif algorithm == "BFS":
        alg = Algorithms.BFS
    elif algorithm == "DFS":
        alg = Algorithms.DFS
    else:
        alg = Algorithms.Dijkstra
    application = App(grid_side, run_flags, alg)
    application.start()
