from implementation import board, game, node
from strategies import strategy


class GameController:
    def __init__(
        self, board: board.Board, strategy: strategy.Strategy | None = None
    ) -> None:
        self._board = board
        self._strategy = strategy

    def get_possible_mister_x_locations(self) -> int:
        pass

    def move_manual(self, detective_id, goal) -> None:
        pass

    def auto_play(self, number_of_rounds: int = 30) -> None:
        pass
