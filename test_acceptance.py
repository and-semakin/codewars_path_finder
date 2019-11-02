from maze_path_finder import path_finder


class TestAcceptance:
    def test_a(self) -> None:
        # fmt: off
        a = "\n".join([
            ".W.",
            ".W.",
            "...",
        ])
        # fmt: on
        assert path_finder(a) == 4

    def test_b(self) -> None:
        # fmt: off
        b = "\n".join([
            ".W.",
            ".W.",
            "W..",
        ])
        # fmt: on
        assert path_finder(b) is False

    def test_c(self) -> None:
        # fmt: off
        c = "\n".join([
            "......",
            "......",
            "......",
            "......",
            "......",
            "......",
        ])
        # fmt: on
        assert path_finder(c) == 10

    def test_d(self) -> None:
        # fmt: off
        d = "\n".join([
            "......",
            "......",
            "......",
            "......",
            ".....W",
            "....W.",
        ])
        # fmt: on
        assert path_finder(d) is False
