from typing import (
    Any,
    Union,
    List,
    Tuple,
    Iterable,
    Set,
)
import heapq

EMPTY = "."
WALL = "W"
MazePosition = str


INF = 10 ** 10


class PriorityQueue:
    elements: List[Any]

    def __init__(self) -> None:
        self.elements = []

    def empty(self) -> bool:
        return len(self.elements) == 0

    def put(self, item: Any, priority: float) -> None:
        heapq.heappush(self.elements, (priority, item))

    def get(self) -> Any:
        return heapq.heappop(self.elements)[1]


Point = Tuple[int, int]


class SquareGrid:
    width: int
    height: int
    walls: Set[Point]

    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height
        self.walls = set()

    def in_bounds(self, id: Point) -> bool:
        (x, y) = id
        return 0 <= x < self.width and 0 <= y < self.height

    def passable(self, id: Point) -> bool:
        return id not in self.walls

    def neighbors(self, id: Point) -> Iterable[Point]:
        (x, y) = id
        results = [(x + 1, y), (x, y - 1), (x - 1, y), (x, y + 1)]
        if (x + y) % 2 == 0:
            results.reverse()  # aesthetics
        return filter(self.passable, filter(self.in_bounds, results))

    def cost(self, *args) -> int:
        return 1


def heuristic(a: Point, b: Point) -> int:
    (x1, y1) = a
    (x2, y2) = b
    return abs(x1 - x2) + abs(y1 - y2)


def a_star_search(graph: SquareGrid, start: Point, goal: Point) -> int:
    frontier = PriorityQueue()
    frontier.put(start, 0)
    cost_so_far = {}
    cost_so_far[start] = 0

    while not frontier.empty():
        current = frontier.get()

        if current == goal:
            break

        for next in graph.neighbors(current):
            new_cost = cost_so_far[current] + graph.cost(current, next)
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost + heuristic(goal, next)
                frontier.put(next, priority)

    return cost_so_far.get(goal, -1)


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

    size = len(parsed_maze)
    grid = SquareGrid(size, size)
    grid.walls = set(
        (i, j)
        for i, row in enumerate(parsed_maze)
        for j, cell in enumerate(row)
        if cell == WALL
    )

    dist = a_star_search(grid, (0, 0), (size - 1, size - 1))
    if dist == -1:
        return False
    return dist
