from typing import List

import pytest

from maze_path_finder import weights, MazePosition


class TestPathFinder:
    @pytest.mark.parametrize(
        ("maze", "expected_weights"),
        [
            (
                [[".", "."], [".", "."]],
                [[0, 1, 1, 0], [1, 0, 0, 1], [1, 0, 0, 1], [0, 1, 1, 0],],
            ),
            (
                [[".", "."], [".", "W"]],
                [[0, 1, 1, 0], [1, 0, 0, 0], [1, 0, 0, 0], [0, 0, 0, 0],],
            ),
            (
                [["W", "W"], ["W", "W"]],
                [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0],],
            ),
        ],
    )
    def test_weights(
        self, maze: List[List[MazePosition]], expected_weights: List[List[int]]
    ) -> None:
        w = weights(maze, inf=0)
        assert w == expected_weights
