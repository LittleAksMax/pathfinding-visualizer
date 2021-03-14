from .app import App
from .algorithms import Algorithms


QUICK_SOLVE = 0b001  # no drawing until end
RANDOM_START_AND_END = 0b010  # create start and end nodes randomly
RANDOM_MAZE = 0b100  # generate a random maze for solve


def run(grid_side, algorithm, run_flags=0b0000):
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
