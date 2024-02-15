from dataclasses import dataclass, field
from itertools import chain
from typing import ClassVar, Dict, List

from dataclasses_json import dataclass_json


def _empty_board_factory():
    return [
        [None, None, None],
        [None, None, None],
        [None, None, None]
    ]


@dataclass_json
@dataclass
class GameBoard:
    x_board: List[List[int | None]] = field(default_factory=_empty_board_factory)
    o_board: List[List[int | None]] = field(default_factory=_empty_board_factory)
    xo_board: List[List[str | None]] = field(default_factory=_empty_board_factory)
    score: Dict[str, int] = field(default_factory=lambda: {"x": 0, "o": 0})
    current_move: int = 0

    LINES: ClassVar =\
        [[[0, 0], [1, 0], [2, 0]],
         [[0, 1], [1, 1], [2, 1]],
         [[0, 2], [1, 2], [2, 2]],
         [[0, 0], [0, 1], [0, 2]],
         [[1, 0], [1, 1], [1, 2]],
         [[2, 0], [2, 1], [2, 2]],
         [[0, 0], [1, 1], [2, 2]],
         [[0, 2], [1, 1], [2, 0]]]

    def __post_init__(self):
        self.active = "x"
        self.passive = "o"

    @property
    def active_board(self):
        if self.active == "x":
            return self.x_board
        return self.o_board

    @property
    def passive_board(self):
        if self.active == "x":
            return self.o_board
        return self.x_board

    def end_turn(self):
        self.active, self.passive = self.passive, self.active
        self.current_move += 1

    def play(self, i, j):
        assert not self.is_game_over()
        assert self.active_board[i][j] is None, "You have already moved here"
        assert self.xo_board[i][j] is None, "This location is already taken"
        self.active_board[i][j] = self.current_move
        if self.passive_board[i][j] is not None:
            self.xo_board[i][j] = self.active
            self.score[self.active] += self.check_for_lines_through(i, j)
        self.end_turn()

    def check_for_lines_through(self, i, j):
        new_lines = 0
        for line in self.LINES:
            if [i, j] in line:
                if all(self.xo_board[_i][_j] == self.active for _i, _j in line):
                    new_lines += 1
        return new_lines

    def is_game_over(self):
        return all(chain.from_iterable(self.xo_board))

    def winner(self):
        assert self.is_game_over(), "The game is not over"
        return max(self.score, key=self.score.get)
