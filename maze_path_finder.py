from typing import Union, Literal, List, Tuple

EMPTY = "."
WALL = "W"
MazePosition = Literal[".", "W"]


def dijkstra(
    maze: List[List[MazePosition]],
    source: Tuple[int, int],
    destination: Tuple[int, int],
) -> int:
    return 0


def path_finder(maze: List[List[MazePosition]]) -> Union[int, Literal[False]]:
    if maze[0][0] == WALL or maze[-1][-1] == WALL:
        return False

    if len(maze) != len(maze[0]):
        return False

    size = len(maze)

    weight = dijkstra(maze, (0, 0), (size - 1, size - 1))

    return weight
