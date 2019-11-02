from typing import Union, List, TypeVar

EMPTY = "."
WALL = "W"
MazePosition = str
ListItem = TypeVar("ListItem")


INF = 10 ** 10


def weights(maze: List[List[MazePosition]], inf: int = INF) -> List[List[int]]:
    size = len(maze)

    def get_flat_index(x: int, y: int) -> int:
        return x * size + y

    w = [[inf for _ in range(size ** 2)] for _ in range(size ** 2)]

    for i, row in enumerate(maze):
        for j, cell in enumerate(row):
            if cell == WALL:
                continue

            current_cell_index = get_flat_index(i, j)

            for shift_i, shift_j in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                if not (0 <= i + shift_i < size):
                    continue
                if not (0 <= j + shift_j < size):
                    continue
                if maze[i + shift_i][j + shift_j] == WALL:
                    continue

                adjacent_cell_index = get_flat_index(i + shift_i, j + shift_j)
                w[current_cell_index][adjacent_cell_index] = 1

    return w


def dijkstra(w: List[List[int]], start: int, inf: int = INF) -> List[int]:
    n = len(w)

    dist = [INF] * n
    dist[start] = 0

    used = [False] * n

    min_dist = 0
    min_vertex = start

    while min_dist < INF:
        i = min_vertex
        used[i] = True
        for j in range(n):
            if dist[i] + w[i][j] < dist[j]:
                dist[j] = dist[i] + w[i][j]
        min_dist = INF
        for j in range(n):
            if not used[j] and dist[j] < min_dist:
                min_dist = dist[j]
                min_vertex = j

    return dist


def path_finder(maze: str) -> Union[int, bool]:
    if maze.strip().replace(EMPTY, "").replace(WALL, "").replace("\n", ""):
        raise ValueError(
            "Maze may contain only following characters: ('.', 'W', '\\n')"
        )

    parsed_maze: List[List[MazePosition]] = [list(row.strip()) for row in maze.split()]

    if parsed_maze[0][0] == WALL or parsed_maze[-1][-1] == WALL:
        raise ValueError("Maze start and finish positions should be empty")

    if len(parsed_maze) != len(parsed_maze[0]):
        raise ValueError("Maze should be a square")

    w = weights(parsed_maze)

    dist = dijkstra(w, 0)
    if dist[-1] == INF:
        return False

    return dist[-1]
