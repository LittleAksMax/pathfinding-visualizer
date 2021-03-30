from .spot_stat import SpotState
from .constants import START_COLOR, END_COLOR, CLOSED_COLOR, OPEN_COLOR, OBSTACLE_COLOR, PATH_COLOR


class Spot(object):
    def __init__(self, x, y):
        self.neighbors = []
        self.x = x
        self.y = y
        self.state = SpotState.Unvisited  # the default

    def set_state(self, new_state):
        self.state = new_state

    @classmethod
    def get_rgb_from_state(cls, state):
        if state == SpotState.Start:
            return START_COLOR
        elif state == SpotState.End:
            return END_COLOR
        elif state == SpotState.Obstacle:
            return OBSTACLE_COLOR
        elif state == SpotState.Open:
            return OPEN_COLOR
        elif state == SpotState.Closed:
            return CLOSED_COLOR
        else:
            return PATH_COLOR
        # no need to check for unvisited, as unvisited is the background color

    def __lt__(self, other):
        return False
