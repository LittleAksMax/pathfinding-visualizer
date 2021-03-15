from .app import App
from .algorithms import Algorithms


QUICK_SOLVE = 0b001  # no drawing until end
RANDOM_MAZE = 0b010  # generate a random maze for solve
RANDOM_START_AND_END = 0b100  # create start and end nodes randomly


def run(grid_side, algorithm, run_flags=0b000):
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
