import visualizer
import sys


if __name__ == '__main__':
    sys.setrecursionlimit(10000)
    visualizer.run(40, "A*", visualizer.RANDOM_MAZE)  \
        # side should be a drop down with all factors of 720, except 720, 360, 180, 240, 1, 2, 3, 4, 5

    sys.exit()
