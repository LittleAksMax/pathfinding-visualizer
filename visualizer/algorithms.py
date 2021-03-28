from .spot_stat import SpotState
from queue import PriorityQueue  # for astar and dijkstras


# enum of different pathfinding algorithms #
class Algorithms(object):
    AStar, BFS, DFS, Dijkstra = range(4)


def reconstruct_path(came_from, current, draw):  # c
    distance = 0

    while current in came_from:
        current = came_from[current]
        current.set_state(SpotState.Path)
        distance += 1
        draw()

    return distance


def bfs(start_node, end_node, spot_grid, draw, quick_solve):  # spot_grid included for concurrency between algorithms
    came_from = dict({})  # to reconstruct path

    open_set = [start_node]  # treat like queue, queue.pop(0)
    closed_set = set({})
    while len(open_set) > 0:
        node = open_set.pop(0)

        if node == end_node:
            distance = reconstruct_path(came_from, end_node, draw)
            return distance

        if node != start_node:
            node.set_state(SpotState.Closed)
        closed_set.add(node)  # add to closed set

        for neighbor in node.neighbors:
            if neighbor in open_set or neighbor in closed_set:
                continue
            came_from[neighbor] = node
            neighbor.set_state(SpotState.Open)  # change state
            open_set.append(neighbor)

        # draw
        if not quick_solve:
            draw()

    return 0  # no distance as didn't finish


def dfs(start_node, end_node, spot_grid, draw, quick_solve):
    came_from = dict({})
    open_set = [start_node]  # treat as stack, open_set.pop()
    closed_set = set({})

    while len(open_set) > 0:
        node = open_set.pop()
        
        if node == end_node:
            distance = reconstruct_path(came_from, end_node, draw)
            return distance

        if node != start_node:
            node.set_state(SpotState.Closed)
        closed_set.add(node)

        for neighbor in node.neighbors:
            if neighbor in open_set or neighbor in closed_set:
                continue
            came_from[neighbor] = node
            neighbor.set_state(SpotState.Open)
            open_set.append(neighbor)

        # draw
        if not quick_solve:
            draw()

    return 0


def heuristic(node_1, node_2):
    x1, y1 = node_1
    x2, y2 = node_2
    return abs(x1 - x2) + abs(y1 - y2)  # manhattan distance


def astar(start_node, end_node, spot_grid, draw, quick_solve):
    count = 0
    open_set = PriorityQueue()
    open_set.put((0, count, start_node))
    came_from = dict({})
    g_score = {spot: float("inf") for row in spot_grid for spot in row}
    g_score[start_node] = 0
    f_score = {spot: float("inf") for row in spot_grid for spot in row}
    f_score[start_node] = heuristic((start_node.x, start_node.y), (end_node.x, end_node.y))
    closed_set = set({})

    open_set_hash = {start_node}
    while not open_set.empty():

        current = open_set.get()[2]
        open_set_hash.remove(current)
        closed_set.add(current)

        if current == end_node:
            distance = reconstruct_path(came_from, end_node, draw)
            return distance

        for neighbor in current.neighbors:
            temp_g_score = g_score[current] + 1

            if temp_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = temp_g_score
                f_score[neighbor] = temp_g_score + heuristic((neighbor.x, neighbor.y), (end_node.x, end_node.y))
                if neighbor in open_set_hash or neighbor in closed_set:
                    continue
                count += 1
                open_set.put((f_score[neighbor], count, neighbor))
                open_set_hash.add(neighbor)
                neighbor.set_state(SpotState.Open)

        # draw
        if not quick_solve:
            draw()

        if current != start_node:
            current.set_state(SpotState.Closed)

    return 0


def dijkstra(start_node, end_node, spot_grid, draw, quick_solve):
    distance = {spot: float("inf") for row in spot_grid for spot in row}
    distance[start_node] = 0

    came_from = dict({})

    open_set = PriorityQueue()  # Priority queue of all nodes in spot_grid
    open_set.put((0, start_node))
    open_set_hash = {start_node}

    closed_set = set({})  # set with all closed nodes

    while not open_set.empty():

        current = open_set.get()[1]  # get smallest
        open_set_hash.remove(current)
        closed_set.add(current)

        if current == end_node:
            distance = reconstruct_path(came_from, end_node, draw)
            return distance

        for neighbor in current.neighbors:
            alt = distance[current] + 1  # Alternative path distance, 1 since you can only go N, E, S, W
            if alt > distance[current]:  # new shortest path, update priority queue

                if neighbor in open_set_hash or neighbor in closed_set:
                    continue

                distance[neighbor] = alt
                came_from[neighbor] = current

                open_set.put((distance[neighbor], neighbor))
                open_set_hash.add(neighbor)
                neighbor.set_state(SpotState.Open)

        # draw
        if not quick_solve:
            draw()

        if current != start_node:
            current.set_state(SpotState.Closed)

    return 0
