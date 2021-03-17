import visualizer
import sys


if __name__ == '__main__':
    visualizer.run(40, "A*", visualizer.RANDOM_START_AND_END)  \
        # side should be a drop down with all factors of 720, except 720, 360, 180, 240, 1, 2, 3, 4, 5

    sys.exit()
