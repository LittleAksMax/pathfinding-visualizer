import visualizer
import sys

if __name__ == '__main__':
    sys.setrecursionlimit(10000)
    visualizer.run(35, "A*")  \
        # 21, 27, 35, 45, 63, 105, 135

    sys.exit(0)
