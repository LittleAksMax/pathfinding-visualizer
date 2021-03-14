import visualizer
import sys


if __name__ == '__main__':
    visualizer.run(50, 50, visualizer.ASTAR | visualizer.QUICK_SOLVE)
    sys.exit()
