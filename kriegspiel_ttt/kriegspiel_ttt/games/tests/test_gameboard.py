import pytest

from kriegspiel_ttt.games.gameboard import GameBoard


class TestGameBoard:
    def test_game_board_construction(self):
        gb = GameBoard()
        assert len(gb.x_board) == 3
        for row in gb.x_board:
            assert len(row) == 3
        assert len(gb.o_board) == 3
        for row in gb.o_board:
            assert len(row) == 3
        assert len(gb.xo_board) == 3
        for row in gb.xo_board:
            assert len(row) == 3
        assert gb.score['x'] == 0
        assert gb.score['o'] == 0
        assert gb.active == "x"
        assert gb.active_board == gb.x_board
        assert gb.passive_board == gb.o_board

    def test_play(self):
        def _assert(gb, x_score, o_score, current_move):
            assert gb.score['x'] == x_score
            assert gb.score['o'] == o_score
            assert gb.current_move == current_move

        gb = GameBoard()
        for k in range(6):
            i = k // 2
            _assert(gb, 0, 0, k)
            gb.play(i, i)
        _assert(gb, 0, 1, 6)

    def test_winner(self):
        gb = GameBoard()
        with pytest.raises(AssertionError):
            gb.winner()

        for i in range(3):
            for j in range(3):
                for _ in ['x', 'o']:
                    gb.play(i, j)
        assert gb.winner() == 'o'


    def test_end_turn(self):
        gb = GameBoard()
        assert gb.score['x'] == 0
        assert gb.score['o'] == 0
        assert gb.active == "x"
        assert gb.current_move == 0

