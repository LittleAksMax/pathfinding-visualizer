import visualizer
import sys


if __name__ == '__main__':
    sys.setrecursionlimit(10000)
    visualizer.run(45, "DIJKSTRA", visualizer.RANDOM_MAZE)  \
        # 21, 27, 35, 45, 63, 105, 135

    sys.exit()
