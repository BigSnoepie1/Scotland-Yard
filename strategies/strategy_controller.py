from implementation import board, game, node
from strategies import strategy


class GameController:
    def __init__(
        self, game: game.Game, strategy: strategy.Strategy | None = None
    ) -> None:
        self._game = game
        self._strategy = strategy
        self._current_move = 1
        self._visible_moves = [3, 8, 13, 18]

    def get_possible_mister_x_locations(self) -> int:
        mister_x_history = self._game._mister_x_history
        detective_history = self._game._detectives_history

    def move_manual(self, detective_id, goal) -> None:
        pass

    def auto_play(self, number_of_rounds: int = 30) -> None:
        pass
